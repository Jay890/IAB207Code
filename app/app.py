from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

app.run()

# run in the PS C:\Users\vergi\Documents\GitHub\IAB207Code\app using (venv)
# python -m flask run
# Also run without debugging 

