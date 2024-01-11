

```bash
datamodel-codegen \
  --input ../jsonschema2openapi/out/definitions.json \
  --output ./out/dataclass_models.py \
  --output-model-type dataclasses.dataclass \
  --snake-case-field \
  --reuse-model \
  --disable-appending-item-suffix \
  --use-title-as-name \
  --use-field-description \
  --use-schema-description \
  --use-standard-collections \
  --allow-population-by-field-name \
  --use-schema-description \
  --input-file-type openapi

datamodel-codegen \
  --input-file-type openapi \
  --input ../jsonschema2openapi/out/definitions.json \
  --output ./out/dataclass_models.py \
  --output-model-type dataclasses.dataclass \
  --reuse-model

```