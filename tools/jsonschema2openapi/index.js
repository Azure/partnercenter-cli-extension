
import SchemaInfo from './info.js';

import path from 'path'
import fs, { read } from 'fs'
import data from './schemas.json' assert { type: 'json' };
import convert from '@openapi-contrib/json-schema-to-openapi-schema';

const schemasDir = "./.schemas";

function ensureDir(dirPath) {
    if (fs.existsSync(dirPath)) {
        fs.rmSync(dirPath, { force: true, recursive: true });
    }
    fs.mkdirSync(dirPath);
}

async function convertSchema(jsonSchema) {
    const convertedSchema = await convert(jsonSchema, {
        dereference: false,
        dereferenceOptions: {
            dereference: { circular: 'ignore' }
        }
    });
    return convertedSchema
}


function writeFile(specFile) {
    const absolutePath = path.resolve(specFile.path);
    fs.writeFileSync(absolutePath, specFile.contents, { encoding: 'utf-8' });
}

async function processSchemas() {
    ensureDir(schemasDir);
    ensureDir('./out')

    const schemas = data.schemas.map(url => {
        console.log(`creating info for: ${url}`)
        return new SchemaInfo(url, schemasDir)
    });

    for (const schemaInfo of schemas) {
        await schemaInfo.get()

        console.log(` - converting ${schemaInfo.url.name()} to openapi component`)
        const component = await convertSchema(schemaInfo.json)

        const specFile = {
            path: './out/' + schemaInfo.fileName(),
            contents: JSON.stringify(component, null, 2)
        }
        writeFile(specFile)
    }
}


async function main() {
    console.log('Processing Schemas')
    await processSchemas()

}

await main();