parcel_insurance_limit_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "min": {
                    "type": "integer"
                },
                "max": {
                    "type": "integer"
                },
                "recommended": {
                    "type": "integer"
                }
            },
            "required": ["min", "max", "recommended"],
            "additionalProperties": False
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

parcel_insurance_limit_err_schema = {
    "type": "object",
    "required": [
        "data",
        "success",
        "name",
        "message",
        "time"
    ],
    "additionalProperties": False,
    "properties": {
        "data": {
            "type": "object",
            "required": [
                "errors"
            ],
            "additionalProperties": False,
            "properties": {
                "errors": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": [
                            "field",
                            "description"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "field": {
                                "type": "string"
                            },
                            "description": {
                                "type": "string"
                            }
                        }
                    },
                    "uniqueItems": True
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
    }
}
