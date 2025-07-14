custom_package_create_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "boxId": {
                    "type": "integer"
                },
                "height": {
                    "type": "integer"
                },
                "width": {
                    "type": "integer"
                },
                "length": {
                    "type": "integer"
                },
                "title": {
                    "type": "string"
                },
                "cost": {
                    "type": "integer"
                },
                "description": {
                    "type": ["string", "null"]
                },
                "imageId": {
                    "type": ["integer", "null"]
                },
                "imageLink": {
                    "type": ["string", "null"],
                    "format": "uri"
                }
            },
            "required": ["boxId", "height", "width", "length", "title", "cost"]
        },
        "success": {
            "type": "boolean"
        },
        "name": {
            "type": "string"
        },
        "message": {
            "type": "string"
        },
        "time": {
            "type": "string",
            "format": "date-time"
        }
    },
    "required": ["data", "success", "time"]
}

custom_package_file_schema = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "imageId": {
          "type": "integer"
        },
        "imageLink": {
          "type": "string",
          "format": "uri"
        }
      },
      "required": ["imageId", "imageLink"]
    },
    "success": {
      "type": "boolean"
    },
    "name": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "time": {
      "type": "string",
      "format": "date-time"
    }
  },
  "required": ["data", "success", "time"]
}
