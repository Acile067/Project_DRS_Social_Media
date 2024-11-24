from email.policy import default
import uuid
from app.app import db
from sqlalchemy import Column, Integer, String


class Post(db.Model):
    __tablename__ = 'posts'

    ID = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    Username = db.Column(db.String(255), nullable=False)
    Txt = db.Column(db.String(255), nullable=True)
    ImagePath = db.Column(db.String(255), nullable=True)
    Approved = db.Column(db.String(255), nullable=False, default="no")


    def __repr__(self):
        return  f"<Username {self.Username}>"

    def get_id(self):
        return self.ID