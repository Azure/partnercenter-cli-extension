import fs from 'fs'
import data from './schemas.json' assert { type: 'json' };
import loader from './loader.js';
import processor from './processor.js';
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';

const schemasDir = "./.schemas";
const outDir = "./out";

function ensureDir(dirPath) {
    if (fs.existsSync(dirPath)) {
        fs.rmSync(dirPath, { force: true, recursive: true });
    }
    fs.mkdirSync(dirPath);
}

async function processSchemas(options) {
    ensureDir(schemasDir);
    ensureDir(outDir)


    const schemas = await loader.load(data.urls);
    await processor.process(schemas, options);
}

/**
 *
 * @param {Arguments} args
 */
async function main(args) {
    console.log('Processing Schemas')

    let options = {
        outputEachSchema: false,
        outputPath: outDir
    };

    await processSchemas(options)
}

await main(yargs(hideBin(process.argv)).argv);