
auth_registration_success_schema = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "authToken": {
          "type": "string"
        },
        "refreshToken": {
          "type": "string"
        },
        "user": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "status": {
              "type": "string"
            },
            "phone": {
              "type": "string"
            },
            "email": {
              "type": "string",
              "format": "email"
            },
            "sex": {
              "type": "string"
            },
            "birthday": {
              "type": "string",
            },
            "passportDataFilled": {
              "type": "boolean"
            },
            "name": {
              "type": "string"
            },
            "passportSeries": {
              "type": ["string", "null"]
            },
            "passportNumber": {
              "type": ["string", "null"]
            }
          },
          "required": ["id", "status", "phone", "email", "sex", "birthday", "name", "passportDataFilled",
                       "passportSeries", "passportNumber"]
        }
      },
      "required": ["authToken", "refreshToken", "user"]
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
