# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
Recording processors for sanitizing sensitive data in test recordings.
"""

import re
from azure.cli.testsdk.scenario_tests import RecordingProcessor
from azure.cli.testsdk.scenario_tests.utilities import is_text_payload


class SasTokenScrubber(RecordingProcessor):
    """
    Sanitize Azure Storage SAS tokens in test recordings.

    This processor removes sensitive SAS token parameters from:
    - Request URIs
    - Request bodies
    - Response bodies

    SAS token parameters that are sanitized:
    - sig: The cryptographic signature
    - se: Expiry time
    - sv: Storage service version
    - sp: Permissions
    - sr: Resource type
    - st: Start time (optional)
    - sip: IP range (optional)
    - spr: Protocol (optional)
    """

    def process_request(self, request):
        """Sanitize SAS tokens in request URI and body."""
        # Sanitize SAS tokens in request URI
        request.uri = self._sanitize_sas_token(request.uri)

        # Sanitize SAS tokens in request body if present
        if is_text_payload(request) and request.body:
            if isinstance(request.body, bytes):
                body = request.body.decode('utf-8')
                request.body = self._sanitize_sas_token(body).encode('utf-8')
            else:
                request.body = self._sanitize_sas_token(request.body)

        return request

    def process_response(self, response):
        """Sanitize SAS tokens in response body."""
        if is_text_payload(response) and response['body']['string']:
            response['body']['string'] = self._sanitize_sas_token(
                response['body']['string']
            )
        return response

    def _sanitize_sas_token(self, content):
        """
        Replace SAS token parameters with sanitized values.

        Args:
            content: String content that may contain SAS tokens

        Returns:
            String with sanitized SAS tokens
        """
        if not content:
            return content

        # List of SAS token parameters and their sanitized replacements
        # Order matters: process 'sig' before other parameters to avoid partial matches
        sas_patterns = [
            # Signature - most sensitive, sanitize first
            (r'sig=[^&\s"\']+', 'sig=SANITIZED_SIGNATURE'),

            # Expiry time - use far future date
            (r'se=[^&\s"\']+', 'se=2099-01-01T00%3A00%3A00Z'),

            # Start time - use past date
            (r'st=[^&\s"\']+', 'st=2020-01-01T00%3A00%3A00Z'),

            # Storage service version
            (r'sv=[^&\s"\']+', 'sv=2021-01-01'),

            # Permissions - sanitize to read-only
            (r'sp=[^&\s"\']+', 'sp=r'),

            # Resource type
            (r'sr=[^&\s"\']+', 'sr=b'),

            # IP range (optional parameter)
            (r'sip=[^&\s"\']+', 'sip=0.0.0.0-255.255.255.255'),

            # Protocol (optional parameter)
            (r'spr=[^&\s"\']+', 'spr=https'),
        ]

        result = content
        for pattern, replacement in sas_patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

        return result
