import convert from '@openapi-contrib/json-schema-to-openapi-schema';
import fs from 'fs'
import path from 'path'
import SchemaInfo, { SchemaUrl } from './schemaInfo.js';
import JSONPath from 'jsonpath'
import createDefinitions from './definitions.js';

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
 * This will replace the JSON Schema $ref values with a local reference
 * so we can do the following in the file that defines the paths: './definitions.json#/components/schemas/<Component>'
 * @param {object} component
 */
function replaceRefs(component) {
    // process references INSIDE $ref
    JSONPath.apply(component.document, '$..["$ref"]', (value) => {
        // replace HTTP reference to a JSON Schema with the local reference of the openapi component
        if (value.startsWith('http')) {
            return `#/components/schemas/${component.name}`
        }

        // replace what was a $def local json schema reference with
        // the "x-$defs" path (which is done during conversion)
        if (value.indexOf('$defs') != -1) {
            return value.replace('$defs', 'components/schemas');
        }

        return value;
    });

    if (component.document["x-$defs"]) {
        //clean up x-$defs which is a conversion of references to the JSON Schemas
        //remove the HTTP json schema objects here since they will get referenced
        //locally
        const orphanedExternalKeys = Object.keys(component.document["x-$defs"]).filter(k => k.startsWith("http"));
        orphanedExternalKeys.forEach(key => {
            delete component.document["x-$defs"][key];
        });
    }
}

class JsonSchemaProcessOptions {
    outputPath = './out'
    outputEachSchema = false;
}

class JsonSchemaProcessor {
    async convert(schemas, options) {
        const components = [];

        console.log('  Converting to OpenAPI.')
        for (const schemaInfo of schemas) {
            console.log(`  - ${schemaInfo.name()}`);

            // converted Open API object
            const document = await convertSchema(schemaInfo.json);

            let component = {
                name: toPascalCase(schemaInfo.name()).replace(/-/g, ''),
                document: document
            };

            replaceRefs(component);

            if (options.outputEachSchema) {
                const specFile = {
                    path: path.join(options.outputPath, schemaInfo.fileName()),
                    contents: JSON.stringify(component.document, null, 2)
                };
                writeFile(specFile);
            }

            components.push(component)
        }

        console.log('  Writing definitions file.')
        let definitions = createDefinitions(components);
        const specFile = {
            path: path.join(options.outputPath, 'definitions.json'),
            contents: JSON.stringify(definitions, null, 2)
        };
        writeFile(specFile);

        console.log("Done.")
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