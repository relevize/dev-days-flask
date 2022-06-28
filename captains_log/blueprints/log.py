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
def get_all_logs():
    all_logs = Log.query.all()
    dumped_logs = logs_schema.dump(all_logs)

    return jsonify({ 'logs': dumped_logs }), 200

@bp.route("/<int:id>", methods=["GET"])
def get_log_by_id(id):
    log = Log.query.filter_by(id=id).first()
    dumped_log = log_schema.dump(log)

    return jsonify({ 'log': dumped_log }), 200

@bp.route("/crew_member/<int:id>", methods=["GET"])
def get_crew_member_logs(id):
    logs = Log.query.filter_by(crew_member_id=id).all()
    dumped_logs = logs_schema.dump(logs)

    return jsonify({ 'logs': dumped_logs }), 200

@bp.route("/<int:id>", methods=["PUT"])
def redact_log(id):
    log = Log.query.filter_by(id=id).first()
    log.redacted = True
    db.session.commit()

    return "The log has been redacted.", 200

@bp.route("/<int:id>", methods=["DELETE"])
def delete_log_by_id(id):
    Log.query.filter_by(id=id).delete()
    db.session.commit()

    return "", 204


"""
Routes to make:
[x] Create Log
[x] Get All Logs
[x] Get Log By Id
[x] Get Crew Member Logs
[x] Delete Log (this is temporary)

Migration:
[x] Migration to include Redacted
[ ] Update routes to not return content if redacted
[x] Redact Log endpoint (this needs to wait for a migration)

Auth:
[ ] Routes must check for rank somehow

Relationship:
[ ] return full crew_member object instead of just id
"""