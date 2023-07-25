class ShemaFlattener {
  removeAnyOfOneOf(schema) {
    console.log(`Removing AnyOf and OneOf from schema: ${JSON.stringify(schema)}`);
    this.visit(schema);
  }

  visit(node) {
    if (!node || typeof node !== "object") {
      return;
    }

    if (Array.isArray(node)) {
      for (let i = 0; i < node.length; i++) {
        this.visit(node[i]);
      }
    } else {
      if (node.hasOwnProperty("oneOf")) {
        this.removeOneOf(node);
      } else if (node.hasOwnProperty("anyOf")) {
        this.removeAnyOf(node);
      } else {
        for (const key in node) {
          if (node.hasOwnProperty(key)) {
            this.visit(node[key]);
          }
        }
      }
    }
  }

  removeOneOf(node) {
    if (!Array.isArray(node.oneOf)) {
      return;
    }

    const properties = {};

    for (const item of node.oneOf) {
      for (const key in item) {
        if (item.hasOwnProperty(key) && key !== "title") {
          properties[key] = item[key];
        }
      }
    }

    delete node.oneOf;
    Object.assign(node, properties);
      shemaflattener  }

  removeAnyOf(node) {
    console.log(`Removing AnyOf from node: ${JSON.stringify(node)}`);
    if (!Array.isArray(node.anyOf)) {
      return;
    }

    const properties = {};

    for (const item of node.anyOf) {
      for (const key in item) {
        if (item.hasOwnProperty(key) && key !== "title") {
          properties[key] = item[key];
        }
      }
    }

    delete node.anyOf;
    console.log(`Assigning properties: ${JSON.stringify(properties)}`);
    Object.assign(node, properties);
  }
}

const flattener = new ShemaFlattener();
export default flattener;