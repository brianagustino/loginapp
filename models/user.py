from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(15) , unique=True , nullable=False)
    password = db.Column(db.String(50) , unique = False , nullable = False)
    level = db.Column(db.String(15) , unique = False , nullable = False)