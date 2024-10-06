import requests
from conftest import get_token, new_booking
BOOKING_URL = 'https://restful-booker.herokuapp.com/booking'

def test_get_bookings():
    response = requests.get(BOOKING_URL)
    if response.status_code == 200:
        print("Get Bookings - PASSED")
    else:
        print("Get Bookings - FAILED")

def test_booking_creation():
    created_booking = new_booking()
    booking_info = requests.get(BOOKING_URL + '/' + str((created_booking['bookingid'])))
    print(booking_info.json())

def test_booking_patch():
    created_booking = new_booking()
    token = get_token()
    booking_patch = requests.patch(BOOKING_URL + '/' + str((created_booking['bookingid'])), 
                                   headers={"Cookie" : "token=" + token},
                                   json={"firstname" : "Konstantinpatched",
                                        "lastname": "Kopchanpatched"})
    print(booking_patch.json())

def test_booking_deletion():
    created_booking = new_booking()
    token = get_token()
    booking_deletion = requests.delete(BOOKING_URL + '/' + str((created_booking['bookingid'])), 
                                   headers={"Cookie" : "token=" + token})
    print(requests.get(BOOKING_URL + '/' + str((created_booking['bookingid']))))