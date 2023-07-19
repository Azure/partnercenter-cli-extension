
import JSONPath from 'jsonpath'

/**
 * Removes duration format which can't be processed by code gen

 * @param {object} component
 */
function removeUnsupportedFormats(component) {
    JSONPath.apply(component.document, '$..format', (value) => {
        if (value === "duration") {
            return ""
        }
        return value;
    });
}


export default removeUnsupportedFormats;