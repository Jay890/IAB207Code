from application.travel.user import User
# Import the class User from user.py
from application.travel.city import City
# Import the City class from city.py
from application.travel.booking import Booking
# import the Booking class from booking.py
from datetime import datetime


# Create an instance of that class by naming it whatever we want followed by class name()
user_instance = User()

#  Create an instance of City class
city_instance = City("Darwin", "It's very hot")

#  Create an instance of the Booking class
booking_instance = Booking(
    datetime.now(), datetime.now(), user_instance, city_instance)

# Are registering / assigning the values to the username, password and email from User class register method
user_instance.register("Bob", "password", "something@gmail.com")

# Whenver we print user_instance it will return whatever we have set in the __repr__ function from User class
print(user_instance)

city_details = city_instance.getCityDetails()
print(city_details)

# Create an another instance of City
city_place2 = City("Perth", "It's very cool")

city_details2 = city_place2.getCityDetails()

print(city_details2)
print(city_instance)
print(booking_instance)
