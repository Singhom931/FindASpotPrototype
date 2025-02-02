from flask import Blueprint

main = Blueprint('payment', __name__)

from . import routes