
## AutoRest Settings

```yaml
input-file: ingestionapi.json
python: true
clear-output-folder: true
output-folder: partnercenter/azext_partnercenter/vendored_sdks/v1
namespace: partnercenter
tag: v1
directive:
  - from: openapi-document
    where: '$.paths["*"]["*]'
    transform: |
      const capitalize = (str) => {
        const lower = str;
        return lower[0].toUpperCase() + lower.slice(1);
      }

      const methodPrefixMap = {
        get: "get",
        post: "create",
        put: "update",
        delete: "delete"
      }

      const verb = $path[2].toLowerCase();
      const urlPath = $path[1];
      const tag = $.tags[0];

      let operationId = verb;

      // append product if it's an action that's a sub-entity of product
      const isNestedEntityOfProduct = urlPath.startsWith('/products') && tag.indexOf('Product') == -1;

      if (isNestedEntityOfProduct) {
        operationId += 'Product';
      }

      //append tag, which is the current entity type
      operationId += capitalize(tag);

      //if the end of the URL is named something other than the tag, it's another nested entity
      let urlParts = urlPath.split('/');
      const lastUrlPart = urlParts[urlParts.length - 1];

      if (!lastUrlPart.endsWith('}') && lastUrlPart != tag.toLowerCase()) {
        operationId += capitalize(lastUrlPart);
      }

      let isCollectionReturned = $.description.toLowerCase().indexOf('collection') != -1 
                                || $.summary.toLowerCase().indexOf('collection') != -1 
                                || $.summary.toLowerCase().indexOf('a set of') != -1;

      if (isCollectionReturned) { // pluralize
        operationId += "s";
      }

      let idNames = urlPath.match(/(?<={)(.*?)(?=})/gi) ?? [];

      if (idNames.length > 1) {
        //get rid of productId if there's other Ids
        idNames = idNames.filter(name => name.indexOf('product') == -1); 
      }

      if (idNames.length > 0) {
        operationId += 'By' + capitalize(idNames[0].toString());
      }
    
      $["operationId"] = operationId;
```