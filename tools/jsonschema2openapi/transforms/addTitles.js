
import SchemaInfo from '../schemaInfo.js';
import JSONPath from 'jsonpath'
import productTypeEnum from './productTypeEnum.js';


const REFERENCE_SUFFIX = "Reference";

function filterObjects(item) {
    return item["type"] && item["type"] === "object"
}

/**
 * This will add the "title" attribute to all the types that are "type": "object"
 * this is so that the title value can be picked up and the model generator will then
 * use this value to generate class or enum values

 * @param {object} component
 */
function addTitles(component) {
    JSONPath.apply(component.document, '$..title', (value) => {
        return component.name;
    });

    JSONPath.apply(component.document, '$..oneOf', (oneOf) => {
        oneOf.filter(filterObjects).forEach(item => {

            if (item["required"]) {
                let title = item["required"][0];
                title = title.charAt(0).toUpperCase() + title.slice(1);

                const refs = JSONPath.query(item, '$..["$ref"]');
                if (refs.length > 0) {
                    const ref = refs[0];
                    if (ref.indexOf(REFERENCE_SUFFIX) != -1) {
                        title += REFERENCE_SUFFIX;
                    }
                }
                item["title"] = title;
            }
        })
        return oneOf;
    });

    productTypeEnum(component);
}


export default addTitles;