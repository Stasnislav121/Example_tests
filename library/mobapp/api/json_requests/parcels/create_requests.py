from library.mobapp.api import AUTOTEST_USER_LONG_EXPIRATION_TOKEN

parcel_create_office_to_office_json = {
    "senderInfo": {
        "cityCode": "68",
        "officeId": "01734",
        "postCode": "",
        "address": "",
        "personalUserInfo": {
            "currentUserId ": "123",
            "name": AUTOTEST_USER_LONG_EXPIRATION_TOKEN['name'],
            "phone": AUTOTEST_USER_LONG_EXPIRATION_TOKEN['phone'],
            "email": AUTOTEST_USER_LONG_EXPIRATION_TOKEN['email'],
            "passport": {
                "number": "6600888999"
            }
        }
    },
    "receiverInfo": {
        "cityCode": "16",
        "officeId": "01349",
        "postCode": "",
        "address": "",
        "personalUserInfo": {
            "name": "MOBILE AUTOTEST Получатель",
            "phone": AUTOTEST_USER_LONG_EXPIRATION_TOKEN['phone'],
            "email": "mobile@autotest.com",
            "passport": {
                "number": ""
            }
        }
    },
    "parcelInfo": {
        "parcelName": "",
        "deliveryId": "officeToOffice",
        "promo": "",
        "declaredPrice": {
            "value": 1100,
            "code": "RUB"
        },
        "package": "799",
        "paidByReceiver": False,
        "additionalServices": ["1327"]
    }
}


class ParcelCreateJsonConstructor:
    @staticmethod
    def sender_office_delivery():
        return {
            "cityCode": "68",
            "officeId": "01734",
            "postCode": "",
            "address": ""
        }

    @staticmethod
    def receiver_office_delivery():
        return {
            "cityCode": "16",
            "officeId": "96801",
            "postCode": "",
            "address": ""
        }

    @staticmethod
    def sender_data():
        return {
            "currentUserId": "123",
            "name": AUTOTEST_USER_LONG_EXPIRATION_TOKEN['name'],
            "phone": AUTOTEST_USER_LONG_EXPIRATION_TOKEN['phone'],
            "email": AUTOTEST_USER_LONG_EXPIRATION_TOKEN['email'],
            "passport": {
                "number": "6600888999"
            }
        }

    @staticmethod
    def receiver_data():
        return {
            "name": "MOBILE AUTOTEST Получатель",
            "phone": AUTOTEST_USER_LONG_EXPIRATION_TOKEN['phone'],
            "email": "mobile@autotest.com",
            "passport": {
                "number": ""
            }
        }

    @staticmethod
    def parcel_data():
        return {
            "parcelName": "",
            "promo": "",
            "declaredPrice": {
                "value": 1100,
                "code": "RUB"
            },
            "paidByReceiver": False,
            "additionalServices": ["1327"]
        }

    @staticmethod
    def bb_package():
        return '799'

    @staticmethod
    def custom_package():
        return {
            "height": 1,
            "length": 21,
            "width": 30
        }

    def build_parcel(self, params: dict):
        sender_info_full = {
            **params['sender_delivery'],
            "personalUserInfo": params['sender_info']
        }

        receiver_info_full = {
            **params['receiver_delivery'],
            "personalUserInfo": params['receiver_info']
        }

        parcel_info = params['parcel_info']
        parcel_info['deliveryId'] = params['delivery_id']
        package = params['package_type']
        if isinstance(package, str):
            parcel_info['package'] = package
        else:
            parcel_info['customPackage'] = package

        return {
            "senderInfo": sender_info_full,
            "receiverInfo": receiver_info_full,
            "parcelInfo": parcel_info
        }

    def parcel_office_to_office_package_bb_json(self, sender_info=None, receiver_info=None, sender_delivery=None,
                                                receiver_delivery=None, delivery_id=None, parcel_info=None,
                                                package_type=None):
        params = {
            "sender_info": sender_info or self.sender_data(),
            "receiver_info": receiver_info or self.receiver_data(),
            "sender_delivery": sender_delivery or self.sender_office_delivery(),
            "receiver_delivery": receiver_delivery or self.receiver_office_delivery(),
            "delivery_id": delivery_id or "officeToOffice",
            "parcel_info": parcel_info or self.parcel_data(),
            "package_type": package_type or self.bb_package()
        }
        return self.build_parcel(params)

    def parcel_office_to_office_custom_package_json(self, sender_info=None, receiver_info=None, sender_delivery=None,
                                                    receiver_delivery=None, delivery_id=None, parcel_info=None,
                                                    package_type=None):
        params = {
            "sender_info": sender_info or self.sender_data(),
            "receiver_info": receiver_info or self.receiver_data(),
            "sender_delivery": sender_delivery or self.sender_office_delivery(),
            "receiver_delivery": receiver_delivery or self.receiver_office_delivery(),
            "delivery_id": delivery_id or "officeToOffice",
            "parcel_info": parcel_info or self.parcel_data(),
            "package_type": package_type or self.custom_package()
        }
        return self.build_parcel(params)
