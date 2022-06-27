from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/hello_captain")
    def hello_captain():
        return "<p>Hello, Captain!</p>"

    # Routes
    from . import user
    app.register_blueprint(user.bp)

    from . import log
    app.register_blueprint(log.bp)

    return app