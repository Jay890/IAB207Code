from app.travel.user import User
from datetime import date

# Using inheritance from user as FrequentTraveller is a a type of User in our class FrequentTraveller(User)
#  User class will be the base class/parent class


class FrequentTraveller(User):
    num_booking: int
    last_travelled_date: date

    def __init__(self):
        # super().__init__()
        self.user_type = "frequent_traveller"

    def register(self, user_name: str, password: str, email: str):
        super(FrequentTraveller, self).register(user_name, password, email)
        self.num_booking = 10

    def register_user(self, user_name: str, password: str, email: str, travellerID: int):
        super(FrequentTraveller, self).register(
            user_name, password, email)
        self.travellerID = travellerID
