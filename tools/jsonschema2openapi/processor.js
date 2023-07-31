import convert from '@openapi-contrib/json-schema-to-openapi-schema';
import fs from 'fs'
import path from 'path'
import SchemaInfo from './schemaInfo.js';
import replaceRefs from './transforms/replaceRefs.js';
import createDefinitions from './definitions.js';
import addTitles from './transforms/addTitles.js';
import removeUnsupportedFormats from './transforms/removeUnsupportedFormats.js';

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

class JsonSchemaProcessOptions {
    outputPath = './out'
    outputEachSchema;
    verbose;
}

class JsonSchemaProcessor {
    transforms = []

    /**
     *
     * @param {Array<Function>} transforms
     */
    constructor(transforms) {
        this.transforms = transforms;
    }

    async convert(schemas, options) {
        const components = [];

        console.log('  Converting to OpenAPI.')
        for (const schemaInfo of schemas) {

            console.log(`  - ${schemaInfo.name()}`);

            // converted Open API object
            const document = await convertSchema(schemaInfo.json);

            // inline construction of openapi component type { name, document }
            let component = {
                name: schemaInfo.componentName(),
                document: document,
                info: schemaInfo
            };

            this.transforms.forEach(async transform => await transform(component));

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
        //console.log(`The components are: ${JSON.stringify(components)}`)
        let definitions = await createDefinitions(components);
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
    async process(schemas, options) {
        console.log('Processing JSON schemas. ' + JSON.stringify(options))
        await this.convert(schemas, options)
    }
}

const processor = new JsonSchemaProcessor(
    [replaceRefs, addTitles, removeUnsupportedFormats]
);

export default processor