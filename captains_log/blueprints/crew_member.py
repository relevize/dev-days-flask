from flask import Blueprint

bp = Blueprint('crew_member', __name__, url_prefix="/crew_member")

@bp.route("/")
def hello_world():
    return "<p>Hello, crew member!</p>"

@bp.route("/<int:id>", methods=['GET'])
def get_crew_member_by_id(id):
    return f"<p>Crew Member Id: {id}</p>"