from datetime import datetime
from marshmallow import Schema, fields

from ..extensions import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    star_date = db.Column(db.DateTime, default=datetime.utcnow)
    log_entry = db.Column(db.Text, nullable=False)

    crew_member_id = db.Column(db.Integer, db.ForeignKey('crew_member.id'), nullable=False)
    crew_member = db.relationship('CrewMember', backref=db.backref('logs', lazy=True))

    def __repr__(self):
        return '<Log %r>' % self.id

class LogSchema(Schema):
    id = fields.Int()
    star_date = fields.DateTime()
    log_entry = fields.Str()
    crew_member_id = fields.Int()

log_schema = LogSchema()
logs_schema = LogSchema(many=True)