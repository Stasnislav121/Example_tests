parcels_search_success_schema = {
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
                            "id": {"type": "string"},
                            "type": {"type": "string"},
                            "title": {"type": "string"},
                            "trackNumber": {"type": "string"},
                            "storeTrackNumber": {"type": "string"},
                            "status": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "integer"},
                                    "title": {"type": "string"},
                                    "icon": {"type": "string", "format": "uri"},
                                    "date": {"type": ["string", "null"], "format": "date-time"},
                                    "color": {"type": "string"}
                                },
                                "required": ["id", "title", "icon", "color"]
                            },
                            "review": {"type": ["string", "null"]},
                            "barcodeLink": {"type": ["string", "null"], "format": "uri"},
                            "additionalInfo": {"type": "string"},
                            "isRemovable": {"type": "boolean"},
                            "retry": {"type": "boolean"},
                            "isFinished": {"type": "boolean"},
                            "isOwner": {"type": "boolean"},
                            "deliveryType": {"type": "string"},
                            "senderOffice": {
                                "type": ["object", "null"],
                                "properties": {
                                    "id": {"type": "string"},
                                    "address": {
                                        "type": "object",
                                        "properties": {
                                            "full": {"type": "string"}
                                        },
                                        "required": ["full"]
                                    },
                                    "isAwaitingReview": {"type": "boolean"}
                                },
                                "required": ["id", "address", "isAwaitingReview"]
                            },
                            "receiverOffice": {
                                "type": ["object", "null"],
                                "properties": {
                                    "id": {"type": "string"},
                                    "address": {
                                        "type": "object",
                                        "properties": {
                                            "full": {"type": "string"}
                                        },
                                        "required": ["full"]
                                    },
                                    "isAwaitingReview": {"type": "boolean"}
                                },
                                "required": ["id", "address", "isAwaitingReview"]
                            },
                            "options": {"type": "integer"},
                            "flags": {
                                "type": "object",
                                "properties": {
                                    "officeChange": {"type": "boolean"},
                                    "deliveryChange": {"type": "boolean"},
                                    "storageDateTimeChange": {"type": "boolean"},
                                    "changeAddress": {"type": "boolean"},
                                    "receiverDataChange": {"type": "boolean"},
                                    "shouldChangeOffice": {"type": "boolean"},
                                    "changeTime": {"type": "boolean"}
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
                            "isFavorite": {"type": "boolean"}
                        },
                        "required": [
                            "id",
                            "type",
                            "title",
                            "trackNumber",
                            "status",
                            "barcodeLink",
                            "additionalInfo",
                            "isRemovable",
                            "retry",
                            "isFinished",
                            "isOwner",
                            "deliveryType",
                            "senderOffice",
                            "receiverOffice",
                            "options",
                            "flags",
                            "isFavorite"
                        ]
                    }
                },
                "total": {"type": "integer"}
            },
            "required": ["items", "total"]
        },
        "success": {"type": "boolean"},
        "name": {"type": "string"},
        "message": {"type": "string"},
        "time": {"type": "string", "format": "date-time"}
    },
    "required": ["data", "success", "time"]
}


parcels_search_favorite_schema = {
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
              "type": {
                "type": ["string", "null"]
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
                "properties": {
                  "id": {
                    "type": "integer"
                  },
                  "title": {
                    "type": "string"
                  },
                  "icon": {
                    "type": "string",
                    "format": "uri"
                  },
                  "date": {
                    "type": ["string", "null"],
                    "format": "date-time"
                  },
                  "color": {
                    "type": "string"
                  }
                },
                "required": ["id", "title", "icon", "color"]
              },
              "review": {
                "type": ["string", "null"]
              },
              "barcodeLink": {
                "type": ["string", "null"]
              },
              "additionalInfo": {
                "type": "string"
              },
              "isRemovable": {
                "type": "boolean"
              },
              "retry": {
                "type": "boolean"
              },
              "isFinished": {
                "type": "boolean"
              },
              "isOwner": {
                "type": "boolean"
              },
              "deliveryType": {
                "type": "string"
              },
              "senderOffice": {
                "type": ["string", "null"]
              },
              "receiverOffice": {
                "type": ["string", "null"]
              },
              "options": {
                "type": "integer"
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
              "title",
              "trackNumber",
              "status",
              "additionalInfo",
              "isRemovable",
              "retry",
              "isFinished",
              "isOwner",
              "options",
              "flags",
              "isFavorite"
            ]
          }
        },
        "total": {
          "type": "integer"
        }
      },
      "required": ["items", "total"]
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
