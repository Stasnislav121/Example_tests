feedback_topic_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "alias": {
                                "type": "string"
                            }
                        },
                        "required": ["id", "title", "alias"]
                    }
                }
            },
            "required": ["items"]
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
