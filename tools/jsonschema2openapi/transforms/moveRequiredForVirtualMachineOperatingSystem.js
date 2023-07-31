
import SchemaInfo from '../schemaInfo.js';
import JSONPath from 'jsonpath'


/**
 * the VirtualMachineOperatingSystem component has a oneOf. Below this is a "required" with the defined required properties
 * This causes an error in the data model code generate.
 *
 * This takes the required JSON attr, removes it and distributes to each anonymous object in the "oneOf"

 * @param {object} component
 */
function moveRequiredForVirtualMachineOperatingSystem(component) {
    if (component.name == "VirtualMachineOperatingSystem") {
        let required = [];
        required = component.document.required;
        delete component.document.required;

        JSONPath.apply(component.document, '$..oneOf', (oneOf) => {
            for (const obj of oneOf) {
                obj['required'] = required;
            }
            return oneOf;
        });
    }
}


export default moveRequiredForVirtualMachineOperatingSystem;