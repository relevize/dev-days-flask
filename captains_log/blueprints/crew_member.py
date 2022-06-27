from flask import Blueprint, request, jsonify

from ..models.CrewMember import CrewMember, crew_member_schema, crew_members_schema
from ..extensions import db

bp = Blueprint('crew_member', __name__, url_prefix="/crew_member")

@bp.route("/", methods=["POST"])
def create_crew_member():
    data = crew_member_schema.load(request.get_json())
    name, rank = data['name'], data['rank']

    new_crew_member = CrewMember(name = name, rank = rank)

    db.session.add(new_crew_member)
    db.session.commit()

    return f"Welcome aboard {rank} {name}", 200

@bp.route("/", methods=["GET"])
def get_all_crew_members():
    all_crew_members = CrewMember.query.all()
    dumped_crew_members = crew_members_schema.dump(all_crew_members)

    return jsonify({'crew_members': dumped_crew_members}), 200

@bp.route("/<int:id>", methods=['GET'])
def get_crew_member_by_id(id):
    crew_member = CrewMember.query.filter_by(id=id).first()
    dumped_crew_member = crew_member_schema.dump(crew_member)

    return jsonify(dumped_crew_member), 200
