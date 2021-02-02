from flask import Blueprint

bp = Blueprint('jinja_templates', __name__, template_folder='templates')

