from flask import Blueprint

from ..models import Log

bp = Blueprint('log', __name__, url_prefix="/log")

@bp.route("/")
def hello_world():
    return "<p>Hello, log!</p>"

@bp.route("/<int:id>", methods=['GET'])
def get_log_by_id(id):
    return f"<p>Log Id: {id}</p>"