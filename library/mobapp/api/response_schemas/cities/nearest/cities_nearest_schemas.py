cities_nearest_schema = {
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
                "code",
                "title",
                "latitude",
                "longitude"
            ],
            "additionalProperties": False,
            "properties": {
                "code": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                },
                "latitude": {
                    "type": "number"
                },
                "longitude": {
                    "type": "number"
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
            "type": "string"
        }
    }
}


cities_nearest_schema_err = {
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
                    "additionalItems": False,
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
            "type": "string"
        }
    }
}
