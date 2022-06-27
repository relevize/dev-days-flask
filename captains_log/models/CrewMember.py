from ..extensions import db

class CrewMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rank = db.Column(db.String(80), nullable=False) # turn this into enum

    def __repr__(self):
        return '<CrewMember %r>' % self.name