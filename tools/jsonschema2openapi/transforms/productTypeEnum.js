
import SchemaInfo from '../schemaInfo.js';
import JSONPath from 'jsonpath'


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
function productTypeEnum(component) {
    if (component.name == "Product") {
        JSONPath.apply(component.document, '$..allOf[1].properties.type', (type) => {
            type['title'] = "OfferType";
            return type;
        });

        // we have to set this otherwise we generate "Type" as the name
        JSONPath.apply(component.document, '$..allOf[1].oneOf[0].allOf[0].properties.type', (type) => {
            type['title'] = "Xbox360NonBackcompatType";
            return type;
        });
    }
}


export default productTypeEnum;