cities_schema = {
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
                "items",
                "total"
            ],
            "additionalProperties": False,
            "properties": {
                "items": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
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
                    "uniqueItems": True,
                    "minItems": 1
                },
                "total": {
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
            "type": "string"
        }
    }
}
