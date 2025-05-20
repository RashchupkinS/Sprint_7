import pytest
from helper import Generator, Courier, Order
import copy




# фикстура генерирует случайные данные курьера, передаёт их в тест и удаляет курьера после теста
@pytest.fixture()
def random_courier_data():
    random_courier_data = Generator.generate_payload()
    copy_random_courier_data = copy.deepcopy(random_courier_data)
    yield random_courier_data
    Courier.delete_courier(copy_random_courier_data)


# фикстура генерирует случайные данные заказа, передаёт их в тест и удаляет заказ после теста
@pytest.fixture()
def random_order_data():
    random_order_data = Generator.generate_random_order_data()
    yield random_order_data
    Order.delete_order_after_test(random_order_data)





