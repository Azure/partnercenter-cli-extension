export class OpenApiPath {
  constructor(durableIdRef, schemaRef) {
    this.path = "/resource-tree/product/{durableId}";
    this.get = {
      operationId: "GetProduct",
      tags: ["Offer"],
      parameters: [
        {
          name: "durableId",
          in: "path",
          required: true,
          schema: {
            type: "string",
          },
        },
      ],
      responses: {
        "200": {
          description: "successful operation",
          content: {
            "application/json": {
              schema: {
                type: "array",
                items: {
                  $ref: schemaRef, // e.g., "./definitions.json#/components/schemas/Product"
                },
              },
            },
          },
        },
        "400": {
          description: "Invalid status value",
        },
      },
    };
  }
}

