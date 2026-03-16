# Security Testing Guidelines

This document outlines security best practices for testing the Partner Center CLI extension.

## Preventing Credential Leaks in Test Recordings

### Overview

Azure CLI test recordings can inadvertently capture sensitive credentials such as:
- Azure Storage SAS tokens
- Access keys
- Service principal credentials
- Subscription IDs
- API keys

To prevent these from being committed to the repository, we have implemented automated scrubbing.

### How It Works

#### 1. Automatic Scrubbing (Preferred)

All tests that inherit from `PartnerCenterScenarioTest` automatically apply the `SasTokenScrubber` recording processor:

```python
from azext_partnercenter.tests.base import PartnerCenterScenarioTest

class MyTest(PartnerCenterScenarioTest):
    def test_something(self):
        # SAS tokens in recordings will be automatically sanitized
        pass
```

The scrubber replaces sensitive SAS token parameters:
- `sig=<signature>` → `sig=SANITIZED_SIGNATURE`
- `se=<expiry>` → `se=2099-01-01T00:00:00Z`
- `sv=<version>` → `sv=2021-01-01`
- `sp=<permissions>` → `sp=r`

#### 2. Manual Review (Required)

**Before committing any test recording files:**

1. **Scan for secrets:**
   ```bash
   # Check for SAS tokens
   grep -r "sig=" partnercenter/azext_partnercenter/tests/latest/recordings/

   # Check for access keys
   grep -r "AccountKey=" partnercenter/azext_partnercenter/tests/latest/recordings/
   ```

2. **Review the diff:**
   ```bash
   git diff partnercenter/azext_partnercenter/tests/latest/recordings/
   ```

3. **Verify sanitization:**
   - Ensure `sig=` values are `SANITIZED_SIGNATURE`
   - Ensure no real expiry dates (should be `2099-01-01`)
   - Ensure no subscription IDs (should be replaced by test framework)

### Secret Scanning Tools

#### GitHub Actions (Automatic)

We use Gitleaks in our CI/CD pipeline to scan all pull requests:
- Workflow: `.github/workflows/secret-scanning.yml`
- Runs automatically on every PR
- Blocks merge if secrets are detected

#### Pre-commit Hooks (Optional)

Developers can install pre-commit hooks to catch secrets before committing:

```bash
# Install pre-commit
pip install pre-commit

# Install the hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

This will run Gitleaks locally before every commit.

#### Manual Scanning with Gitleaks

```bash
# Install Gitleaks
brew install gitleaks  # macOS
# or download from: https://github.com/gitleaks/gitleaks/releases

# Scan the entire repository
gitleaks detect --source . --verbose

# Scan uncommitted changes
gitleaks protect --staged --verbose
```

## Running Tests Without Azure Access

If you don't have access to an Azure subscription for live testing:

### Playback Mode (No Azure Required)

Tests can run in playback mode using existing recordings:

```bash
# Activate virtual environment
source env/bin/activate

# Run tests in playback mode (default)
azdev test partnercenter --test test_marketplace_offer_listing_media
```

Playback mode:
- ✅ Uses recorded YAML files
- ✅ No Azure credentials needed
- ✅ Validates test logic
- ❌ Cannot create new recordings

### Live Mode (Azure Access Required)

To create or update test recordings:

```bash
# Run tests in live mode
azdev test partnercenter --live --test test_marketplace_offer_listing_media
```

Live mode:
- ✅ Makes real API calls to Azure
- ✅ Creates/updates recording files
- ✅ Scrubbers automatically sanitize sensitive data
- ❌ Requires valid Azure credentials

## Common Issues

### Issue: SAS Token in Recording After Running Live Test

**Cause:** Scrubber not applied or regex pattern didn't match

**Solution:**
1. Verify test class inherits from `PartnerCenterScenarioTest`
2. Check that `SasTokenScrubber` is in recording_processors
3. Review the SAS token format - may need to update regex pattern

### Issue: Cannot Regenerate Recording (Lost Azure Access)

**Cause:** Azure subscription decommissioned or access revoked

**Solution:**
1. Use manual sanitization (see example below)
2. Update existing recording file
3. Validate YAML syntax after changes

**Manual Sanitization Example:**
```bash
cd partnercenter/azext_partnercenter/tests/latest/recordings

# Backup original
cp test_file.yaml test_file.yaml.backup

# Sanitize SAS signatures
sed -i '' 's/sig=[^&"]*&/sig=SANITIZED_SIGNATURE\&/g' test_file.yaml
sed -i '' 's/sig=[^&"]*"/sig=SANITIZED_SIGNATURE"/g' test_file.yaml

# Sanitize expiry times
sed -i '' 's/se=[^&"]*&/se=2099-01-01T00%3A00%3A00Z\&/g' test_file.yaml
sed -i '' 's/se=[^&"]*"/se=2099-01-01T00%3A00%3A00Z"/g' test_file.yaml

# Validate YAML
python -c "import yaml; yaml.safe_load(open('test_file.yaml'))"
```

### Issue: Pre-commit Hook Blocking Commit

**Cause:** Gitleaks detected a potential secret

**Solution:**
1. Review the detection - is it a real secret?
2. If real: Remove the secret, use environment variable
3. If false positive: Add to `.gitleaksignore`
4. Never bypass with `--no-verify` for real secrets!

## Best Practices

### DO ✅

- ✅ Always inherit from `PartnerCenterScenarioTest`
- ✅ Review recording files before committing
- ✅ Use short-lived SAS tokens (1-hour expiry) when testing
- ✅ Run secret scanning tools before creating PR
- ✅ Use environment variables for credentials
- ✅ Report any credential leaks immediately

### DON'T ❌

- ❌ Commit test recordings without reviewing them
- ❌ Bypass pre-commit hooks with `--no-verify`
- ❌ Use production credentials in tests
- ❌ Commit long-lived SAS tokens (even if sanitized)
- ❌ Manually edit recording files without sanitizing
- ❌ Push to GitHub before running local secret scan

## Incident Response

If you discover a credential leak in the repository:

### Immediate Actions

1. **DO NOT PANIC** - Most test credentials are short-lived
2. **Verify the credential type and expiration**
3. **Check if it's already expired** (use the expiry timestamp)

### If Credential is Active

1. **Revoke immediately:**
   - SAS tokens: Delete the SAS policy or rotate storage account keys
   - Access keys: Rotate keys in Azure Portal
   - Service principals: Rotate client secrets

2. **Assess exposure:**
   - When was it committed?
   - How long was it active?
   - What permissions did it have?

3. **Report to security team:**
   - Create IcM ticket (if Microsoft internal)
   - Or follow your organization's security incident process

### If Credential is Expired

1. **Verify expiration:**
   ```bash
   # Check expiry timestamp in recording file
   grep "se=" <recording-file>.yaml
   ```

2. **Document:**
   - Create local incident documentation
   - Note that credential was expired
   - Document risk as LOW

3. **Fix going forward:**
   - Implement/verify scrubbers are working
   - Update tests to prevent recurrence
   - Consider git history cleanup (if needed)

## Additional Resources

- [Azure CLI Test Authoring](https://github.com/Azure/azure-cli/blob/dev/doc/authoring_tests.md)
- [Gitleaks Documentation](https://github.com/gitleaks/gitleaks)
- [Pre-commit Framework](https://pre-commit.com/)
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/en-us/securityengineering/sdl)

## Questions?

If you have questions about security testing practices, please:
1. Review this documentation
2. Check existing test examples in the repository
3. Consult with the repository maintainers

---

**Last Updated:** March 15, 2026
**Maintained by:** Partner Center CLI Extension Team
