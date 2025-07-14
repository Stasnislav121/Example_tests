parcel_calc_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "delivery": {
                    "type": "object",
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
                            "properties": {
                                "value": {
                                    "type": ["integer", "number"]
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
                        "description",
                        "price"
                    ]
                },
                "deliveryServices": {
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
                "discount": {
                    "type": ["null", "object"],
                    "properties": {
                            "title": {
                              "type": "string"
                            },
                            "price": {
                              "type": "object",
                              "properties": {
                                "value": {
                                  "type":  ["integer", "number"]
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
                        "title",
                        "price"
                   ]
                },
                "finalPrice": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": ["integer", "number"]
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
                "delivery",
                "deliveryServices",
                "finalPrice"
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

parcel_calc_err_schema = {
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
              "required": [
                "field",
                "description"
              ]
          }
        }
      },
      "required": [
        "errors"
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
