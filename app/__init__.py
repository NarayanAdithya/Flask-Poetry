from flask import Flask

app = Flask(__name__)

from app.home import home

app.register_blueprint(home, url_prefix='')
