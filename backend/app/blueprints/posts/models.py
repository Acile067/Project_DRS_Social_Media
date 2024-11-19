from app.app import db
from sqlalchemy import Column, Integer, String


class Post(db.Model):
    __tablename__ = 'posts'

    ID = db.Column(Integer, primary_key=True)
    Username = db.Column(db.String(255), nullable=False)
    Text = db.Column(db.String(255), nullable=False)
    ImagePath = db.Column(db.String(255), nullable=False)
    Approved = db.Column(db.String(255), nullable=False)


    #def __repr__(self):
        #return  f"<Username {self.Username}, Name: {self.Name}>"

    def get_id(self):
        return self.ID