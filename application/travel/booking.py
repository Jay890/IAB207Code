# In this class we need to know another the User and City class
from application.travel.user import User
from application.travel.city import City
# We also need to import date as we need it as type
from datetime import date

# We can show relationship that booking has with User and City below connected from imports above
# So a booking has a User and a City


class Booking:
    start_date: date
    end_date: date
    booking_date: date
    num_guest: int

    user: User
    city: City

# Create a constructor that takes a start date, end date, city, user

    def __init__(self, start_date: date, end_date: date, user: User, city: City):
        self.start_date = start_date
        self.end_date = end_date
        self.user = user
        self.city = city

    def __repr__(self):
        return f"start_date:{self.start_date}, end_date:{self.end_date}, user:{self.user}, city:{self. city}"
