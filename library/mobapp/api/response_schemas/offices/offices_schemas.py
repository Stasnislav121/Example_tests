info_office_schema = {
  "type": "object",
  "properties": {
    "data": {
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
              "additionalProperties": False,
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
            },
            "countryInfo": {
              "type": "object",
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
              },
              "additionalProperties": False,
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
              ]
            }
          },
          "additionalProperties": False,
          "required": [
            "postcode",
            "country",
            "city",
            "address",
            "latitude",
            "longitude",
            "countryCode",
            "countryInfo"
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
                      "additionalProperties": False,
                      "required": [
                        "start",
                        "end"
                      ]
                  },
                  "additionalItems": False
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
                      "additionalProperties": False,
                      "required": [
                        "start",
                        "end"
                      ]
                  },
                  "additionalItems": False
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
                      "additionalProperties": False,
                      "required": [
                        "start",
                        "end"
                      ]
                  },
                  "additionalItems": False
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
                      "additionalProperties": False,
                      "required": [
                        "start",
                        "end"
                      ]
                  },
                  "additionalItems": False
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
                      "additionalProperties": False,
                      "required": [
                        "start",
                        "end"
                      ]
                  },
                  "additionalItems": False
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
                      "additionalProperties": False,
                      "required": [
                        "start",
                        "end"
                      ]
                  },
                  "additionalItems": False
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
                      "additionalProperties": False,
                      "required": [
                        "start",
                        "end"
                      ]
                  },
                  "additionalItems": False
                }
              },
              "additionalProperties": False,
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
                  "additionalProperties": False,
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
                  "additionalProperties": False,
                  "required": [
                    "workingHours",
                    "break"
                  ]
                }
              },
              "additionalProperties": False,
              "required": [
                "weekdays",
                "weekends"
              ]
            },
            "description": {
              "type": "string"
            }
          },
          "additionalProperties": False,
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
          },
          "minItems": 1
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
                  "type": "integer"
                },
                "title": {
                  "type": "string"
                },
                "price": {
                  "type": "object",
                  "properties": {
                    "value": {
                      "type": "integer"
                    },
                    "code": {
                      "type": "string"
                    }
                  },
                  "additionalProperties": False,
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
          },
          "minItems": 1
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
                  "type": "integer"
                },
                "type": {
                  "type": "string"
                },
                "link": {
                  "type": "string"
                }
              },
              "additionalProperties": False,
              "required": [
                "id",
                "type",
                "link"
              ]
          },
          "minItems": 1
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
      },
      "additionalProperties": False,
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
  "additionalProperties": False,
  "required": [
    "data",
    "success",
    "name",
    "message",
    "time"
  ]
}

offices_schema = {
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
                "id": {
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
                      "type": "string",
                      "enum": ["sending", "receiving"]
                  },
                  "minItems": 1,
                  "maxItems": 2,
                  "additionalItems": False
                },
                "officeType": {
                  "type": "string",
                  "enum": ["base", "express"]
                }
              },
              "additionalProperties": False,
              "required": [
                "id",
                "latitude",
                "longitude",
                "availability",
                "officeType"
              ]
          },
          "minItems": 1
        },
        "total": {
          "type": "integer"
        }
      },
      "additionalProperties": False,
      "required": [
        "items",
        "total"
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
  "additionalProperties": False,
  "required": [
    "data",
    "success",
    "name",
    "message",
    "time"
  ]
}

offices_empty_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "items": {
          "type": "array",
          "items": {},
          "additionalItems": False
        },
        "total": {
          "type": "integer"
        }
      },
      "additionalProperties": False,
      "required": [
        "items",
        "total"
      ]
    },
    "success": {
      "type": "boolean",
      "enum": [True]
    },
    "name": {
      "type": "string",
      "enum": [""]
    },
    "message": {
      "type": "string",
      "enum": [""]
    },
    "time": {
      "type": "string"
    }
  },
  "additionalProperties": False,
  "required": [
    "data",
    "success",
    "name",
    "message",
    "time"
  ]
}


offices_search_schema = {
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
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
              "additionalProperties": False,
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
            "isAvailableForCourier": {
              "type": "boolean"
            }
          },
          "additionalProperties": False,
          "required": [
            "postcode",
            "country",
            "city",
            "address",
            "latitude",
            "longitude",
            "isAvailableForCourier"
          ]
      },
      "minItems": 1,
      "additionalItems": False
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
  "additionalProperties": False,
  "required": [
    "data",
    "success",
    "name",
    "message",
    "time"
  ]
}

office_filters_schema = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "required": [
        "filters",
        "fastFilters"
      ],
      "additionalProperties": False,
      "properties": {
        "filters": {
          "type": "array",
          "additionalItems": False,
          "items": {
            "type": "object",
            "required": [
              "groupId",
              "groupTitle",
              "filters"
            ],
            "additionalProperties": False,
            "properties": {
              "groupId": {
                "type": "string",
                "enum": [
                  "payment-method",
                  "services",
                  "others"
                ]
              },
              "groupTitle": {
                "type": "string",
                "enum": [
                  "Способы оплаты",
                  "Услуги",
                  "Другое"
                ]
              },
              "filters": {
                "type": "array",
                "additionalItems": False,
                "items": {
                  "type": "object",
                  "required": [
                    "id",
                    "title",
                    "isDefault"
                  ],
                  "additionalProperties": False,
                  "properties": {
                    "id": {
                      "type": "string",
                      "enum": [
                        "2",
                        "10",
                        "5",
                        "6",
                        "13",
                        "7",
                        "12",
                        "14"
                      ]
                    },
                    "title": {
                      "type": "string",
                      "enum": [
                        "Оплата картой",
                        "Отправка посылки",
                        "Примерка",
                        "Частичная выдача",
                        "Возврат международных посылок",
                        "Открыто сейчас",
                        "Без выходных",
                        "Рядом"
                      ]
                    },
                    "isDefault": {
                      "type": "boolean",
                      "enum": [False]
                    }
                  }
                },
                "minItems": 1,
                "maxItems": 4
              }
            }
          },
          "minItems": 1,
          "maxItems": 3
        },
        "fastFilters": {
          "type": "array",
          "additionalItems": False,
          "items": {
            "type": "object",
            "required": [
              "id",
              "title",
              "isDefault"
            ],
            "additionalProperties": False,
            "minItems": 8,
            "maxItems": 8,
            "properties": {
              "id": {
                "type": "string",
                "enum": [
                  "2",
                  "10",
                  "5",
                  "6",
                  "13",
                  "7",
                  "12",
                  "14"
                ]
              },
              "title": {
                "type": "string",
                "enum": [
                  "Оплата картой",
                  "Отправка посылки",
                  "Примерка",
                  "Частичная выдача",
                  "Возврат международных посылок",
                  "Открыто сейчас",
                  "Без выходных",
                  "Рядом"
                ]
              },
              "isDefault": {
                "type": "boolean",
                "enum": [False]
              }
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
      "type": "string"
    }
  },
  "additionalProperties": False,
  "required": [
    "data",
    "success",
    "name",
    "message",
    "time"
  ]
}
