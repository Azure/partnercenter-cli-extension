
import https from 'https'
import path from 'path'
import fs from 'fs'

function readFile(file) {
    const absolutePath = path.resolve(file);
    const json = fs.readFileSync(absolutePath, { encoding: 'utf-8' });
    return json
}

function toPascalCase(str) {
    return str.replace(/(\w)(\w*)/g, function (g0, g1, g2) { return g1.toUpperCase() + g2.toLowerCase(); });
}


export class SchemaUrl {
    static baseUrl = "https://product-ingestion.azureedge.net/schema/"
    value;
    parts;

    constructor(url) {
        this.value = url
        this.parts = this.getParts(url)
    }

    getParts(url) {
        return url.replace(SchemaUrl.baseUrl, "").split("/")
    }

    name() {
        return this.parts[0]
    }

    version() {
        return this.parts[1]
    }

}

/**
 * JSON Schema info acting as a descriptor to consume conversion
 */
class SchemaInfo {
    url;
    json;
    downloadPath;

    constructor(url, downloadPath) {
        this.url = new SchemaUrl(url)
        this.downloadPath = downloadPath
    }

    fileName() {
        return this.url.name() + "_" + this.url.version() + ".json";
    }

    filePath() {
        return this.downloadPath + '/' + this.fileName();
    }

    name() {
        return this.url.name();
    }

    componentName() {
        return toPascalCase(this.name()).replace(/-/g, '');
    }

    async get() {
        //console.log(`fetching ${this.url.name()}`)

        let promise = new Promise((resolve, reject) => {
            https.get(this.url.value, res => {
                res.on('end', () => {
                    setTimeout(() => {
                        const fileContents = readFile(this.filePath())
                        resolve(JSON.parse(fileContents));
                    }, 100);
                }).pipe(fs.createWriteStream(this.filePath()), { end: true })
            })
        });
        const value = await promise;
        this.json = value;
    }
}

export default SchemaInfo