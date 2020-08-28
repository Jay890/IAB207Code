# Here we have a shortened path import using the __init__.py (package)
from app.travel.user import User
# Import the class User from user.py
from app.travel.city import City
# Import the City class from city.py
from app.travel.booking import Booking
# import the Booking class from booking.py
from datetime import datetime

from app.travel.frequent_traveller import FrequentTraveller

from app.travel import master_user_instance
# Now we can pass this as a parameter or register a user. So this is how you can share code between parts of your
# python application

# from teh __init__.py
from app.travel import x
print(x)

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


# Create an instance of FrequentTraveller class
frequent_traveller_instance = FrequentTraveller()

print(city_details2)
print(city_instance)
print(booking_instance)


# frequent_traveller_instance.register(
#     "Customer 2", "password", "email@gmail.com")

frequent_traveller_instance.register_user(
    "Coco pops", "tasty123", "cocopops@gmail.com", "100")

print(frequent_traveller_instance)


# A tip for inheritance. In our conceptual model. Booking has a relationship with User and City. So knows about them.
# However, booking doesn't know that FrequentTraveller exists. But because FrequentTraveller class is a IS relationship type
# with User. So FrequentTraveller is a type of User and is inherited we can use still use FrequentTraveller as a user in relation
# to Booking

# For example. If we created the frequent_traveller_instance. Then in the booking_stance we have created before with user_instance
# we can now pass in frequent_traveller_instance instead

booking_instance2 = Booking(
    datetime.now(), datetime.now(), frequent_traveller_instance, city_instance)
print(booking_instance2)

# So the above code still runs even though in the Booking constructor we ask for a user and never imported the
# FrequentTraveller class into Booking class. But because FrequentTraveller inherits from User class (is a type of User)
# We can then still pass it as a type of user
# But in the Booking class we won't have access and we can't see the specific attributes from
# FrequentTraveller class e.g. num_booking
