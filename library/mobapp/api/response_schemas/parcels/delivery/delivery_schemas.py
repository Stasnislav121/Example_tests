parcel_delivery_with_export_delivery_type_schema = {
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
              "title": {
                "type": "string"
              },
              "price": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": ["integer", "number"]
                  },
                  "code": {
                    "type": "string",
                    "enum": ["RUB"]
                  }
                },
                "required": [
                  "value",
                  "code"
                ],
                "additionalProperties": False
              },
              "includedServices": {
                "type": "array",
                "items": {
                  "type": "string",
                  "enum": [
                    "Доставка отправления между адресатами",
                    "Упаковка",
                    "Страхование",
                    "Отслеживание",
                    "Проверка содержимого при получении",
                    "Сообщения получателю о поступлении посылки, отправителю – о выдаче посылки (Push/VK/Viber/SMS)",
                    "Доставка посылки курьером",
                    ""
                  ]
                },
                "minItems": 3,
                "maxItems": 3,
                "uniqueItems": True
              },
              "additionalServices": {
                "type": "array",
                "items": {
                  "items": {}
                }
              },
              "isDefault": {
                "type": "boolean"
              },
              "promoDiscount": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": ["integer", "number"]
                  },
                  "code": {
                    "type": "string",
                    "enum": ["RUB"]
                  }
                },
                "required": [
                  "value",
                  "code"
                ],
                "additionalProperties": False
              },
              "deliverySmallDescription": {
                "type": "string",
                "minLength": 1
              },
              "deliveryDetailedDescription": {
                "type": "string",
                "minLength": 1
              },
              "isSelectable": {
                "type": "boolean"
              },
              "footerInfo": {
                "type": "object",
                "properties": {
                  "days": {
                    "type": "string",
                  },
                  "daysType": {
                    "type": "string",
                    "enum": ["working"]
                  },
                  "additionalInfo": {
                    "type": "string",
                    "enum": ["Все налоги уже включены"]
                  }
                },
                "required": [
                  "days",
                  "daysType",
                  "additionalInfo"
                ],
                "additionalProperties": False
              }
            },
            "required": [
              "id",
              "title",
              "price",
              "includedServices",
              "additionalServices",
              "isDefault",
              "promoDiscount",
              "deliverySmallDescription",
              "deliveryDetailedDescription",
              "isSelectable",
              "footerInfo"
            ],
            "additionalProperties": False
          },
          "minItems": 1,
          "maxItems": 1
        }
      },
      "required": [
        "items"
      ],
      "additionalProperties": False
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

parcel_delivery_with_two_delivery_type_schema = {
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
              "title": {
                "type": "string"
              },
              "price": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": ["integer", "number"]
                  },
                  "code": {
                    "type": "string",
                    "enum": ["RUB"]
                  }
                },
                "required": [
                  "value",
                  "code"
                ],
                "additionalProperties": False
              },
              "includedServices": {
                "type": "array",
                "items": {
                  "type": "string",
                  "enum": [
                    "Доставка отправления между адресатами",
                    "Упаковка",
                    "Страхование",
                    "Отслеживание",
                    "Проверка содержимого при получении",
                    "Сообщения получателю о поступлении посылки, отправителю – о выдаче посылки (Push/VK/Viber/SMS)",
                    "Доставка посылки курьером",
                    ""
                  ]
                },
                "minItems": 6,
                "maxItems": 7,
                "uniqueItems": True
              },
              "additionalServices": {
                "type": "array",
                "items": {
                  "items": {}
                }
              },
              "isDefault": {
                "type": "boolean"
              },
              "promoDiscount": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": ["integer", "number"]
                  },
                  "code": {
                    "type": "string",
                    "enum": ["RUB"]
                  }
                },
                "required": [
                  "value",
                  "code"
                ],
                "additionalProperties": False
              },
              "deliverySmallDescription": {
                "type": "string",
                "minLength": 1
              },
              "deliveryDetailedDescription": {
                "type": "string",
                "minLength": 1
              },
              "isSelectable": {
                "type": "boolean"
              },
              "footerInfo": {
                "type": "object",
                "properties": {
                  "days": {
                    "type": "string",
                  },
                  "daysType": {
                    "type": "string",
                    "enum": ["working"]
                  },
                  "additionalInfo": {
                    "type": "string",
                    "enum": ["Все налоги уже включены"]
                  }
                },
                "required": [
                  "days",
                  "daysType",
                  "additionalInfo"
                ],
                "additionalProperties": False
              }
            },
            "required": [
              "id",
              "title",
              "price",
              "includedServices",
              "additionalServices",
              "isDefault",
              "promoDiscount",
              "deliverySmallDescription",
              "deliveryDetailedDescription",
              "isSelectable",
              "footerInfo"
            ],
            "additionalProperties": False
          },
          "minItems": 2,
          "maxItems": 2
        }
      },
      "required": [
        "items"
      ],
      "additionalProperties": False
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

parcel_delivery_with_four_delivery_type_schema = {
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
              "title": {
                "type": "string"
              },
              "price": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": ["integer", "number"]
                  },
                  "code": {
                    "type": "string",
                    "enum": ["RUB"]
                  }
                },
                "required": [
                  "value",
                  "code"
                ],
                "additionalProperties": False
              },
              "includedServices": {
                "type": "array",
                "items": {
                  "type": "string",
                  "enum": [
                    "Доставка отправления между адресатами",
                    "Упаковка",
                    "Страхование",
                    "Отслеживание",
                    "Проверка содержимого при получении",
                    "Сообщения получателю о поступлении посылки, отправителю – о выдаче посылки (Push/VK/Viber/SMS)",
                    "Доставка посылки курьером",
                    ""
                  ]
                },
                "minItems": 6,
                "maxItems": 8,
                "uniqueItems": True
              },
              "additionalServices": {
                "type": "array",
                "items": {
                  "items": {}
                }
              },
              "isDefault": {
                "type": "boolean"
              },
              "promoDiscount": {
                "type": "object",
                "properties": {
                  "value": {
                    "type": ["integer", "number"]
                  },
                  "code": {
                    "type": "string",
                    "enum": ["RUB"]
                  }
                },
                "required": [
                  "value",
                  "code"
                ],
                "additionalProperties": False
              },
              "deliverySmallDescription": {
                "type": "string",
                "minLength": 1
              },
              "deliveryDetailedDescription": {
                "type": "string",
                "minLength": 1
              },
              "isSelectable": {
                "type": "boolean"
              },
              "footerInfo": {
                "type": "object",
                "properties": {
                  "days": {
                    "type": "string",
                  },
                  "daysType": {
                    "type": "string",
                    "enum": ["working"]
                  },
                  "additionalInfo": {
                    "type": "string",
                    "enum": ["Все налоги уже включены"]
                  }
                },
                "required": [
                  "days",
                  "daysType",
                  "additionalInfo"
                ],
                "additionalProperties": False
              }
            },
            "required": [
              "id",
              "title",
              "price",
              "includedServices",
              "additionalServices",
              "isDefault",
              "promoDiscount",
              "deliverySmallDescription",
              "deliveryDetailedDescription",
              "isSelectable",
              "footerInfo"
            ],
            "additionalProperties": False
          },
          "minItems": 4,
          "maxItems": 4
        }
      },
      "required": [
        "items"
      ],
      "additionalProperties": False
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

parcel_delivery_err_schema = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "errors": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "field": {
                "type": "string"
              },
              "description": {
                "type": "string"
              }
            },
            "required": ["field", "description"]
          }
        }
      },
      "required": ["errors"]
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
