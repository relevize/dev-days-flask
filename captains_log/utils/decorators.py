from flask import request, jsonify

from ..models.CrewMember import CrewMember, crew_member_schema

def extract_jwt_and_hydrate_crew_member(func):
    def extract_jwt_and_hydrate_crew_member_wrapper(**kwargs):
        auth_header = request.headers.get('Authorization')
        auth_token = auth_header.split(" ")[1]
        decoded_token = CrewMember.decode_auth_token(auth_token)
        crew_member_id = decoded_token
        crew_member = CrewMember.query.filter_by(id=crew_member_id).first()
        dumped_crew_member = crew_member_schema.dump(crew_member)
        kwargs["crew_member"] = dumped_crew_member

        return func(**kwargs)

    return extract_jwt_and_hydrate_crew_member_wrapper

def authenticate_captain_rank(func):
    def wrapper(**kwargs):
        """
        Only a Captain should be able to view all logs!
        """
        requester_rank = kwargs['crew_member']['rank']
        if requester_rank != 'captain':
            requester_name = kwargs['crew_member']['name']
            message = f'{requester_rank} {requester_name}, only a crew member with the rank of captain may view all logs'
            return jsonify({ 'message': message }), 403

        return func(**kwargs)

    return wrapper