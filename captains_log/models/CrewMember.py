import enum
from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from ..extensions import db

class RankEnum(enum.Enum):
    ensign = 0
    lieutenant = 1
    lieutenant_commander = 2 
    commander = 3
    captain = 4

class CrewMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.Enum(RankEnum), nullable=False)

    def __repr__(self):
        return '<CrewMember %r>' % self.name


class CrewMemberSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    rank = EnumField(RankEnum)

crew_member_schema = CrewMemberSchema()
crew_members_schema = CrewMemberSchema(many=True)
