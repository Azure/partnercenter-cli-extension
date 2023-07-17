
import path from 'path'
import fs from 'fs'

function readFile(file) {
    const absolutePath = path.resolve(file);
    const json = fs.readFileSync(absolutePath, { encoding: 'utf-8' });
    return json
}

const definitionsTemplatePath = "./templates/definitions.json"

const moveDefsToCommponentsSchemas = function(spec, component) {
    //next we now need to move all remaining x-$defs into the component schemas and remove the key
    if (component.document["x-$defs"]) {
        const xdefsKeys = Object.keys(component.document["x-$defs"])
        xdefsKeys.forEach(key => {
            if (spec.components.schemas[key]) { //if already exists, we have a conflict
                throw new Error("$def already exists in schemas " + key);
            }
            spec.components.schemas[key] = component.document["x-$defs"][key]
        });
        delete component.document["x-$defs"];
    }
}

const createDefinitions = function (components) {
    const json = readFile(definitionsTemplatePath);
    let spec = JSON.parse(json);

    for (const component of components) {
        moveDefsToCommponentsSchemas(spec, component)
        spec.components.schemas[component.name] = component.document;
    }

    return spec;
}

export default createDefinitions;