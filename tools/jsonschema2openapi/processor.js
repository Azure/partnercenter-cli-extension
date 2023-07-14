import convert from '@openapi-contrib/json-schema-to-openapi-schema';
import fs from 'fs'
import path from 'path'
import SchemaInfo, { SchemaUrl } from './schemaInfo.js';
import JSONPath from 'jsonpath'

function writeFile(specFile) {
    const filePath = path.resolve(specFile.path);
    fs.writeFileSync(filePath, specFile.contents, { encoding: 'utf-8' });
}

/**
     * converts the JSON schema to open api
     * @param {object} schema
     * @returns
     */
async function convertSchema(schema) {
    const options = {
        dereference: false,
        convertUnreferencedDefinitions: true,
        dereferenceOptions: {
            dereference: { circular: 'ignore' }
        }
    };

    const convertedSchema = await convert(schema, options);
    return convertedSchema
}

function toPascalCase(str) {
    return str.replace(/(\w)(\w*)/g, function (g0, g1, g2) { return g1.toUpperCase() + g2.toLowerCase(); });
}

/**
 * the objective is to consolidate all these types to a common "definitions.js"
 * This will replace the JSON Schema $ref values with a local reference to './definitions.json#/definitions/<Component>'
 * @param {object} component
 */
function replaceRefs(document) {
    let updated = document;
    JSONPath.apply(updated, '$..["$ref"]', (value) => {
        if (value.startsWith('http')) {
            const schemaUrl = new SchemaUrl(value);
            const name = toPascalCase(schemaUrl.name()).replace(/-/g, '');
            return `./definitions.json#/definitions/${name}`
        }
        return value;
    });
    return updated;
}

class JsonSchemaProcessOptions {
    outputPath = './out'
}

class JsonSchemaProcessor {
    async convert(schemas, options) {
        console.log('  Converting to OpenAPI.')
        for (const schemaInfo of schemas) {
            console.log(`  - ${schemaInfo.name()}`);

            // converted Open API object
            const document = await convertSchema(schemaInfo.json);
            const updated = replaceRefs(document);

            const specFile = {
                path: path.join(options.outputPath, schemaInfo.fileName()),
                contents: JSON.stringify(updated, null, 2)
            };
            writeFile(specFile);
        }
    }

    /**
     * processes all the schema infos provided and commits the convertions to output path
     * using the file name provided by the schema info
     * @param {Array<SchemaInfo>} schemas
     * @param {JsonSchemaProcessOptions} options
     */
    async process(schemas, options = new JsonSchemaProcessOptions()) {
        console.log('Processing JSON schemas.')
        await this.convert(schemas, options)
    }
}

const processor = new JsonSchemaProcessor();

export default processor