# dependencies
from travel import db, create_app

# create instance of our app
app = create_app()
context = app.app_context()
context.push()

db.create_all()
