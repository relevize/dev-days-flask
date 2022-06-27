from flask import Blueprint, request, jsonify

from ..models.Log import Log, log_schema, logs_schema
from ..extensions import db

bp = Blueprint('log', __name__, url_prefix="/log")

@bp.route("/", methods=["POST"])
def create_log():
    data = log_schema.load(request.get_json())
    log_entry, crew_member_id = data['log_entry'], data['crew_member_id']
    new_log = Log(log_entry = log_entry, crew_member_id = crew_member_id)
    db.session.add(new_log)
    db.session.commit()

    return "", 200

@bp.route("/", methods=["GET"])
def get_all_crew_members_logs():
    all_logs = Log.query.all()
    dumped_logs = logs_schema.dump(all_logs)

    return jsonify({ 'logs': dumped_logs }), 200