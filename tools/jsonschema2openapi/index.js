import fs from 'fs'
import data from './schemas.json' assert { type: 'json' };
import loader from './loader.js';
import processor from './processor.js';
import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';

const schemasDir = "./.schemas";
const outDir = "./out";

function ensureDir(dirPath, options) {
    if (options.clean) {
        if (fs.existsSync(dirPath)) {
            fs.rmSync(dirPath, { force: true, recursive: true });
        }
        fs.mkdirSync(dirPath);
        return;
    }

    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath);
    }
}

async function processSchemas(options) {
    ensureDir(schemasDir, { clean: false });
    ensureDir(outDir, { clean: true })


    const schemas = await loader.load(data.urls);
    await processor.process(schemas, options);
}

/**
 *
 * @param {Arguments} args
 */
async function main(args) {
    console.log('Processing Schemas')

    const outputEachSchema = args["output-each-schema"];
    let options = {
        outputEachSchema: outputEachSchema,
        outputPath: outDir
    };

    await processSchemas(options)
}

await main(yargs(hideBin(process.argv)).argv);