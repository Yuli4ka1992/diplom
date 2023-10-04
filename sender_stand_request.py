import configuration
import requests
import data

def post_new_order(order_body): # функция для создания заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, order_body)

def get_order_info(t): # функция для проверки заказа про треку
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO + '?t=' + str(t))
# Использую арумент функции, это динамический параметр, а не фиксированное значение
