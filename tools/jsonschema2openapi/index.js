import fs from 'fs'
import data from './schemas.json' assert { type: 'json' };
import loader from './loader.js';
import processor from './processor.js';

const schemasDir = "./.schemas";
const outDir = "./out";

function ensureDir(dirPath) {
    if (fs.existsSync(dirPath)) {
        fs.rmSync(dirPath, { force: true, recursive: true });
    }
    fs.mkdirSync(dirPath);
}

async function processSchemas() {
    ensureDir(schemasDir);
    ensureDir(outDir)


    const schemas = await loader.load(data.urls);
    await processor.process(schemas, { outputEachSchema: false, outputPath: './out' });
}


async function main() {
    console.log('Processing Schemas')
    await processSchemas()
}

await main();