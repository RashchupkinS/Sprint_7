import allure
import pytest
from data import color_selection, TestMessages
from helper import Order




# класс с тестами для создания заказа
class TestCreateOrder:

    @allure.step('Создание заказа')
    @pytest.mark.parametrize('color', color_selection)
    def test_create_order_successful_creation(self, random_order_data, color):
        random_order_data["color"] = color
        response = Order.create_order(random_order_data)
        assert response.status_code == TestMessages.ORDER_SUCCESSFUL_CREATION["code"]
        assert TestMessages.ORDER_SUCCESSFUL_CREATION["message"] in response.json()


# класс с тестами для проверки получения списка заказов
class TestListOfOrders:

    @allure.step('Получение списка заказов')
    def test_get_list_of_orders_successful(self):
        response = Order.get_list_of_orders()
        assert response.status_code == TestMessages.ORDER_GET_LIST_OF_ORDERS["code"]
        assert TestMessages.ORDER_GET_LIST_OF_ORDERS["message"] in response.json()




