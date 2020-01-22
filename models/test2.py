from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Test2(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    keterangan = db.Column(db.String(255) , nullable = False)