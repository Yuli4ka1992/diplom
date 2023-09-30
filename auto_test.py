import sender_stand_request
import data

def test_get_order_by_track():
    order = sender_stand_request.post_new_order(data.order_body) # создание заказа
    track = order.json()["track"]  # сохранение
    check_order = sender_stand_request.get_order_info(track)
    assert check_order.status_code == 200

# Юлия Жирова, 8-я когорта — Финальный проект. Инженер по тестированию плюс
