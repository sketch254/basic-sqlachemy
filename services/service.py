from extension import db
from models.profile import Profile
from models.user import User

def save(obj):
    db.session.add(obj) # staged only, nothing sent yet
    try:
        db.session.commit() # flush, then end transaction
    except Exception:
        db.session.rollback() # required to reuse session
        raise
    return obj


def fetch(Model, pk_value):
    return db.session.get(Model, pk_value) # obj or None


def remove(obj):
    db.session.delete(obj) # same try / commit / rollback
