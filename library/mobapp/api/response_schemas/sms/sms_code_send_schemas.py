sms_code_send_success_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "timer": {
                    "type": "integer"
                }
            }
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

sms_code_send_err_param_schema = {
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

sms_code_send_err_registration_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": ["object", "null"]
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
