import requests
import allure
import random
import string
from urls import Urls
from faker import Faker
from data import color_selection, TestMessages, EXCLUDE_PARAMETERS




# класс содержит генераторы случайных валидных данных
class Generator:

    # статический метод генерирует случайную последовательность английских букв в нижнем регистре
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string


    # статический метод генерирует случайную последовательность русских букв в нижнем регистре
    @staticmethod
    def generate_random_russian_string(length):
        letters = [chr(i) for i in range(1072, 1105)]
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string


    # статический метод генерирует случайную последовательность цифр в формате строки
    @staticmethod
    def generate_random_numbers_as_string(length):
        numbers = '0123456789'
        random_numbers = ''.join(random.choice(numbers) for _ in range(length))
        return random_numbers


    # статический метод генерирует список из валидных случайных логина, пароля и имени
    @staticmethod
    def generate_payload():
        login = Generator.generate_random_string(10)
        password = Generator.generate_random_numbers_as_string(4)
        first_name = Generator.generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload


    # статический метод генерирует заказ со случайными валидными данными
    @staticmethod
    def generate_random_order_data():
        faker = Faker(locale="ru_RU")
        order_data = {
            "firstName": Generator.generate_random_russian_string(10),
            "lastName": Generator.generate_random_russian_string(15),
            "address": Generator.generate_random_russian_string(20),
            "metroStation": faker.random_int(min=1, max=10, step=1),
            "phone": f"8{Generator.generate_random_numbers_as_string(10)}",
            "rentTime": faker.random_int(min=1, max=6, step=1),
            "deliveryDate": faker.date_between(start_date='+1d', end_date='+5d').isoformat(),
            "comment": Generator.generate_random_russian_string(5),
            "color": random.choice(color_selection)
        }
       # print(order_data)
        return order_data


# класс содержит методы для работы с курьером
class Courier:

    # статический метод регистрирует нового курьера
    @staticmethod
    @allure.step('Регистрация курьера')
    def register_courier(courier_data):
        response = requests.post(url=Urls.CREATE_COURIER, data=courier_data)
        return response


    # статический метод исключает заданную пару ключ-значение из регистрационных данных
    @staticmethod
    def excludes_parameter_from_courier_registration_data(registered_courier_data, exclude):
        del registered_courier_data[exclude]
        return registered_courier_data


    # статический метод изменяет значение регистрационных данных по ключу(исключает последний символ)
    @staticmethod
    def change_parameter_value_in_courier_registration_data(registered_courier_data, change):
        change_data = registered_courier_data[change]
        registered_courier_data[change] = change_data[:-1]
        return registered_courier_data


    # статический метод авторизует курьера
    @staticmethod
    @allure.step('Авторизация курьера')
    def login_courier(registered_courier_data):
        del registered_courier_data[EXCLUDE_PARAMETERS["firstName"]]
        response = requests.post(url=Urls.LOGIN_COURIER, data=registered_courier_data)
        return response


    # статический метод удаляет курьера после теста
    @staticmethod
    def delete_courier(registered_courier_data):
        response = Courier.login_courier(registered_courier_data)
        if response.status_code == TestMessages.COURIER_DELETE["code"]:
            courier_id = response.json()["id"]
            requests.delete(f"{Urls.DELETE_COURIER}{courier_id}")


# класс содержит методы для работы с заказом
class Order:

    # статический метод создаёт заказ
    # и добавляет к json трек заказа по ключу DELETE для дальнейшего удаления заказа после теста
    @staticmethod
    @allure.step('Создать заказ')
    def create_order(order_data):
        response = requests.post(url=Urls.CREATE_ORDER, data=order_data)
        order_data["delete"] = response.json()["track"]
        return response


    # статический метод удаляет заказ после теста
    @staticmethod
    def delete_order_after_test(order_data):
        track = order_data["delete"]
        requests.put(url=Urls.CANCEL_ORDER, data={
            "track": track
        })


    # статический метод получает список заказов
    @staticmethod
    @allure.step('Получить список заказов')
    def get_list_of_orders():
        return requests.get(url=Urls.GET_LIST_OF_ORDERS)




