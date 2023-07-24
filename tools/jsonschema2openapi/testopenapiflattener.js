import flattener from "./shemaflattener.js";

const openApiSpec = {
  swagger: "2.0",
  info: {
    title: "AllOf Property Example",
    version: "1.0.0",
  },
  paths: {
    "/data": {
      post: {
        summary: "Submit Data",
        consumes: ["application/json"],
        produces: ["application/json"],
        parameters: [],
        responses: {
          200: {
            description: "OK",
          },
        },
        requestBody: {
          required: true,
          schema: {
            allOf: [
              { $ref: "#/definitions/Person" },
              { $ref: "#/definitions/Employee" },
            ],
          },
        },
      },
    },
  },
  definitions: {
    Person: {
      type: "object",
      properties: {
        name: {
          type: "string",
        },
        age: {
          type: "integer",
        },
      },
    },
    Employee: {
      type: "object",
      properties: {
        employeeId: {
          type: "string",
        },
        department: {
          type: "string",
        },
      },
    },
  },
};

const openApiSpecWithAnyOf = {
  swagger: "2.0",
  info: {
    title: "AnyOf Property Example",
    version: "1.0.0",
  },
  paths: {
    "/data": {
      post: {
        summary: "Submit Data",
        consumes: ["application/json"],
        produces: ["application/json"],
        parameters: [],
        responses: {
          200: {
            description: "OK",
          },
        },
        requestBody: {
          required: true,
          schema: {
            anyOf: [
              { $ref: "#/definitions/Person" },
              { $ref: "#/definitions/Company" },
            ],
          },
        },
      },
    },
  },
  definitions: {
    Person: {
      type: "object",
      properties: {
        name: {
          type: "string",
        },
        age: {
          type: "integer",
        },
      },
    },
    Company: {
      type: "object",
      properties: {
        name: {
          type: "string",
        },
        registrationNumber: {
          type: "string",
        },
      },
    },
  },
};

// Test accessing the spec data
console.log(openApiSpec.info.title); // Output: "AllOf Property Example"
console.log(openApiSpec.paths["/data"].post.summary); // Output: "Submit Data"
console.log(openApiSpec.definitions.Person.properties.name.type); // Output: "string"
console.log(openApiSpec.definitions.Employee.properties.department.type); // Output: "string"

flattener.removeAnyOfOneOf(openApiSpecWithAnyOf);
console.log(JSON.stringify(openApiSpecWithAnyOf, null, 2));