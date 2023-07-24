

import Converter from 'api-spec-converter';

export default class OpenApi3toSwaggerConverter {
    async convert(spec) {
        return await Converter.convert({
            from: 'openapi_3',
            to: 'swagger_2',
            source: spec,
        });
    }
}

exportconvertToSwagger2 = async function(spec) {
    const converter = new OpenApi3toSwaggerConverter();
    return await converter.convert(spec);
}