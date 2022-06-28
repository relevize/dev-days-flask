import enum
import jwt
import datetime
from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from ..extensions import db

class RankEnum(enum.Enum):
    ensign = 0
    lieutenant = 1
    lieutenant_commander = 2 
    commander = 3
    captain = 4

# secret_key = "\x1e[\xb1\x01:\x9a\xb3\x05v6\x8c`\xb3\x9a\xeb5/dm\xde[\x18\xc3\x99"
secret_key = "a_bad_secret_key"

class CrewMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.Enum(RankEnum), nullable=False)

    def encode_auth_token(id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=20, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': id
            }

            return jwt.encode(
                payload,
                secret_key,
                algorithm='HS256'
            )
        except Exception as e:
            return e
            
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, secret_key, algorithms=["HS256"])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return '<CrewMember %r>' % self.name

class CrewMemberSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    rank = EnumField(RankEnum)
    formatted_rank = fields.Method('format_rank', dump_only=True)
    # formatted_rank could also be a `fields.Function`
    # word_count = fields.Function(lambda obj: len(obj.words))


    def format_rank(self, crew_member):
        split_rank = crew_member.rank.name.split('_')
        spaced_rank = ' '.join(split_rank)
        title_case_rank = spaced_rank.title()

        return title_case_rank

crew_member_schema = CrewMemberSchema()
crew_members_schema = CrewMemberSchema(many=True)
