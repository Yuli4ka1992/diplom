import configuration
import requests
import data

def post_new_order(body): # функция для создания заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)

def get_order_info(t): # функция для проверки заказа про треку
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO + '?t=' + str(t))

create_order = post_new_order(data.order_body) # создание заказа
order = create_order.json() # сохранение трека
track = order['track']      # в переменную

check_order = get_order_info(track) # проверка заказа
if check_order.status_code == 200:     # по треку
    print('test passed')

# Юлия Жирова, 8-я когорта — Финальный проект. Инженер по тестированию плюс