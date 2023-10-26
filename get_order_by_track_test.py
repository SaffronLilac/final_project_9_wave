# Белла Гереева, 9-й поток - Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


def test_get_order_by_track_success():
    create_order_response = sender_stand_request.create_order(data.order_data, data.headers)
    track = create_order_response.json().get('track')

    get_order_by_track_response = sender_stand_request.get_order_by_track(track, data.headers)
    get_order_by_track_status = get_order_by_track_response.status_code

    assert get_order_by_track_status == 200
