from campr_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db.Model.metadata.reflect(db.engine)

# to-do: 14:38 video, make relationship between Campsites and users
class CampSites(db.Model):
    __table__ = db.Model.metadata.tables['CampSites']

    def __repr__(self):
        return f"Campsite('{self.site_name}', '{self.gps}', '{self.city}')"

class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.email}')"