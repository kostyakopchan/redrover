import requests
from conftest import get_token, new_booking
BOOKING_URL = 'https://restful-booker.herokuapp.com/booking'

def test_get_bookings():
    response = requests.get(BOOKING_URL)
    assert response.status_code == 200, "Bookings not received"

def test_booking_creation():
    created_booking = new_booking()
    booking_info = requests.get(BOOKING_URL + '/' + str((created_booking['bookingid'])))
    assert booking_info.json()['firstname'] == created_booking['booking']['firstname'], "Booking not created"

def test_booking_patch():
    created_booking = new_booking()
    token = get_token()
    booking_patch = requests.patch(BOOKING_URL + '/' + str((created_booking['bookingid'])), 
                                   headers={"Cookie" : "token=" + token},
                                   json={"firstname" : "Konstantinpatched",
                                        "lastname": "Kopchanpatched"})
    assert booking_patch.json()['firstname'] == 'Konstantinpatched', "Name not patched"
    assert booking_patch.json()['lastname'] == 'Kopchanpatched', 'Lastname not patched'

def test_booking_deletion():
    created_booking = new_booking()
    token = get_token()
    booking_deletion = requests.delete(BOOKING_URL + '/' + str((created_booking['bookingid'])), 
                                   headers={"Cookie" : "token=" + token})
    response = requests.get(BOOKING_URL + '/' + str((created_booking['bookingid'])))
    assert response.status_code == 404, 'Booking not deleted'