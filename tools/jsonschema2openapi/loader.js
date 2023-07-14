
import SchemaInfo from "./schemaInfo.js";

class JsonSchemaLoadOptions {
    outputPath = './.schemas';
}

class JsonSchemaLoader {
    /**
     *
     * @param {Array<string>} schemaUrls
     * @param {JsonSchemaLoadOptions} options
     */
    async load(schemaUrls, options = new JsonSchemaLoadOptions()) {
        console.log('Loading schemas from urls.')

        const schemas = schemaUrls.map(url => {
            console.log(`  - ${url}`)
            return new SchemaInfo(url, options.outputPath)
        });

        for (const schemaInfo of schemas) {
            await schemaInfo.get()
        }

        return schemas;
    }
}

const loader = new JsonSchemaLoader()

export default loader;