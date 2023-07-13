
import https from 'https'

import path from 'path'
import fs, { read } from 'fs'
import data from './schemas.json' assert { type: 'json' };
import convert from '@openapi-contrib/json-schema-to-openapi-schema';

function ensureSchemasDir() {
    const dirname = ".schemas"
    if (fs.existsSync(dirname)) {
        fs.rmSync(dirname, { force: true, recursive: true });
    }
    fs.mkdirSync(dirname);
}

async function downloadSchema(schema) {
    let promise = new Promise((resolve, reject) => {
        https.get(schema.url, res => {
            res.on('end', () => {
                setTimeout(() => {
                    resolve();
                }, 100);
            }).pipe(fs.createWriteStream('./.schemas/' + schema.name), { end: true })
        })
    });
    await promise;
}

async function convertSchema(jsonSchema) {
    const convertedSchema = await convert(jsonSchema, {
        dereference: true,
        dereferenceOptions: {
            dereference: { circular: 'ignore' }
        }
    });
    return convertedSchema
}

function readFile(file) {
    const absolutePath = path.resolve(file);
    const json = fs.readFileSync(absolutePath, { encoding: 'utf-8' });
    return json
}

function writeFile(spec) {
    const absolutePath = path.resolve("./out/" + spec.name);
    fs.writeFileSync(absolutePath, spec.contents, { encoding: 'utf-8' });
}

async function processSchemas() {
    for (const schema of data.schemas) {
        console.log(`downloading ${schema.name}`)
        await downloadSchema(schema)

        let content = readFile('./.schemas/' + schema.name)
        //console.log(content)
        const json = JSON.parse(content)
        const component = await convertSchema(json)
        const spec = {
            name: schema.name,
            contents: JSON.stringify(component, null, 2)
        }
        writeFile(spec)
    }
}


async function main() {
    console.log('main')

    ensureSchemasDir()
    await processSchemas()

}

await main();