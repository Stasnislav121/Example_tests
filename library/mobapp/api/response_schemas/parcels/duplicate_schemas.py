parcel_duplicate_schema = {
    "type": "object",
    "required": [
        "data",
        "success",
        "name",
        "message",
        "time"
    ],
    "properties": {
        "data": {
            "type": "object",
            "required": [
                "senderInfo",
                "receiverInfo",
                "parcelInfo"
            ],
            "properties": {
                "senderInfo": {
                    "type": "object",
                    "required": [
                        "city",
                        "office",
                        "address",
                        "personalUserInfo"
                    ],
                    "properties": {
                        "city": {
                            "type": "object",
                            "required": [
                                "code",
                                "title",
                                "latitude",
                                "longitude"
                            ],
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
                        "office": {
                            "type": "object",
                            "required": [
                                "id",
                                "address",
                                "favourite",
                                "schedule",
                                "current",
                                "latitude",
                                "longitude",
                                "availability"
                            ],
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
                                                    "type": "string"
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
                                    "properties": {
                                        "detailedSchedule": {
                                            "type": "object",
                                            "properties": {
                                                "sun": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                            "properties": {
                                                "weekdays": {
                                                    "type": "object",
                                                    "required": [
                                                        "workingHours",
                                                        "break"
                                                    ],
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
                                    "items": {
                                        "type": "string"
                                    },
                                    "uniqueItems": True
                                }
                            }
                        },
                        "address": {
                            "type": "null"
                        },
                        "personalUserInfo": {
                            "type": "object",
                            "required": [
                                "name",
                                "phone",
                                "email",
                                "passport"
                            ],
                            "properties": {
                                "name": {
                                    "type": "string"
                                },
                                "phone": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "passport": {
                                    "type": "object",
                                    "required": [
                                        "seria",
                                        "number"
                                    ],
                                    "properties": {
                                        "seria": {
                                            "type": "string"
                                        },
                                        "number": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "receiverInfo": {
                    "type": "object",
                    "required": [
                        "city",
                        "office",
                        "address",
                        "personalUserInfo"
                    ],
                    "properties": {
                        "city": {
                            "type": "object",
                            "required": [
                                "code",
                                "title",
                                "latitude",
                                "longitude"
                            ],
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
                        "office": {
                            "type": "object",
                            "required": [
                                "id",
                                "address",
                                "favourite",
                                "schedule",
                                "current",
                                "latitude",
                                "longitude",
                                "availability"
                            ],
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
                                                    "type": "string"
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
                                            "properties": {
                                                "sun": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                                    "items": {
                                                        "type": "object",
                                                        "required": [
                                                            "start",
                                                            "end"
                                                        ],
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
                                            "properties": {
                                                "weekdays": {
                                                    "type": "object",
                                                    "required": [
                                                        "workingHours",
                                                        "break"
                                                    ],
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
                                    "items": {
                                        "type": "string"
                                    },
                                    "uniqueItems": True
                                }
                            }
                        },
                        "address": {
                            "type": "null"
                        },
                        "personalUserInfo": {
                            "type": "object",
                            "required": [
                                "name",
                                "phone",
                                "email",
                                "passport"
                            ],
                            "properties": {
                                "name": {
                                    "type": "string"
                                },
                                "phone": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "passport": {
                                    "type": "object",
                                    "required": [
                                        "seria",
                                        "number"
                                    ],
                                    "properties": {
                                        "seria": {
                                            "type": "string"
                                        },
                                        "number": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "parcelInfo": {
                    "type": "object",
                    "required": [
                        "parcelName",
                        "deliveryId",
                        "promo",
                        "declaredPrice",
                        "package",
                        "paidByReceiver",
                        "additionalServices"
                    ],
                    "properties": {
                        "parcelName": {
                            "type": "string"
                        },
                        "deliveryId": {
                            "type": "string"
                        },
                        "promo": {
                            "type": "string"
                        },
                        "declaredPrice": {
                            "type": "object",
                            "required": [
                                "value",
                                "code"
                            ],
                            "properties": {
                                "value": {
                                    "type": "integer"
                                },
                                "code": {
                                    "type": "string"
                                }
                            }
                        },
                        "package": {
                            "type": "object",
                            "required": [
                                "id",
                                "title",
                                "image",
                                "",
                                "length",
                                "width",
                                "height",
                                "parcelExample",
                                "isCustom"
                            ],
                            "properties": {
                                "id": {
                                    "type": ["string", "null"]
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
                                },
                                "isCustom": {
                                    "type": "boolean"
                                }
                            }
                        },
                        "paidByReceiver": {
                            "type": "boolean"
                        },
                        "additionalServices": {
                            "type": "array",
                            "items": {},
                            "uniqueItems": True
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
