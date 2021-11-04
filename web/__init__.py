from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'starting_key'

    from .auth import auth
    from .views import views

    # app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(auth, url_prefix='/')

    app.register_blueprint(views, url_prefix=str)
    app.register_blueprint(auth, url_prefix=str)

    return app
