# Class keyword followed by the name of class (uppercase convention)
from travel import db


class User(db.Model):
    # good practice to specify table name and also allows all data (current and new) to be put in users table
    __table__ = 'users'
    # define the primary key in class
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)



    # user_name: str
    # password_hash: str
    # email: str
    # user_type: str
    # Give some attributes from the conceptual model

    # In order to use this User class we have to define a constructor.
    # In python we define a constructor in python is by defining the initialisation function and pass it self
    # Reference to itself

    # def __init__(self):
    #     self.user_type = "guest"

    # In order to use this  class we have to create an instance of this class in the main.py and we have to import it
    # there

    # Create a __repr__ function that prints all values

    # def __repr__(self):
    #     return "test"

    # String formatting where we can add some values to my class inside of the string f"something"

    # def __repr__(self):
    #     return f"user_type: {self.user_type}"

    # Create a register function that takes username, password and emailID
    # Below is a public method for the User class which we can call from other class instances
    def register(self, user_name: str, password_hash: str, email: str):
        self.user_name = user_name
        self.password_hash = password_hash
        self.email = email
