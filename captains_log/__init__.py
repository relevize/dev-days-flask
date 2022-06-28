from flask import Flask

from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    from .blueprints import crew_member, log, auth
    app.register_blueprint(crew_member.bp)
    app.register_blueprint(log.bp)
    app.register_blueprint(auth.bp)

    return app