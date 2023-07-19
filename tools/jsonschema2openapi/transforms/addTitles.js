
import SchemaInfo from '../schemaInfo.js';
import JSONPath from 'jsonpath'



function toPascalCase(str) {
    return str.replace(/(\w)(\w*)/g, function (g0, g1, g2) { return g1.toUpperCase() + g2.toLowerCase(); });
}

function filterObjects(item) {
    return item["type"] && item["type"] === "object"
}
/**
 * the objective is to consolidate all these types to a common "definitions.js"
 * This will replace the JSON Schema $ref values with a local reference
 * so we can do the following in the file that defines the paths: './definitions.json#/components/schemas/<Component>'
 * @param {object} component
 */
function addTitles(component) {
    // process references INSIDE $ref
    JSONPath.apply(component.document, '$..oneOf', (oneOf) => {
        oneOf.filter(filterObjects).forEach(item => {
            console.log(item);

            if (item["required"]) {
                item["title"] = toPascalCase(item["required"][0]);
            }
        })
        return oneOf;
    });
}


export default addTitles;