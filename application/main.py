from application.travel.user import User
# Import the class User from user.py
from application.travel.city import City
# Import the City class from city.py


# Create an instance of that class by naming it whatever we want followed by class name()
user_instance = User()

#  Create an instance of City class
city_instance = City("Darwin", "It's very hot")

# Are registering / assigning the values to the username, password and email from User class register method
user_instance.register("Bob", "password", "something@gmail.com")

# Whenver we print user_instance it will return whatever we have set in the __repr__ function from User class
print(user_instance)

city_details = city_instance.getCityDetails()
print(city_details)
