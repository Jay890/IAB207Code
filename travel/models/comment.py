from datetime import datetime

class Comment:
    user: str
    comment_text: str
    timestamp: datetime

    # create our constructor
    def __init__(self,  user: str, comment_text: str, timestamp: datetime):
        self.user = user
        self.comment_text = comment_text
        self.timestamp = timestamp
    # now reference comment class (destinations.py)
