from flask_sqlaclchemy import SQLAlchemy

db = SQLAlchemy()

class Siswa(db.Models):
    id = db.Column(db.Integer , primary_key=True)
    umur = db.Column(db.Integer , nullable = True)
    umur = db.Column(db.Integer, unique=False, nullable=True)
    kelamin = db.Column(db.String(1), nullable=True)
    agama = db.Column(db.String(25), nullable=True)
    alamat = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), unique=True, nullable=True)
    kelas = db.Column(db.Integer, nullable=True)
    nilai = db.Column(db.Integer, nullable=True)
    lulus = db.Column(db.String(1), nullable=True)
