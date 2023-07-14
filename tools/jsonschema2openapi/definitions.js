
import path from 'path'
import fs from 'fs'

function readFile(file) {
    const absolutePath = path.resolve(file);
    const json = fs.readFileSync(absolutePath, { encoding: 'utf-8' });
    return json
}

const definitionsTemplatePath = "./templates/definitions.json"

const createDefinitions = function (components) {
    const json = readFile(definitionsTemplatePath);
    let spec = JSON.parse(json);

    for (const component of components) {
        spec.definitions[component.name] = component.document;
    }
    return spec;
}

export default createDefinitions;