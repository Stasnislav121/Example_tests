stocks_schema = {
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
                            "id",
                            "title",
                            "description",
                            "image"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "description": {
                                "type": "string"
                            },
                            "image": {
                                "type": "string"
                            }
                        }
                    },
                    "uniqueItems": True
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

stock_schema = {
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
                "title",
                "description",
                "image",
                "expirationDate",
                "promocode",
                "discount",
                "imageText"
            ],
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "image": {
                    "type": "string"
                },
                "expirationDate": {
                    "type": "string"
                },
                "promocode": {
                    "type": "string"
                },
                "discount": {
                    "type": ["null", "string"]
                },
                "imageText": {
                    "type": "string"
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

stock_schema_err = {
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

stock_for_bottom_sheet_schema = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "format": "uuid"
        },
        "image": {
          "type": "string",
          "format": "uri"
        },
        "showIntervalDays": {
          "type": "integer"
        },
        "title": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "button": {
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
      },
      "required": ["id", "image", "showIntervalDays", "title", "description", "button"]
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
