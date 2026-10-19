from flask import Flask
from config.config import CONFIGS
from extension import db

def create_app(env_name, overrides=None):
    app = Flask(__name__)
    app.config.from_object(CONFIGS[env_name])
    if overrides:
        app.config.update(overrides)

    db.init_app(app) # connect extension

    from models.profile import Profile
    from models.user import User

    from controllers.routes import bp
    app.register_blueprint(bp)

    with app.app_context(): # context required
        db.create_all() # create missing tables
        
    return app
