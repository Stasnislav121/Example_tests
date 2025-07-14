parcel_calc_multi_with_custom_package_json = {
    "parcel": {
        "customPackage": {
            "width": 1,
            "length": 1,
            "height": 1
        },
        "declaredPrice": {
            "code": "RUB",
            "value": 1000
        }
    },
    "receivers": [
        {
            "deliveryType": "officeToOffice",
            "destinationInfo": {
                "cityId": "68",
                "office": {
                    "officeId": "01734"
                }
            },
            "id": "b0cb80e9-4fcc-4d1e-a0b7-24062af04f51",
            "paidByReceiver": False
        }
    ],
    "sender": {
        "destinationInfo": {
            "cityId": "68"
        }
    }
}

parcel_calc_multi_with_package_json = {
    "parcel": {
        "packageId": "799",
        "declaredPrice": {
            "code": "RUB",
            "value": 1000
        }
    },
    "receivers": [
        {
            "deliveryType": "officeToOffice",
            "destinationInfo": {
                "cityId": "68",
                "office": {
                    "officeId": "01734"
                }
            },
            "id": "b0cb80e9-4fcc-4d1e-a0b7-24062af04f51",
            "paidByReceiver": False
        }
    ],
    "sender": {
        "destinationInfo": {
            "cityId": "16"
        }
    }
}

parcel_calc_multi_with_custom_package_id_json = {
    "parcel": {
        "customPackageId": 13,
        "declaredPrice": {
            "code": "RUB",
            "value": 1000
        }
    },
    "receivers": [
        {
            "deliveryType": "officeToOffice",
            "destinationInfo": {
                "cityId": "68",
                "office": {
                    "officeId": "01734"
                }
            },
            "id": "b0cb80e9-4fcc-4d1e-a0b7-24062af04f51",
            "paidByReceiver": False
        }
    ],
    "sender": {
        "destinationInfo": {
            "cityId": "16"
        }
    }
}


parcel_calc_multi_with_cd_json = {
  "parcel": {
    "customPackageId": "null",
    "declaredPrice": {
      "code": "RUB",
      "value": 1000.0
    },
    "packageId": "799"
  },
  "receivers": [
    {
      "deliveryType": "officeToDoor",
      "destinationInfo": {
        "cityId": "25",
        "door": {
          "address": "Россия, Краснодар, Центральный внутригородской округ, микрорайон Центральный, Длинная улица, 84",
          "postCode": "350000"
        }
      },
      "id": "f69bbb8e-cf63-4c41-bd83-81f9de2b0be4",
      "paidByReceiver": False,
      "personalInfo": {
        "email": "hdhdjd@djdj.dk",
        "name": "bzhx dbd",
        "phone": "79124346464"
      }
    }
  ],
  "sender": {
    "destinationInfo": {
      "cityId": "16"
    }
  }
}
