from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/hello_captain")
    def hello_captain():
        return "<p>Hello, Captain!</p>"

    # Blueprints
    from .blueprints import user, log
    app.register_blueprint(user.bp)
    app.register_blueprint(log.bp)

    return app