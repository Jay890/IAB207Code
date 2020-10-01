from datetime import datetime
from travel import db

class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())

    # add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))

    # user: str
    # comment_text: str
    # timestamp: datetime

    # create our constructor
    # def __init__(self,  user: str, comment_text: str, timestamp: datetime):
    #     self.user = user
    #     self.comment_text = comment_text
    #     self.timestamp = timestamp
    # now reference comment class (destinations.py)
