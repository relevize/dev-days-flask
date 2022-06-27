from flask import Blueprint, request, jsonify

from ..models.CrewMember import CrewMember
from ..extensions import db

bp = Blueprint('crew_member', __name__, url_prefix="/crew_member")

@bp.route("/greeting")
def hello_world():
    return "<p>Hello, crew member!</p>"

@bp.route("/", methods=["POST"])
def create_crew_member():
    data = request.get_json()
    print(data)
    new_crew_member = CrewMember(name=data['name'], rank=data['rank'])

    db.session.add(new_crew_member)
    db.session.commit()

    return "", 204

@bp.route("/", methods=["GET"])
def get_all_crew_members():
    result = CrewMember.query.all()
    users = []
    for user in result:
        users.append(user.name)
    return jsonify(users), 200

@bp.route("/<int:id>", methods=['GET'])
def get_crew_member_by_id(id):
    return f"<p>Crew Member Id: {id}</p>"