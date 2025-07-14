common_err_schema = {
  "type": "object",
  "properties": {
    "data": {
      "type": "null"
    },
    "success": {
      "type": "boolean",
      "const": False
    },
    "name": {
      "type": "string",
      "const": "Что-то пошло не так"
    },
    "message": {
      "type": "string",
      "const": "Попробуйте обновить страницу"
    },
    "time": {
      "type": "string"
    }
  },
  "required": [
    "data",
    "success",
    "name",
    "message",
    "time"
  ]
}

common_success_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": ["object", "null", "array"]
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
    "required": ["success", "time"],
    "additionalProperties": False
}

common_unprocessable_entity_err_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "errors": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "field": {
                                "type": "string"
                            },
                            "description": {
                                "type": "string"
                            }
                        },
                        "required": ["field", "description"]
                    }
                }
            },
            "required": ["errors"]
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
    "required": ["data", "success", "name", "message", "time"],
    "additionalProperties": False
}
