parcels_id_pip_not_owner_schema = {
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
                "type",
                "title",
                "trackNumber",
                "storeTrackNumber",
                "status",
                "statuses",
                "sender",
                "receiver",
                "deliveryDate",
                "storageDate",
                "deliveryInfo",
                "senderOffice",
                "senderAddress",
                "receiverOffice",
                "receiverAddress",
                "pack",
                "payer",
                "cost",
                "worth",
                "services",
                "paymentStatus",
                "paymentType",
                "comments",
                "review",
                "barcodeLink",
                "receiptLink",
                "promocode",
                "sharedLink",
                "barcodeDescription",
                "readyInOffice",
                "isFinished",
                "isRemovable",
                "retry",
                "products",
                "isOwner",
                "issueCode",
                "options",
                "flags",
                "isFavorite"
            ],
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "string"
                },
                "type": {
                    "type": "null"
                },
                "title": {
                    "type": "string"
                },
                "trackNumber": {
                    "type": "string"
                },
                "storeTrackNumber": {
                    "type": "string"
                },
                "status": {
                    "type": "object",
                    "required": [
                        "id",
                        "type",
                        "title",
                        "icon",
                        "date",
                        "color",
                        "location"
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "type": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "icon": {
                            "type": "string",
                            "format": "uri"
                        },
                        "date": {
                            "type": "string",
                            "format": "date-time"
                        },
                        "color": {
                            "type": "string"
                        },
                        "location": {
                            "type": "null"
                        }
                    }
                },
                "statuses": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
                        "type": "object",
                        "required": [
                            "id",
                            "type",
                            "title",
                            "icon",
                            "date",
                            "color",
                            "location"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "type": "integer"
                            },
                            "type": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "icon": {
                                "type": "string",
                                "format": "uri"
                            },
                            "date": {
                                "type": "string",
                                "format": "date-time"
                            },
                            "color": {
                                "type": "string"
                            },
                            "location": {
                                "type": "null"
                            }
                        }
                    },
                    "uniqueItems": True
                },
                "sender": {
                    "type": "null"
                },
                "receiver": {
                    "type": "null"
                },
                "deliveryDate": {
                    "type": "null"
                },
                "storageDate": {
                    "type": "null"
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
                                    "type": "integer"
                                },
                                "code": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                },
                "senderOffice": {
                    "type": "object",
                    "required": [
                        "id",
                        "address",
                        "favourite",
                        "schedule",
                        "current",
                        "latitude",
                        "longitude",
                        "availability",
                        "phone",
                        "services",
                        "howToGet",
                        "media",
                        "officeType",
                        "companyName",
                        "isAwaitingReview"
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "address": {
                            "type": "object",
                            "required": [
                                "postcode",
                                "country",
                                "city",
                                "address",
                                "latitude",
                                "longitude",
                                "countryCode",
                                "countryInfo"
                            ],
                            "additionalProperties": False,
                            "properties": {
                                "postcode": {
                                    "type": "string"
                                },
                                "country": {
                                    "type": "string"
                                },
                                "city": {
                                    "type": "object",
                                    "required": [
                                        "code",
                                        "title",
                                        "latitude",
                                        "longitude"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "code": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "latitude": {
                                            "type": "number"
                                        },
                                        "longitude": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "address": {
                                    "type": "string"
                                },
                                "latitude": {
                                    "type": "number"
                                },
                                "longitude": {
                                    "type": "number"
                                },
                                "countryCode": {
                                    "type": "string"
                                },
                                "countryInfo": {
                                    "type": "object",
                                    "required": [
                                        "countryName",
                                        "internationalPrefix",
                                        "domesticPrefix",
                                        "icon",
                                        "countryCode",
                                        "passportSeriesMask",
                                        "passportNumberMask",
                                        "innExists",
                                        "postalCodeMask",
                                        "isExport",
                                        "isoCode",
                                        "passportSeriesExists"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "countryName": {
                                            "type": "string"
                                        },
                                        "internationalPrefix": {
                                            "type": "string"
                                        },
                                        "domesticPrefix": {
                                            "type": "string"
                                        },
                                        "icon": {
                                            "type": "string",
                                            "format": "uri"
                                        },
                                        "countryCode": {
                                            "type": "string"
                                        },
                                        "passportSeriesMask": {
                                            "type": "string"
                                        },
                                        "passportNumberMask": {
                                            "type": "string"
                                        },
                                        "innExists": {
                                            "type": "boolean"
                                        },
                                        "postalCodeMask": {
                                            "type": "string"
                                        },
                                        "isExport": {
                                            "type": "boolean"
                                        },
                                        "isoCode": {
                                            "type": "string"
                                        },
                                        "passportSeriesExists": {
                                            "type": "boolean"
                                        }
                                    }
                                }
                            }
                        },
                        "favourite": {
                            "type": "boolean"
                        },
                        "schedule": {
                            "type": "object",
                            "required": [
                                "detailedSchedule",
                                "shortSchedule",
                                "description"
                            ],
                            "additionalProperties": False,
                            "properties": {
                                "detailedSchedule": {
                                    "type": "object",
                                    "required": [
                                        "sun",
                                        "mon",
                                        "tue",
                                        "wed",
                                        "thu",
                                        "fri",
                                        "sat"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "sun": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "mon": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "tue": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "wed": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "thu": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "fri": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "sat": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        }
                                    }
                                },
                                "shortSchedule": {
                                    "type": "object",
                                    "required": [
                                        "weekdays",
                                        "weekends"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "weekdays": {
                                            "type": "object",
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ],
                                            "additionalProperties": False,
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            }
                                        },
                                        "weekends": {
                                            "type": "object",
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ],
                                            "additionalProperties": False,
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                },
                                "description": {
                                    "type": "string"
                                }
                            }
                        },
                        "current": {
                            "type": "string"
                        },
                        "latitude": {
                            "type": "number"
                        },
                        "longitude": {
                            "type": "number"
                        },
                        "availability": {
                            "type": "array",
                            "additionalItems": False,
                            "items": {
                                "type": "string"
                            },
                            "uniqueItems": True
                        },
                        "phone": {
                            "type": "string"
                        },
                        "services": {
                            "type": "array",
                            "additionalItems": False,
                            "items": {
                                "type": "object",
                                "required": [
                                    "id",
                                    "title",
                                    "price"
                                ],
                                "additionalProperties": False,
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
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
                                                "type": "integer"
                                            },
                                            "code": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            },
                            "uniqueItems": True
                        },
                        "howToGet": {
                            "type": "string"
                        },
                        "media": {
                            "type": "array",
                            "additionalItems": False,
                            "items": {
                                "type": "object",
                                "required": [
                                    "id",
                                    "type",
                                    "link"
                                ],
                                "additionalProperties": False,
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "type": {
                                        "type": "string"
                                    },
                                    "link": {
                                        "type": "string",
                                        "format": "uri"
                                    }
                                }
                            },
                            "uniqueItems": True
                        },
                        "officeType": {
                            "type": "string"
                        },
                        "companyName": {
                            "type": "null"
                        },
                        "isAwaitingReview": {
                            "type": "boolean"
                        }
                    }
                },
                "senderAddress": {
                    "type": "null"
                },
                "receiverOffice": {
                    "type": "object",
                    "required": [
                        "id",
                        "address",
                        "favourite",
                        "schedule",
                        "current",
                        "latitude",
                        "longitude",
                        "availability",
                        "phone",
                        "services",
                        "howToGet",
                        "media",
                        "officeType",
                        "companyName",
                        "isAwaitingReview"
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "address": {
                            "type": "object",
                            "required": [
                                "postcode",
                                "country",
                                "city",
                                "address",
                                "latitude",
                                "longitude",
                                "countryCode",
                                "countryInfo"
                            ],
                            "additionalProperties": False,
                            "properties": {
                                "postcode": {
                                    "type": "string"
                                },
                                "country": {
                                    "type": "string"
                                },
                                "city": {
                                    "type": "object",
                                    "required": [
                                        "code",
                                        "title",
                                        "latitude",
                                        "longitude"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "code": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "latitude": {
                                            "type": "number"
                                        },
                                        "longitude": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "address": {
                                    "type": "string"
                                },
                                "latitude": {
                                    "type": "number"
                                },
                                "longitude": {
                                    "type": "number"
                                },
                                "countryCode": {
                                    "type": "string"
                                },
                                "countryInfo": {
                                    "type": "object",
                                    "required": [
                                        "countryName",
                                        "internationalPrefix",
                                        "domesticPrefix",
                                        "icon",
                                        "countryCode",
                                        "passportSeriesMask",
                                        "passportNumberMask",
                                        "innExists",
                                        "postalCodeMask",
                                        "isExport",
                                        "isoCode",
                                        "passportSeriesExists"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "countryName": {
                                            "type": "string"
                                        },
                                        "internationalPrefix": {
                                            "type": "string"
                                        },
                                        "domesticPrefix": {
                                            "type": "string"
                                        },
                                        "icon": {
                                            "type": "string",
                                            "format": "uri"
                                        },
                                        "countryCode": {
                                            "type": "string"
                                        },
                                        "passportSeriesMask": {
                                            "type": "string"
                                        },
                                        "passportNumberMask": {
                                            "type": "string"
                                        },
                                        "innExists": {
                                            "type": "boolean"
                                        },
                                        "postalCodeMask": {
                                            "type": "string"
                                        },
                                        "isExport": {
                                            "type": "boolean"
                                        },
                                        "isoCode": {
                                            "type": "string"
                                        },
                                        "passportSeriesExists": {
                                            "type": "boolean"
                                        }
                                    }
                                }
                            }
                        },
                        "favourite": {
                            "type": "boolean"
                        },
                        "schedule": {
                            "type": "object",
                            "required": [
                                "detailedSchedule",
                                "shortSchedule",
                                "description"
                            ],
                            "additionalProperties": False,
                            "properties": {
                                "detailedSchedule": {
                                    "type": "object",
                                    "required": [
                                        "sun",
                                        "mon",
                                        "tue",
                                        "wed",
                                        "thu",
                                        "fri",
                                        "sat"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "sun": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "mon": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "tue": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "wed": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "thu": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "fri": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "sat": {
                                            "type": "array",
                                            "additionalItems": False,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": False,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        }
                                    }
                                },
                                "shortSchedule": {
                                    "type": "object",
                                    "required": [
                                        "weekdays",
                                        "weekends"
                                    ],
                                    "additionalProperties": False,
                                    "properties": {
                                        "weekdays": {
                                            "type": "object",
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ],
                                            "additionalProperties": False,
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            }
                                        },
                                        "weekends": {
                                            "type": "object",
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ],
                                            "additionalProperties": False,
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                },
                                "description": {
                                    "type": "string"
                                }
                            }
                        },
                        "current": {
                            "type": "string"
                        },
                        "latitude": {
                            "type": "number"
                        },
                        "longitude": {
                            "type": "number"
                        },
                        "availability": {
                            "type": "array",
                            "additionalItems": False,
                            "items": {
                                "type": "string"
                            },
                            "uniqueItems": True
                        },
                        "phone": {
                            "type": "string"
                        },
                        "services": {
                            "type": "array",
                            "additionalItems": False,
                            "items": {
                                "type": "object",
                                "required": [
                                    "id",
                                    "title",
                                    "price"
                                ],
                                "additionalProperties": False,
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
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
                                                "type": "integer"
                                            },
                                            "code": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            },
                            "uniqueItems": True
                        },
                        "howToGet": {
                            "type": "string"
                        },
                        "media": {
                            "type": "array",
                            "additionalItems": False,
                            "items": {
                                "type": "object",
                                "required": [
                                    "id",
                                    "type",
                                    "link"
                                ],
                                "additionalProperties": False,
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "type": {
                                        "type": "string"
                                    },
                                    "link": {
                                        "type": "string",
                                        "format": "uri"
                                    }
                                }
                            },
                            "uniqueItems": True
                        },
                        "officeType": {
                            "type": "string"
                        },
                        "companyName": {
                            "type": "null"
                        },
                        "isAwaitingReview": {
                            "type": "boolean"
                        }
                    }
                },
                "receiverAddress": {
                    "type": "null"
                },
                "pack": {
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
                            "type": "string",
                            "format": "uri"
                        },
                        "isCustom": {
                            "type": "boolean"
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
                "payer": {
                    "type": "string"
                },
                "cost": {
                    "type": "null"
                },
                "worth": {
                    "type": "null"
                },
                "services": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
                        "type": "object",
                        "required": [
                            "id",
                            "title",
                            "price"
                        ],
                        "additionalProperties": False,
                        "properties": {
                            "id": {
                                "type": "integer"
                            },
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
                                        "type": "integer"
                                    },
                                    "code": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    },
                    "uniqueItems": True
                },
                "paymentStatus": {
                    "type": "string"
                },
                "paymentType": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {
                        "type": "string"
                    },
                    "uniqueItems": True
                },
                "comments": {
                    "type": "string"
                },
                "review": {
                    "type": "null"
                },
                "barcodeLink": {
                    "type": "null"
                },
                "receiptLink": {
                    "type": "null"
                },
                "promocode": {
                    "type": "string"
                },
                "sharedLink": {
                    "type": "string",
                    "format": "uri"
                },
                "barcodeDescription": {
                    "type": "string"
                },
                "readyInOffice": {
                    "type": "boolean"
                },
                "isFinished": {
                    "type": "boolean"
                },
                "isRemovable": {
                    "type": "boolean"
                },
                "retry": {
                    "type": "boolean"
                },
                "products": {
                    "type": "array",
                    "additionalItems": False,
                    "items": {},
                    "uniqueItems": True
                },
                "isOwner": {
                    "type": "boolean"
                },
                "issueCode": {
                    "type": "null"
                },
                "options": {
                    "type": "integer"
                },
                "flags": {
                    "type": "object",
                    "required": [
                        "officeChange",
                        "deliveryChange",
                        "storageDateTimeChange",
                        "changeAddress",
                        "receiverDataChange",
                        "shouldChangeOffice",
                        "changeTime"
                    ],
                    "additionalProperties": False,
                    "properties": {
                        "officeChange": {
                            "type": "boolean"
                        },
                        "deliveryChange": {
                            "type": "boolean"
                        },
                        "storageDateTimeChange": {
                            "type": "boolean"
                        },
                        "changeAddress": {
                            "type": "boolean"
                        },
                        "receiverDataChange": {
                            "type": "boolean"
                        },
                        "shouldChangeOffice": {
                            "type": "boolean"
                        },
                        "changeTime": {
                            "type": "boolean"
                        }
                    }
                },
                "isFavorite": {
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
            "type": "string",
            "format": "date-time"
        }
    }
}

