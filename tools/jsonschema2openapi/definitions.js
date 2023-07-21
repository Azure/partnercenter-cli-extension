
import path from 'path'
import fs from 'fs'
import {OpenApiPath} from './openapipath.js';

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
            if (!spec.components.schemas[key]) { //if already exists, we have a conflict
                spec.components.schemas[key] = component.document["x-$defs"][key]
            }
        });
        delete component.document["x-$defs"];
    }
}

const createDefinitions = function (components) {
    const json = readFile(definitionsTemplatePath);
    let spec = JSON.parse(json);

    for (const component of components) {
        const path = getPathForComponent(component);
        // todo: add function to determine if component should be included in path
        if (path) {
            console.log('Found the Product');
            spec.paths = path;
        }
        moveDefsToCommponentsSchemas(spec, component)
        spec.components.schemas[component.name] = component.document;
    }

    return spec;
}

const getPathForComponent = function (component) {
    if (component.name === "Product") {
        console.log('Found the Product');
        const productPath = new OpenApiPath("./definitions.json#/components/schemas/DurableId", `./definitions.json#/components/schemas/${component.name}`, component.name);
        return productPath;
    }
    return null;
}

export default createDefinitions;