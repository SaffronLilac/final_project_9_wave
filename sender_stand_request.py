import requests
import configuration



def create_order(order_data, headers):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                             json=order_data,
                             headers=headers)
    return response


def get_order_by_track(track, headers):
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                            params={'t': track},
                            headers=headers)
    return response

