
import SchemaInfo from '../schemaInfo.js';
import JSONPath from 'jsonpath'

/**
 * the objective is to consolidate all these types to a common "definitions.js"
 * This will replace the JSON Schema $ref values with a local reference
 * so we can do the following in the file that defines the paths: './definitions.json#/components/schemas/<Component>'
 * @param {object} component
 */
function replaceRefs(component) {
    // process references INSIDE $ref
    JSONPath.apply(component.document, '$..["$ref"]', (value) => {
        // replace HTTP reference to a JSON Schema with the local reference of the openapi component
        if (value.startsWith('http')) {
            const componentName = new SchemaInfo(value).componentName();
            return `#/components/schemas/${componentName}`
        }

        // replace what was a $def local json schema reference with
        // the "x-$defs" path (which is done during conversion)
        if (value.indexOf('$defs') != -1) {
            return value.replace('$defs', 'components/schemas');
        }

        return value;
    });

    if (component.document["x-$defs"]) {
        //clean up x-$defs which is a conversion of references to the JSON Schemas
        //remove the HTTP json schema objects here since they will get referenced
        //locally
        const orphanedExternalKeys = Object.keys(component.document["x-$defs"]).filter(k => k.startsWith("http"));
        orphanedExternalKeys.forEach(key => {
            delete component.document["x-$defs"][key];
        });
    }
}


export default replaceRefs;