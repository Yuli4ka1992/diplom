import sender_stand_request
import data

def order(data):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
         json=data.order_body)
    response = post_new_order(data.order_body);
    print(response.status_code)
    print(response.json())


def test_create_user_number_type_first_name_get_error_response():
    order_data = get_order_data(new)
    response = sender_stand_request.post_new_order(order_data)
    assert response.status_code == 200

def zakaz_finished_true():
    if finished == true
    print ('2')

def zakaz_canсelled_true():
    if canсelled == true
    print ('-1')

def zakaz_inDelivery_true():
    if canсelled == true
    print ('1')

def zakaz_all():
    if finished != true
    and canсelled != true
    and canсelled != true
    print ('0')