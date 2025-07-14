class ParcelsResponseHandler:
    @staticmethod
    def get_string_delivery_small_description(days):
        if days % 10 == 1 and days % 100 != 11:
            return f'Через {days} рабочий день'
        elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
            return f'Через {days} рабочих дня'
        else:
            return f'Через {days} рабочих дней'

    @staticmethod
    def get_parcels_list(parcels_resp):
        result = [parcel["result"] for parcel in parcels_resp]
        return result
