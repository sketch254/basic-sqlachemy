from flask_sqlalchemy import SQLAlchemy
# 2. Instantiate without app instance
# Empty on purpose, bound to app later via init_app()
db = SQLAlchemy()
# Example usage in app factory (app.py):
