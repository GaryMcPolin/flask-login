# from flask import Flask
# from flask_bootstrap import Bootstrap
# import logging
#
# logging.basicConfig()
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'Thisisasecret'
# app.config['DEBUG'] = True
#
# bootstrap = Bootstrap(app)
#
# # Imports routes for app
# from errors.handlers import *
#
# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port=5000)
from app import create_app

app = create_app()
app.config['DEBUG'] = True

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
