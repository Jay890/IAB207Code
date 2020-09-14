from travel.models.comment import Comment

class Destination:
    name:str
    description: str
    image_url: str
    currency: str
    comments: list

    def __init__(self, name:str, description:str, image_url:str, currency:str, comments: list):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.currency = currency
        self.comments = comments

    
