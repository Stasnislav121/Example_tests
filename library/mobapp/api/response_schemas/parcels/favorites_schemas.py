parcel_id_favorites_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "null"
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
