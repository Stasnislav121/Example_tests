parcel_delivery_multi_schema = {
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
                "toDoor",
                "toOffice"
            ],
            "additionalProperties": False,
            "properties": {
                "toDoor": {
                    "type": "object",
                    "required": [
                        "price",
                        "estimate"
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "price": {
                            "type": "object",
                            "required": [
                                "delivery",
                                "deliveryServices",
                                "discount",
                                "finalPrice"
                            ],
                            "additionalProperties": False,
                            "properties": {
                                "delivery": {
                                    "type": "object",
                                    "required": [
                                        "id",
                                        "title",
                                        "description",
                                        "price"
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
                                },
                                "deliveryServices": {
                                    "type": "array",
                                    "additionalItems": False,
                                    "items": {},
                                    "uniqueItems": True
                                },
                                "discount": {
                                    "type": "object",
                                    "required": [
                                        "title",
                                        "price"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "title": {
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
                                                    "type": ["integer", "number"]
                                                },
                                                "code": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                },
                                "finalPrice": {
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
                        },
                        "estimate": {
                            "type": "string"
                        }
                    }
                },
                "toOffice": {
                    "type": "object",
                    "required": [
                        "price",
                        "estimate"
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "price": {
                            "type": "object",
                            "required": [
                                "delivery",
                                "deliveryServices",
                                "discount",
                                "finalPrice"
                            ],
                            "additionalProperties": False,
                            "properties": {
                                "delivery": {
                                    "type": "object",
                                    "required": [
                                        "id",
                                        "title",
                                        "description",
                                        "price"
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
                                },
                                "deliveryServices": {
                                    "type": "array",
                                    "additionalItems": False,
                                    "items": {},
                                    "uniqueItems": True
                                },
                                "discount": {
                                    "type": "object",
                                    "required": [
                                        "title",
                                        "price"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "title": {
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
                                                    "type": ["integer", "number"]
                                                },
                                                "code": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                },
                                "finalPrice": {
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
                        },
                        "estimate": {
                            "type": "string"
                        }
                    }
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
            "type": "string",
            "format": "date-time"
        }
    }
}
