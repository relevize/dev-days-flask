from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix="/user")

@bp.route("/")
def hello_world():
    return "<p>Hello, user!</p>"