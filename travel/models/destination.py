from travel.models.comment import Comment
from travel import db

class Destination(db.Model):
    __tablename__ = 'destinations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    currency = db.Column(db.String(3))
    image_url = db.Column(db.String(400))

    # Virtual property - backref
    comments = db.relationship('Comment', backref='destination')

    # name:str
    # description: str
    # image_url: str
    # currency: str
    # comments: list
    #
    # def __init__(self, name:str, description:str, image_url:str, currency:str, comments: list):
    #     self.name = name
    #     self.description = description
    #     self.image_url = image_url
    #     self.currency = currency
    #     self.comments = comments
        # self.comments = list()

    # version 1
    # def add_comment(self, comments: Comment):
    #     self.comments.append(comment)
 
    
    
