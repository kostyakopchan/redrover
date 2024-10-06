import requests

TOKEN_URL = 'https://restful-booker.herokuapp.com/auth'
BOOKING_URL = 'https://restful-booker.herokuapp.com/booking'

def get_token():
    result = requests.post(TOKEN_URL, json={'username' : 'admin',
                                            'password' : 'password123'})
    return result.json()['token']

def new_booking():
    result = requests.post(BOOKING_URL, json={"firstname" : "Konstantin",
                                                "lastname" : "Kopchan",
                                                "totalprice" : 111,
                                                "depositpaid" : True,
                                                "bookingdates" : {
                                                    "checkin" : "2018-01-01",
                                                    "checkout" : "2019-01-01"
                                                                },
                                                "additionalneeds" : "Breakfast"
                                                })
    return result.json()