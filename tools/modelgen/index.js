import fs from 'fs';
import path from 'path';
import { spawn } from "child_process";


async function generate() {
    if (fs.existsSync('out')) {
        fs.rmSync('out', { force: true, recursive: true });
    }
    fs.mkdirSync('out');
    console.log('Generating Python code...');

    const indent = '  ';

    let options = [
        "--input", '../jsonschema2openapi/out/definitions.json',
        "--output", path.join('./out', "models.py"),
        "--snake-case-field",
        "--reuse-model",
        "--disable-appending-item-suffix",
        "--use-title-as-name",
        "--use-field-description",
        "--use-schema-description",
        "--use-standard-collections",
        "--allow-population-by-field-name",
        "--use-schema-description",
        "--input-file-type", "openapi"];

    const process = spawn("datamodel-codegen", options);
    process.stdout.setEncoding('utf8');
    process.stderr.setEncoding('utf8');

    let data = "";
    for await (const chunk of process.stdout) {
        console.log(indent + chunk);
        data += chunk;
    }

    let error = "";
    for await (const chunk of process.stderr) {
        console.error(indent + chunk);
        error += chunk;
    }
    // process.on('close', () => {
    //     console.log(indent + '  Generation complete.');
    // });
}


async function generateFromSchemasDir() {
    const dir = "schemadirtest";

    if (fs.existsSync('out')) {
        fs.rmSync('out', { force: true, recursive: true });
    }
    fs.mkdirSync('out');
    fs.rmSync(`./${dir}/.DS_Store`, { force: true })

    console.log('Generating Python code...');
    const indent = '  ';

    let options = [
        "--output", "out",
        "--snake-case-field",
        "--disable-appending-item-suffix",
        "--openapi-scopes", "schemas",
        "--reuse-model",
        "--use-title-as-name",
        "--use-field-description",
        "--use-schema-description",
        "--use-standard-collections",
        "--allow-population-by-field-name",
        "--use-schema-description",
        "--input-file-type", "jsonschema"];

    options.push("--input", dir);

    const process = spawn("datamodel-codegen", options);


    let data = "";
    for await (const chunk of process.stdout) {
        console.log(indent+chunk);
        data += chunk;
    }

    let error = "";
    for await (const chunk of process.stderr) {
        console.error(indent+chunk);
        error += chunk;
    }
}

async function main() {
   // await generateFromSchemasFile();
    await generate();
}

/**
 * 1. store all URLs of the schema files
 * 2. Download all
 * 3. rename each file to the name of the specific schema using $id (regex capture name)
 * 4. move file to the folder, named the version from $id
 * 5. replace snakecase with underscore in file name
 * 6. go through each file, and...
 *      - add title attribute with Pascal case of the name of the schema
 *      - find the $ref values and replace with local reference instead of URI
 *      - remove $defs attribute
 *
 */

await main();