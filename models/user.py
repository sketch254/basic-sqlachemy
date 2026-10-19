from extension import db


class User(db.Model):
    __tablename__ = "users" # Always explicit

    # Primary Key & Column Definitions
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

    # Options: nullable, unique, default, index

    # how to relate to the profile
    profile = db.relationship(
        "Profile", 
        uselist=False,
        back_populates= "user")

    def __repr__(self):
        return f"<User {self.id}: {self.first_name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
