countries_schema = {
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "countries": {
          "type": "array",
          "items": {
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
                "type": ["null", "string"]
              },
              "passportNumberMask": {
                "type": ["null", "string"]
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
              "phoneMaskWithCountryCode": {
                "type": ["null", "string"]
              },
              "phoneMaskWithoutCountryCode": {
                "type": ["null", "string"]
              },
              "mobilePhoneRegex": {
                "type": ["null", "string"]
              }
            },
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
              "phoneMaskWithCountryCode",
              "phoneMaskWithoutCountryCode",
              "mobilePhoneRegex"
            ]
          },
          "minItems": 1,
        }
      },
      "required": [
        "countries"
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
