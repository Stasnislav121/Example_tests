multi_create_schema = {
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
                "parcels"
            ],
            "additionalProperties": False,
            "properties": {
                "parcels": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
                        "type": "object",
                        "required": [
                            "result"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "result": {
                                "type": "object",
                                "required": [
                                    "clientReceiverId",
                                    "trackNumber",
                                    "sharedLink"
                                ],
                                "additionalProperties": False,
                                "properties": {
                                    "clientReceiverId": {
                                        "type": "string"
                                    },
                                    "trackNumber": {
                                        "type": "string"
                                    },
                                    "sharedLink": {
                                        "type": "string"
                                    }
                                }
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
