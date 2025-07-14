parcel_calc_multi_schema = {
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
                "actualDeliveryInfo",
                "senderPrice",
                "receiverPrice",
                "includedServices"
            ],
            "additionalProperties": False,
            "properties": {
                "actualDeliveryInfo": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
                        "type": "object",
                        "required": [
                            "receiverId",
                            "deliveryInfo"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "receiverId": {
                                "type": "string"
                            },
                            "deliveryInfo": {
                                "type": "object",
                                "required": [
                                    "deliveryId",
                                    "deliveryInfo",
                                    "price"
                                ],
                                "additionalProperties": False,
                                "properties": {
                                    "deliveryId": {
                                        "type": "string"
                                    },
                                    "deliveryInfo": {
                                        "type": "string"
                                    },
                                    "price": {
                                        "type": "object",
                                        "required": [
                                            "value",
                                            "code"
                                        ],
                                        "additionalProperties": False,
                                        "properties": {
                                            "value": {
                                                "type": "number"
                                            },
                                            "code": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "uniqueItems": True
                },
                "senderPrice": {
                    "type": "object",
                    "required": [
                        "base",
                        "discount",
                        "total"
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "base": {
                            "type": "string"
                        },
                        "discount": {
                            "type": ["string", "null"]
                        },
                        "total": {
                            "type": "string"
                        }
                    }
                },
                "receiverPrice": {
                    "type": "null"
                },
                "includedServices": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
                        "type": "string"
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
