# класс содержит ссылки API
class Urls:
    # ссылки для работы с курьером
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    CREATE_COURIER = MAIN_URL + '/api/v1/courier'
    DELETE_COURIER = MAIN_URL + '/api/v1/courier/'
    LOGIN_COURIER = MAIN_URL + '/api/v1/courier/login'

    # ссылки для работы с заказом
    CREATE_ORDER = MAIN_URL + '/api/v1/orders'
    CANCEL_ORDER = MAIN_URL + '/api/v1/orders/cancel'
    GET_LIST_OF_ORDERS = MAIN_URL + '/api/v1/orders'




