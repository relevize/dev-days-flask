from flask import Blueprint, jsonify

from ..models.CrewMember import CrewMember

bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/<int:id>', methods=["GET"])
def get_user_token(id):

    # verify user exists - could this become a decorator?
    crew_member_id = CrewMember.query.filter_by(id=id).first()
    if not crew_member_id:
        return "That crew member does not exist.", 400

    jwt = CrewMember.encode_auth_token(id)

    data = {
        "message": "Here is like a 'totally secure' secret key, dude",
        "jwt": "Bearer " + jwt
    }

    return jsonify(data), 200