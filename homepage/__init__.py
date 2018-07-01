from flask import Flask
from flask import render_template
from flask import request

from .homepage.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/')
def index():
    return render_template('home.html')

if app == '__main__':
    app.run(debug=True)