parcels_id_pip_owner_schema = {
    "type": "object",
    "required": [
        "data",
        "success",
        "name",
        "message",
        "time"
    ],
    "additionalProperties": True,
    "properties": {
        "data": {
            "type": "object",
            "required": [
                "id",
                "type",
                "title",
                "trackNumber",
                "storeTrackNumber",
                "status",
                "statuses",
                "sender",
                "receiver",
                "deliveryDate",
                "storageDate",
                "deliveryInfo",
                "senderOffice",
                "senderAddress",
                "receiverOffice",
                "receiverAddress",
                "pack",
                "payer",
                "cost",
                "worth",
                "services",
                "paymentStatus",
                "paymentType",
                "comments",
                "review",
                "barcodeLink",
                "receiptLink",
                "promocode",
                "sharedLink",
                "barcodeDescription",
                "readyInOffice",
                "isFinished",
                "isRemovable",
                "retry",
                "products",
                "isOwner",
                "issueCode",
                "options",
                "flags",
                "isFavorite"
            ],
            "additionalProperties": True,
            "properties": {
                "id": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                },
                "trackNumber": {
                    "type": "string"
                },
                "storeTrackNumber": {
                    "type": "string"
                },
                "status": {
                    "type": "object",
                    "required": [
                        "id",
                        "type",
                        "title",
                        "icon",
                        "date",
                        "color",
                        "location"
                    ],
                    "additionalProperties": True,
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "type": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "icon": {
                            "type": "string",
                            "format": "uri"
                        },
                        "date": {
                            "type": "string",
                            "format": "date-time"
                        },
                        "color": {
                            "type": "string"
                        },
                        "location": {
                            "type": ["object", "null"],
                            "required": [
                                "country",
                                "location"
                            ],
                            "additionalProperties": False,
                            "properties": {
                                "country": {
                                    "type": "string"
                                },
                                "location": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                },
                "statuses": {
                    "type": "array",
                    "additionalItems": True,
                    "items": {
                        "type": "object",
                        "required": [
                            "id",
                            "type",
                            "title",
                            "icon",
                            "date",
                            "color",
                            "location"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "id": {
                                "type": "integer"
                            },
                            "type": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "icon": {
                                "type": "string",
                                "format": "uri"
                            },
                            "date": {
                                "type": "string",
                                "format": "date-time"
                            },
                            "color": {
                                "type": "string"
                            },
                            "location": {
                                "type": ["object", "null"],
                                "required": [
                                    "country",
                                    "location"
                                ],
                                "additionalProperties": False,
                                "properties": {
                                    "country": {
                                        "type": "string"
                                    },
                                    "location": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    },
                    "uniqueItems": True
                },
                "sender": {
                    "type": "object",
                    "required": [
                        "fullName",
                        "phone",
                        "email"
                    ],
                    "additionalProperties": True,
                    "properties": {
                        "fullName": {
                            "type": "string"
                        },
                        "phone": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        }
                    }
                },
                "receiver": {
                    "type": "object",
                    "required": [
                        "fullName",
                        "phone",
                        "email"
                    ],
                    "additionalProperties": True,
                    "properties": {
                        "fullName": {
                            "type": "string"
                        },
                        "phone": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        }
                    }
                },
                "deliveryDate": {
                    "type": "null"
                },
                "storageDate": {
                    "type": "null"
                },
                "deliveryInfo": {
                    "type": "object",
                    "required": [
                        "deliveryId",
                        "deliveryInfo",
                        "price"
                    ],
                    "additionalProperties": True,
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
                            "additionalProperties": True,
                            "properties": {
                                "value": {
                                    "type": "integer"
                                },
                                "code": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                },
                "senderOffice": {
                    "type": "object",
                    "required": [
                        "id",
                        "address",
                        "favourite",
                        "schedule",
                        "current",
                        "latitude",
                        "longitude",
                        "availability",
                        "phone",
                        "services",
                        "howToGet",
                        "media",
                        "officeType",
                        "companyName",
                        "isAwaitingReview"
                    ],
                    "additionalProperties": True,
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "address": {
                            "type": "object",
                            "required": [
                                "postcode",
                                "country",
                                "city",
                                "address",
                                "latitude",
                                "longitude",
                                "countryCode",
                                "countryInfo"
                            ],
                            "additionalProperties": True,
                            "properties": {
                                "postcode": {
                                    "type": "string"
                                },
                                "country": {
                                    "type": "string"
                                },
                                "city": {
                                    "type": "object",
                                    "required": [
                                        "code",
                                        "title",
                                        "latitude",
                                        "longitude"
                                    ],
                                    "additionalProperties": True,
                                    "properties": {
                                        "code": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "latitude": {
                                            "type": "number"
                                        },
                                        "longitude": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "address": {
                                    "type": "string"
                                },
                                "latitude": {
                                    "type": "number"
                                },
                                "longitude": {
                                    "type": "number"
                                },
                                "countryCode": {
                                    "type": "string"
                                },
                                "countryInfo": {
                                    "type": "object",
                                    "required": [
                                        "countryName",
                                        "internationalPrefix",
                                        "domesticPrefix",
                                        "icon",
                                        "countryCode",
                                        "passportSeriesMask",
                                        "passportNumberMask",
                                        "innExists",
                                        "postalCodeMask",
                                        "isExport",
                                        "isoCode",
                                        "passportSeriesExists"
                                    ],
                                    "additionalProperties": True,
                                    "properties": {
                                        "countryName": {
                                            "type": "string"
                                        },
                                        "internationalPrefix": {
                                            "type": "string"
                                        },
                                        "domesticPrefix": {
                                            "type": "string"
                                        },
                                        "icon": {
                                            "type": "string",
                                            "format": "uri"
                                        },
                                        "countryCode": {
                                            "type": "string"
                                        },
                                        "passportSeriesMask": {
                                            "type": "string"
                                        },
                                        "passportNumberMask": {
                                            "type": "string"
                                        },
                                        "innExists": {
                                            "type": "boolean"
                                        },
                                        "postalCodeMask": {
                                            "type": "string"
                                        },
                                        "isExport": {
                                            "type": "boolean"
                                        },
                                        "isoCode": {
                                            "type": "string"
                                        },
                                        "passportSeriesExists": {
                                            "type": "boolean"
                                        }
                                    }
                                }
                            }
                        },
                        "favourite": {
                            "type": "boolean"
                        },
                        "schedule": {
                            "type": "object",
                            "required": [
                                "detailedSchedule",
                                "shortSchedule",
                                "description"
                            ],
                            "additionalProperties": True,
                            "properties": {
                                "detailedSchedule": {
                                    "type": "object",
                                    "required": [
                                        "sun",
                                        "mon",
                                        "tue",
                                        "wed",
                                        "thu",
                                        "fri",
                                        "sat"
                                    ],
                                    "additionalProperties": True,
                                    "properties": {
                                        "sun": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "mon": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "tue": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "wed": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "thu": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "fri": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "sat": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        }
                                    }
                                },
                                "shortSchedule": {
                                    "type": "object",
                                    "required": [
                                        "weekdays",
                                        "weekends"
                                    ],
                                    "additionalProperties": True,
                                    "properties": {
                                        "weekdays": {
                                            "type": "object",
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ],
                                            "additionalProperties": True,
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            }
                                        },
                                        "weekends": {
                                            "type": "object",
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ],
                                            "additionalProperties": True,
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                },
                                "description": {
                                    "type": "string"
                                }
                            }
                        },
                        "current": {
                            "type": "string"
                        },
                        "latitude": {
                            "type": "number"
                        },
                        "longitude": {
                            "type": "number"
                        },
                        "availability": {
                            "type": "array",
                            "additionalItems": True,
                            "items": {
                                "type": "string"
                            },
                            "uniqueItems": True
                        },
                        "phone": {
                            "type": "string"
                        },
                        "services": {
                            "type": "array",
                            "additionalItems": True,
                            "items": {
                                "type": "object",
                                "required": [
                                    "id",
                                    "title",
                                    "price"
                                ],
                                "additionalProperties": True,
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "title": {
                                        "type": "string"
                                    },
                                    "price": {
                                        "type": "object",
                                        "required": [
                                            "value",
                                            "code"
                                        ],
                                        "additionalProperties": True,
                                        "properties": {
                                            "value": {
                                                "type": "integer"
                                            },
                                            "code": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            },
                            "uniqueItems": True
                        },
                        "howToGet": {
                            "type": "string"
                        },
                        "media": {
                            "type": "array",
                            "additionalItems": True,
                            "items": {},
                            "uniqueItems": True
                        },
                        "officeType": {
                            "type": "string"
                        },
                        "companyName": {
                            "type": "null"
                        },
                        "isAwaitingReview": {
                            "type": "boolean"
                        }
                    }
                },
                "senderAddress": {
                    "type": "null"
                },
                "receiverOffice": {
                    "type": "object",
                    "required": [
                        "id",
                        "address",
                        "favourite",
                        "schedule",
                        "current",
                        "latitude",
                        "longitude",
                        "availability",
                        "phone",
                        "services",
                        "howToGet",
                        "media",
                        "officeType",
                        "companyName",
                        "isAwaitingReview"
                    ],
                    "additionalProperties": True,
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "address": {
                            "type": "object",
                            "required": [
                                "postcode",
                                "country",
                                "city",
                                "address",
                                "latitude",
                                "longitude",
                                "countryCode",
                                "countryInfo"
                            ],
                            "additionalProperties": True,
                            "properties": {
                                "postcode": {
                                    "type": "string"
                                },
                                "country": {
                                    "type": "string"
                                },
                                "city": {
                                    "type": "object",
                                    "required": [
                                        "code",
                                        "title",
                                        "latitude",
                                        "longitude"
                                    ],
                                    "additionalProperties": True,
                                    "properties": {
                                        "code": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "latitude": {
                                            "type": "number"
                                        },
                                        "longitude": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "address": {
                                    "type": "string"
                                },
                                "latitude": {
                                    "type": "number"
                                },
                                "longitude": {
                                    "type": "number"
                                },
                                "countryCode": {
                                    "type": "string"
                                },
                                "countryInfo": {
                                    "type": "object",
                                    "required": [
                                        "countryName",
                                        "internationalPrefix",
                                        "domesticPrefix",
                                        "icon",
                                        "countryCode",
                                        "passportSeriesMask",
                                        "passportNumberMask",
                                        "innExists",
                                        "postalCodeMask",
                                        "isExport",
                                        "isoCode",
                                        "passportSeriesExists"
                                    ],
                                    "additionalProperties": True,
                                    "properties": {
                                        "countryName": {
                                            "type": "string"
                                        },
                                        "internationalPrefix": {
                                            "type": "string"
                                        },
                                        "domesticPrefix": {
                                            "type": "string"
                                        },
                                        "icon": {
                                            "type": "string",
                                            "format": "uri"
                                        },
                                        "countryCode": {
                                            "type": "string"
                                        },
                                        "passportSeriesMask": {
                                            "type": "string"
                                        },
                                        "passportNumberMask": {
                                            "type": "string"
                                        },
                                        "innExists": {
                                            "type": "boolean"
                                        },
                                        "postalCodeMask": {
                                            "type": "string"
                                        },
                                        "isExport": {
                                            "type": "boolean"
                                        },
                                        "isoCode": {
                                            "type": "string"
                                        },
                                        "passportSeriesExists": {
                                            "type": "boolean"
                                        }
                                    }
                                }
                            }
                        },
                        "favourite": {
                            "type": "boolean"
                        },
                        "schedule": {
                            "type": "object",
                            "required": [
                                "detailedSchedule",
                                "shortSchedule",
                                "description"
                            ],
                            "additionalProperties": True,
                            "properties": {
                                "detailedSchedule": {
                                    "type": "object",
                                    "required": [
                                        "sun",
                                        "mon",
                                        "tue",
                                        "wed",
                                        "thu",
                                        "fri",
                                        "sat"
                                    ],
                                    "additionalProperties": True,
                                    "properties": {
                                        "sun": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {},
                                            "uniqueItems": True
                                        },
                                        "mon": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "tue": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "wed": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "thu": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "fri": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        },
                                        "sat": {
                                            "type": "array",
                                            "additionalItems": True,
                                            "items": {
                                                "type": "object",
                                                "required": [
                                                    "start",
                                                    "end"
                                                ],
                                                "additionalProperties": True,
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                }
                                            },
                                            "uniqueItems": True
                                        }
                                    }
                                },
                                "shortSchedule": {
                                    "type": "object",
                                    "required": [
                                        "weekdays",
                                        "weekends"
                                    ],
                                    "additionalProperties": True,
                                    "properties": {
                                        "weekdays": {
                                            "type": "object",
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ],
                                            "additionalProperties": True,
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            }
                                        },
                                        "weekends": {
                                            "type": "object",
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ],
                                            "additionalProperties": True,
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                },
                                "description": {
                                    "type": "string"
                                }
                            }
                        },
                        "current": {
                            "type": "string"
                        },
                        "latitude": {
                            "type": "number"
                        },
                        "longitude": {
                            "type": "number"
                        },
                        "availability": {
                            "type": "array",
                            "additionalItems": True,
                            "items": {
                                "type": "string"
                            },
                            "uniqueItems": True
                        },
                        "phone": {
                            "type": "string"
                        },
                        "services": {
                            "type": "array",
                            "additionalItems": True,
                            "items": {
                                "type": "object",
                                "required": [
                                    "id",
                                    "title",
                                    "price"
                                ],
                                "additionalProperties": True,
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "title": {
                                        "type": "string"
                                    },
                                    "price": {
                                        "type": "object",
                                        "required": [
                                            "value",
                                            "code"
                                        ],
                                        "additionalProperties": True,
                                        "properties": {
                                            "value": {
                                                "type": "integer"
                                            },
                                            "code": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            },
                            "uniqueItems": True
                        },
                        "howToGet": {
                            "type": "string"
                        },
                        "media": {
                            "type": "array",
                            "additionalItems": True,
                            "items": {},
                            "uniqueItems": True
                        },
                        "officeType": {
                            "type": "string"
                        },
                        "companyName": {
                            "type": "null"
                        },
                        "isAwaitingReview": {
                            "type": "boolean"
                        }
                    }
                },
                "receiverAddress": {
                    "type": "null"
                },
                "pack": {
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
                    "additionalProperties": True,
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "image": {
                            "type": "string",
                            "format": "uri"
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
                "payer": {
                    "type": "string"
                },
                "cost": {
                    "type": "object",
                    "required": [
                        "services",
                        "delivery",
                        "discount",
                        "total"
                    ],
                    "additionalProperties": True,
                    "properties": {
                        "services": {
                            "type": "array",
                            "additionalItems": True,
                            "items": {},
                            "uniqueItems": True
                        },
                        "delivery": {
                            "type": "object",
                            "required": [
                                "value",
                                "code"
                            ],
                            "additionalProperties": True,
                            "properties": {
                                "value": {
                                    "type": "integer"
                                },
                                "code": {
                                    "type": "string"
                                }
                            }
                        },
                        "discount": {
                            "type": "null"
                        },
                        "total": {
                            "type": "object",
                            "required": [
                                "value",
                                "code"
                            ],
                            "additionalProperties": True,
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
                "worth": {
                    "type": "null"
                },
                "services": {
                    "type": "array",
                    "additionalItems": True,
                    "items": {
                        "type": "object",
                        "required": [
                            "id",
                            "title",
                            "price"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "id": {
                                "type": "integer"
                            },
                            "title": {
                                "type": "string"
                            },
                            "price": {
                                "type": "object",
                                "required": [
                                    "value",
                                    "code"
                                ],
                                "additionalProperties": True,
                                "properties": {
                                    "value": {
                                        "type": "integer"
                                    },
                                    "code": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    },
                    "uniqueItems": True
                },
                "paymentStatus": {
                    "type": "string"
                },
                "paymentType": {
                    "type": "array",
                    "additionalItems": True,
                    "items": {
                        "type": "string"
                    },
                    "uniqueItems": True
                },
                "comments": {
                    "type": "string"
                },
                "review": {
                    "type": "null"
                },
                "barcodeLink": {
                    "type": "string"
                },
                "receiptLink": {
                    "type": "null"
                },
                "promocode": {
                    "type": "string"
                },
                "sharedLink": {
                    "type": "string",
                    "format": "uri"
                },
                "barcodeDescription": {
                    "type": "string"
                },
                "readyInOffice": {
                    "type": "boolean"
                },
                "isFinished": {
                    "type": "boolean"
                },
                "isRemovable": {
                    "type": "boolean"
                },
                "retry": {
                    "type": "boolean"
                },
                "products": {
                    "type": "array",
                    "additionalItems": True,
                    "items": {},
                    "uniqueItems": True
                },
                "isOwner": {
                    "type": "boolean"
                },
                "issueCode": {
                    "type": "null"
                },
                "options": {
                    "type": "integer"
                },
                "flags": {
                    "type": "object",
                    "required": [
                        "officeChange",
                        "deliveryChange",
                        "storageDateTimeChange",
                        "changeAddress",
                        "receiverDataChange",
                        "shouldChangeOffice",
                        "changeTime"
                    ],
                    "additionalProperties": True,
                    "properties": {
                        "officeChange": {
                            "type": "boolean"
                        },
                        "deliveryChange": {
                            "type": "boolean"
                        },
                        "storageDateTimeChange": {
                            "type": "boolean"
                        },
                        "changeAddress": {
                            "type": "boolean"
                        },
                        "receiverDataChange": {
                            "type": "boolean"
                        },
                        "shouldChangeOffice": {
                            "type": "boolean"
                        },
                        "changeTime": {
                            "type": "boolean"
                        }
                    }
                },
                "isFavorite": {
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
            "type": "string",
            "format": "date-time"
        }
    }
}
