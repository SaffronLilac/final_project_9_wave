# Белла Гереева, 9-й поток - Финальный проект. Инженер по тестированию плюс
import requests
import data
import configuration


def create_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                             json=data.order_data,
                             headers=data.headers)
    track = response.json().get('track')
    return track


def get_order_by_track(track):
    # print(f"track is {track}")
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                            params={'t': track},
                            headers=data.headers)
    # print(f"status-code is {response.status_code}")
    return response.status_code


def test_order():
    track = create_order()
    assert get_order_by_track(track) == 200
