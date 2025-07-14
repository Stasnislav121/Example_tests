import random

bb_package = {
    "packageId": "799",
    "declaredPrice": {
        "code": "RUB",
        "value": 1000.0
    }
}

custom_package = {
    "customPackage": {
        "height": 1,
        "length": 21,
        "width": 30
    },
    "declaredPrice": {
        "code": "RUB",
        "value": 1000.0
    }
}

custom_template_package = {
    "customPackageId": "1",
    "declaredPrice": {
        "code": "RUB",
        "value": 1000.0
    }
}

office_to_office = {
    "cityId": "16",
    "office": {
        "officeId": "66471"
    }
}

office_to_door = {
    "cityId": "116",
    "door": {
        "address": "Россия, Санкт-Петербург, Невский проспект, 68А",
        "postCode": "190000"
    }
}


def get_receiver(delivery_type, personal_info_type):
    receiver = {
        "deliveryType": delivery_type,
        "destinationInfo": personal_info_type,
        "id": f"a597a6b8-{random.randint(0000, 9999)}-4420-87a2-7c58f7af5fe8",
        "paidByReceiver": False,
        "personalInfo": {
            "email": "poluchatel@ddsdf.fd",
            "name": "Poluchatel",
            "phone": "79123456789"
        }
    }
    return receiver


def get_pattern_request_parcel_multi_create(parcel_package, delivery_type, personal_info_type, count_receivers):
    parcel_multi_create_json = {
        "parcel": parcel_package,
        "receivers": [get_receiver(delivery_type=delivery_type,
                                   personal_info_type=personal_info_type) for _ in range(count_receivers)],
        "sender": {
            "destinationInfo": {
                "cityId": "68"
            }
        }
    }
    return parcel_multi_create_json


def parcel_multi_create_office_to_office_json():
    return get_pattern_request_parcel_multi_create(parcel_package=bb_package,
                                                   delivery_type="officeToOffice",
                                                   personal_info_type=office_to_office,
                                                   count_receivers=1)


def parcel_multi_create_office_to_door_json():
    return get_pattern_request_parcel_multi_create(parcel_package=bb_package,
                                                   delivery_type="officeToDoor",
                                                   personal_info_type=office_to_door,
                                                   count_receivers=1)


def parcel_multi_create_custom_package_json():
    return get_pattern_request_parcel_multi_create(parcel_package=custom_package,
                                                   delivery_type="officeToOffice",
                                                   personal_info_type=office_to_office,
                                                   count_receivers=1)


def parcel_multi_create_bb_package_json():
    return get_pattern_request_parcel_multi_create(parcel_package=bb_package,
                                                   delivery_type="officeToOffice",
                                                   personal_info_type=office_to_office,
                                                   count_receivers=1)


def parcel_multi_create_custom_template_package_json():
    return get_pattern_request_parcel_multi_create(parcel_package=custom_template_package,
                                                   delivery_type="officeToOffice",
                                                   personal_info_type=office_to_office,
                                                   count_receivers=1)


def parcel_multi_create_custom_with_many_recievers_json():
    return get_pattern_request_parcel_multi_create(parcel_package=bb_package,
                                                   delivery_type="officeToOffice",
                                                   personal_info_type=office_to_office,
                                                   count_receivers=10)
