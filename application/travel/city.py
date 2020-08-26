class City:
    city_name: str
    city_description: str

    # Create a constructor function that takes the name of the city and description
    # When an object instance of city class is created we need to provide the city name and description ourselves at the time
    #  of creation
    def __init__(self, city_name: str, city_description: str):
        self.city_name = city_name
        self.city_description = city_description

    # Prints the values i the city class

    def __repr__(self):
        return f"city_name:{self.city_name}, city_description:{self.city_description}"

    # Create a method that returns the details of the city
    # Create a getCityDetails()
    # We can specify a return type with -> (which is good practice for other coders to read your code)

    def getCityDetails(self) -> str:
        return f"{self.city_name}, {self.city_description}"
