from flask import Flask, render_template
# from flask_bootstrap3 import Bootstrap
from flask.ext.bootstrap import Bootstrap
from datetime import datetime
from flask.ext.moment import Moment


app = Flask(__name__)
Bootstrap(app)
Moment(app)
app.config['SECRET_KEY'] = 'hard to x'

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
