from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix="/user")

@bp.route("/")
def hello_world():
    return "<p>Hello, user!</p>"

@bp.route("/<int:id>", methods=['GET'])
def get_user_by_id(id):
    return f"<p>User Id: {id}</p>"