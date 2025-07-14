packs_schema = {
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
                "boxes",
                "packages",
                "envelops"
            ],
            "additionalProperties": False,
            "properties": {
                "boxes": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
                        "type": "object",
                        "required": [
                            "id",
                            "title",
                            "image",
                            "",
                            "length",
                            "width",
                            "height",
                            "parcelExample"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "image": {
                                "type": "string"
                            },
                            "": {
                                "type": "boolean"
                            },
                            "length": {
                                "type": "integer"
                            },
                            "width": {
                                "type": "integer"
                            },
                            "height": {
                                "type": "integer"
                            },
                            "parcelExample": {
                                "type": "string"
                            }
                        }
                    },
                    "uniqueItems": True
                },
                "packages": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
                        "type": "object",
                        "required": [
                            "id",
                            "title",
                            "image",
                            "",
                            "length",
                            "width",
                            "height",
                            "parcelExample"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "image": {
                                "type": "string"
                            },
                            "": {
                                "type": "boolean"
                            },
                            "length": {
                                "type": "null"
                            },
                            "width": {
                                "type": "integer"
                            },
                            "height": {
                                "type": "integer"
                            },
                            "parcelExample": {
                                "type": "string"
                            }
                        }
                    },
                    "uniqueItems": True
                },
                "envelops": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
                        "type": "object",
                        "required": [
                            "id",
                            "title",
                            "image",
                            "",
                            "length",
                            "width",
                            "height",
                            "parcelExample"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "image": {
                                "type": "string"
                            },
                            "": {
                                "type": "boolean"
                            },
                            "length": {
                                "type": "null"
                            },
                            "width": {
                                "type": "integer"
                            },
                            "height": {
                                "type": "integer"
                            },
                            "parcelExample": {
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
