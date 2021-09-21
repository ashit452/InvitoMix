import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

from flask import Flask

app = Flask(__name__)

app.secret_key = 'sessionData'

app.config['TESTING'] = True

import project.com.controller
