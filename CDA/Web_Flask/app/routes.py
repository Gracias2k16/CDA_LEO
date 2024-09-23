from app import app

@app.route('/') # decorators
@app.route('/index')
def index():
    strResult = 'Hello Bruz!'
    return strResult
