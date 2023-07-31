
import SchemaInfo from "./schemaInfo.js";

class JsonSchemaLoadOptions {
    outputPath = './.schemas';
    verbose = false;
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
            if (options.verbose) {
                console.log(`  - ${url}`)
            }
            return new SchemaInfo(url, options.schemasPath)
        });

        for (const schemaInfo of schemas) {
            await schemaInfo.get()
        }

        return schemas;
    }
}

const loader = new JsonSchemaLoader()

export default loader;