from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Satuan(db.Model):
    satuan_id = db.Column(db.Integer , primary_key=True)
    nama_satuan = db.Column(db.String(15) , nullable=True)
    keterangan = db.Column(db.String(15) , nullable=True)

class Barang(db.Model):
    id_barang = db.Column(db.Integer , primary_key = True)
    nama_barang = db.Column(db.String(25) , nullable = False)
    satuan_id = db.Column(db.Integer , db.ForeignKey('satuan.satuan_id' , ondelete ='SET NULL') , nullable = True)
    satuan = db.relationship("Satuan" , foreign_keys=[satuan_id])
    keterangan = db.Column(db.String(15) , nullable=True)

class Stok(db.Model):
    stock_id = db.Column(db.Integer , primary_key=True)
    id_barang = db.Column(db.Integer , db.ForeignKey("barang.id_barang" , ondelete = 'SET NULL') , nullable = True)
    barang = db.relationship("Barang" , foreign_keys =[id_barang])
    jumlah =  db.Column(db.Integer , nullable = False , unique = False)
    keterangan = db.Column(db.String(15), nullable = True)