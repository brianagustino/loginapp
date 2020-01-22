from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Karyawan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(25), unique=True, nullable=False)
    umur = db.Column(db.String(120), unique=True, nullable=True)
    alamat = db.Column(db.String(120), unique=True, nullable=True)

    # def __repr__(self):
    #     return '<User %r>' % self.nama


