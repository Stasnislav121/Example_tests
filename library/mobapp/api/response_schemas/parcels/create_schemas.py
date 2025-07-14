parcel_create_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                },
                "type": {},
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
                    "properties": {
                        "id": {
                            "type": "number"
                        },
                        "type": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "icon": {
                            "type": "string"
                        },
                        "date": {
                            "type": "string"
                        },
                        "color": {
                            "type": "string"
                        },
                        "location": {}
                    },
                    "required": [
                        "id",
                        "type",
                        "title",
                        "icon",
                        "date",
                        "color",
                        "location"
                    ]
                },
                "statuses": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "type": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "icon": {
                                "type": "string"
                            },
                            "date": {
                                "type": "string"
                            },
                            "color": {
                                "type": "string"
                            },
                            "location": {}
                        },
                        "required": [
                            "id",
                            "type",
                            "title",
                            "icon",
                            "date",
                            "color",
                            "location"
                        ]
                    }
                },
                "sender": {},
                "receiver": {},
                "deliveryDate": {},
                "storageDate": {},
                "deliveryInfo": {
                    "type": "object",
                    "properties": {
                        "deliveryId": {
                            "type": "string"
                        },
                        "deliveryInfo": {
                            "type": "string"
                        },
                        "price": {
                            "type": "object",
                            "properties": {
                                "value": {
                                    "type": "number"
                                },
                                "code": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "value",
                                "code"
                            ]
                        }
                    },
                    "required": [
                        "deliveryId",
                        "deliveryInfo",
                        "price"
                    ]
                },
                "senderOffice": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "address": {
                            "type": "object",
                            "properties": {
                                "postcode": {
                                    "type": "string"
                                },
                                "country": {
                                    "type": "string"
                                },
                                "city": {
                                    "type": "object",
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
                                    },
                                    "required": [
                                        "code",
                                        "title",
                                        "latitude",
                                        "longitude"
                                    ]
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
                                }
                            },
                            "required": [
                                "postcode",
                                "country",
                                "city",
                                "address",
                                "latitude",
                                "longitude",
                                "countryCode"
                            ]
                        },
                        "favourite": {
                            "type": "boolean"
                        },
                        "schedule": {
                            "type": "object",
                            "properties": {
                                "detailedSchedule": {
                                    "type": "object",
                                    "properties": {
                                        "sun": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "mon": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "tue": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "wed": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "thu": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "fri": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "sat": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        }
                                    },
                                    "required": [
                                        "sun",
                                        "mon",
                                        "tue",
                                        "wed",
                                        "thu",
                                        "fri",
                                        "sat"
                                    ]
                                },
                                "shortSchedule": {
                                    "type": "object",
                                    "properties": {
                                        "weekdays": {
                                            "type": "object",
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ]
                                        },
                                        "weekends": {
                                            "type": "object",
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "weekdays",
                                        "weekends"
                                    ]
                                },
                                "description": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "detailedSchedule",
                                "shortSchedule",
                                "description"
                            ]
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
                            }
                        },
                        "phone": {
                            "type": "string"
                        },
                        "services": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "number"
                                    },
                                    "title": {
                                        "type": "string"
                                    },
                                    "price": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "number"
                                            },
                                            "code": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "value",
                                            "code"
                                        ]
                                    }
                                },
                                "required": [
                                    "id",
                                    "title",
                                    "price"
                                ]
                            }
                        },
                        "howToGet": {
                            "type": "string"
                        },
                        "media": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "number"
                                    },
                                    "type": {
                                        "type": "string"
                                    },
                                    "link": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "id",
                                    "type",
                                    "link"
                                ]
                            }
                        },
                        "officeType": {
                            "type": "string"
                        },
                        "companyName": {},
                        "isAwaitingReview": {
                            "type": "boolean"
                        }
                    },
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
                    ]
                },
                "senderAddress": {},
                "receiverOffice": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "address": {
                            "type": "object",
                            "properties": {
                                "postcode": {
                                    "type": "string"
                                },
                                "country": {
                                    "type": "string"
                                },
                                "city": {
                                    "type": "object",
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
                                    },
                                    "required": [
                                        "code",
                                        "title",
                                        "latitude",
                                        "longitude"
                                    ]
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
                                }
                            },
                            "required": [
                                "postcode",
                                "country",
                                "city",
                                "address",
                                "latitude",
                                "longitude",
                                "countryCode"
                            ]
                        },
                        "favourite": {
                            "type": "boolean"
                        },
                        "schedule": {
                            "type": "object",
                            "properties": {
                                "detailedSchedule": {
                                    "type": "object",
                                    "properties": {
                                        "sun": {
                                            "type": "array",
                                            "items": {}
                                        },
                                        "mon": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "tue": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "wed": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "thu": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "fri": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        },
                                        "sat": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "start": {
                                                        "type": "string"
                                                    },
                                                    "end": {
                                                        "type": "string"
                                                    }
                                                },
                                                "required": [
                                                    "start",
                                                    "end"
                                                ]
                                            }
                                        }
                                    },
                                    "required": [
                                        "sun",
                                        "mon",
                                        "tue",
                                        "wed",
                                        "thu",
                                        "fri",
                                        "sat"
                                    ]
                                },
                                "shortSchedule": {
                                    "type": "object",
                                    "properties": {
                                        "weekdays": {
                                            "type": "object",
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ]
                                        },
                                        "weekends": {
                                            "type": "object",
                                            "properties": {
                                                "workingHours": {
                                                    "type": "string"
                                                },
                                                "break": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "workingHours",
                                                "break"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "weekdays",
                                        "weekends"
                                    ]
                                },
                                "description": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "detailedSchedule",
                                "shortSchedule",
                                "description"
                            ]
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
                            }
                        },
                        "phone": {
                            "type": "string"
                        },
                        "services": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "number"
                                    },
                                    "title": {
                                        "type": "string"
                                    },
                                    "price": {
                                        "type": "object",
                                        "properties": {
                                            "value": {
                                                "type": "number"
                                            },
                                            "code": {
                                                "type": "string"
                                            }
                                        },
                                        "required": [
                                            "value",
                                            "code"
                                        ]
                                    }
                                },
                                "required": [
                                    "id",
                                    "title",
                                    "price"
                                ]
                            }
                        },
                        "howToGet": {
                            "type": "string"
                        },
                        "media": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "number"
                                    },
                                    "type": {
                                        "type": "string"
                                    },
                                    "link": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "id",
                                    "type",
                                    "link"
                                ]
                            }
                        },
                        "officeType": {
                            "type": "string"
                        },
                        "companyName": {},
                        "isAwaitingReview": {
                            "type": "boolean"
                        }
                    },
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
                    ]
                },
                "receiverAddress": {},
                "pack": {
                    "type": "object",
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
                            "type": "number"
                        },
                        "width": {
                            "type": "number"
                        },
                        "height": {
                            "type": "number"
                        },
                        "parcelExample": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "image",
                        "",
                        "length",
                        "width",
                        "height",
                        "parcelExample"
                    ]
                },
                "payer": {
                    "type": "string"
                },
                "cost": {},
                "worth": {},
                "services": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "number"
                            },
                            "title": {
                                "type": "string"
                            },
                            "price": {
                                "type": "object",
                                "properties": {
                                    "value": {
                                        "type": "number"
                                    },
                                    "code": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "value",
                                    "code"
                                ]
                            }
                        },
                        "required": [
                            "id",
                            "title",
                            "price"
                        ]
                    }
                },
                "paymentStatus": {
                    "type": "string"
                },
                "paymentType": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "comments": {
                    "type": "string"
                },
                "review": {},
                "barcodeLink": {},
                "receiptLink": {},
                "promocode": {
                    "type": "string"
                },
                "sharedLink": {
                    "type": "string"
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
                    "items": {}
                },
                "isOwner": {
                    "type": "boolean"
                },
                "issueCode": {},
                "options": {
                    "type": "number"
                },
                "flags": {
                    "type": "object",
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
                    },
                    "required": [
                        "officeChange",
                        "deliveryChange",
                        "storageDateTimeChange",
                        "changeAddress",
                        "receiverDataChange",
                        "shouldChangeOffice",
                        "changeTime"
                    ]
                },
                "isFavorite": {
                    "type": "boolean"
                }
            },
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
            ]
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
    },
    "required": [
        "data",
        "success",
        "name",
        "message",
        "time"
    ]
}
