page_documents_schema = {
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
                            "title": {
                                "type": "string"
                            },
                            "link": {
                                "type": "string",
                                "format": "uri"
                            }
                        },
                        "required": ["title", "link"]
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
