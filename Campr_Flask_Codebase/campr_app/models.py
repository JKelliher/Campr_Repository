from campr_app import db

db.Model.metadata.reflect(db.engine)

# to-do: 14:38 video, make relationship between Campsites and users
class CampSites(db.Model):
    __table__ = db.Model.metadata.tables['CampSites']

    def __repr__(self):
        return f"Campsite('{self.site_name}', '{self.gps}', '{self.city}')"