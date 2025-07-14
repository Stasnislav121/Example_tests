faq_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "link": {
                    "type": "string",
                    "format": "uri"
                }
            },
            "required": ["link"]
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
