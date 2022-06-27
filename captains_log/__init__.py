from .blueprints import crew_member
from flask import Flask

from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    db.init_app(app)

    @app.route("/hello_captain")
    def hello_captain():
        return "<p>Hello, Captain!</p>"

    # Blueprints
    from .blueprints import crew_member, log
    app.register_blueprint(crew_member.bp)
    app.register_blueprint(log.bp)

    return app