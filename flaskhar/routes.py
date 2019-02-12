from . import app

@app.route('/', subdomain='home')
def hello_world():
    return "Hello world"