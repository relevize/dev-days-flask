from .blueprints import crew_member
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)

    class CrewMember(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), nullable=False)
        rank = db.Column(db.String(80), nullable=False) # turn this into enum

        def __repr__(self):
            return '<CrewMember %r>' % self.name

    class Log(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        star_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        log_entry = db.Column(db.Text, nullable=False)

        crew_member_id = db.Column(db.Integer, db.ForeignKey('crew_member.id'), nullable=False)
        crew_member = db.relationship('CrewMember', backref=db.backref('logs', lazy=True))

        def __repr__(self):
            return '<Log %r>' % self.id


    @app.route("/hello_captain")
    def hello_captain():
        return "<p>Hello, Captain!</p>"

    # Blueprints
    from .blueprints import crew_member, log
    app.register_blueprint(crew_member.bp)
    app.register_blueprint(log.bp)

    return app