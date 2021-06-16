from app import app
from app import views


@app.route('/')
@app.route('/index')
def index():
    return 'Ok'
