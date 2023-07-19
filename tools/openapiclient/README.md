

[Python Generator](https://openapi-generator.tech/docs/generators/python)

> WARNING: due to the limitations of the generation, the python module structure could not be controlled at the folder AND at the code level. The import statements had to be fixed, so if regenerating, the imports will need to be manually fixed.
Generate code using v1 key, defined in openapitools.json
```
npx @openapitools/openapi-generator-cli generate --generator-key v1
```

Extract the templates to view/customize if necessary
```
npx @openapitools/openapi-generator-cli author template -g python
```