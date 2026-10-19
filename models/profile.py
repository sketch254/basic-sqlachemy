from extension import db


class Profile(db.Model):
    __tablename__ = "profiles" # Always explicit

    # Primary Key & Column Definitions
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(80), nullable=False)


    # relationship column
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True)

    # Options: nullable, unique, default, index

    # how to relate to the user
    user = db.relationship(
        "User",
        back_populates = "profile"
    )


    def __repr__(self):
        return f"<Profile {self.id}: {self.first_name}>"
