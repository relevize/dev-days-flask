from flask import Blueprint

bp = Blueprint('log', __name__, url_prefix="/log")

@bp.route("/")
def hello_world():
    return "<p>Hello, log!</p>"