user_info_schema = {
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
                "id",
                "status",
                "phone",
                "email",
                "sex",
                "birthday",
                "passportDataFilled",
                "name",
                "passportSeries",
                "passportNumber"
            ],
            "additionalProperties": False,
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
                    "type": "string"
                },
                "sex": {
                    "type": "string"
                },
                "birthday": {
                    "type": "string"
                },
                "passportDataFilled": {
                    "type": "boolean",
                    "enum": [True, False]
                },
                "name": {
                    "type": "string"
                },
                "passportSeries": {
                    "type": ["null", "string"]
                },
                "passportNumber": {
                    "type": ["null", "string"]
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

user_logout_schema = {
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
                "result"
            ],
            "additionalProperties": False,
            "properties": {
                "result": {
                    "type": "boolean"
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

user_logout_schema_err = {
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
            "type": "string"
        }
    }
}


user_chat_list_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "additionalInfo": {
                    "type": "string"
                },
                "links": {
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
            "required": ["additionalInfo", "links"]
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
