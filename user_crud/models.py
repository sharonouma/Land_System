# models.py

from flask_login import UserMixin
from . import db

class TblUser(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    user_email = db.Column(db.String(100), unique=True)
    user_password = db.Column(db.String(100))
    user_name = db.Column(db.String(1000))
    phone_number = db.Column(db.String(1000))
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
   
    def get_id(self):
        return (self.user_id)
    
class TitleDeed(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    location = db.Column(db.String(100), unique=True)
    area = db.Column(db.Float)
    plot_number = db.Column(db.String(1000))
    serial_no = db.Column(db.String(1000))
    documentation_number = db.Column(db.String(1000))
    nature_of_title = db.Column(db.String(1000))
    Issue_date = db.Column(db.String(1000))
    owner_id = db.Column(db.Integer, db.ForeignKey('tbl_user.user_id'))
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    