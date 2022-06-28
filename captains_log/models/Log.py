from datetime import datetime
from marshmallow import Schema, fields, pre_dump

from ..extensions import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    star_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    log_entry = db.Column(db.Text, nullable=False)
    redacted = db.Column(db.Boolean, nullable=False, default=False)

    crew_member_id = db.Column(db.Integer, db.ForeignKey('crew_member.id'), nullable=False)
    crew_member = db.relationship('CrewMember', backref=db.backref('logs', lazy=True))

    def __repr__(self):
        return '<Log %r>' % self.id

class LogSchema(Schema):
    id = fields.Int()
    star_date = fields.DateTime()
    log_entry = fields.Str()
    redacted = fields.Bool(load_only=True)
    crew_member_id = fields.Int()
    formatted_log_entry = fields.Method('format_log_entry', dump_only=True)

    def format_log_entry(self, log):
        if log.redacted:
            return "Log entry is redacted, and only accessale by senior officers."
        return log.log_entry

log_schema = LogSchema()
logs_schema = LogSchema(many=True)