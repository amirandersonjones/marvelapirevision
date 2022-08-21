# from the flask package that we installed import the Flask object/class
from flask import Flask

# from our config file import the Config class that we created
from config import Config

# define/instantiate our Flask object...aka tell the computer that this is a flask app
app = Flask(__name__, static_url_path='/static', static_folder='static')


# aka configure our flask app from the Config object we just wrote
app.config.from_object(Config)