from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    img_url = db.Column(db.String(1000))
    
    def __repr__(self):
        p = self
        return f"<User id={p.id} first_name={p.first_name} Last Name={p.last_name} Image Url={p.img_url}>"