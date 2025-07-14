sms_code_verify_success_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "verificationToken": {
                    "type": "string"
                }
            },
            "required": ["verificationToken"]
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

sms_code_verify_err_schema = {
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
  "required": ["data", "success", "name", "message", "time"]
}
