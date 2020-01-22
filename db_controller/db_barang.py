from models.barang import Stok , Barang , Satuan

class BarangController:
    def __init__(self, db_construct):
        self.db = db_construct

    def get_all_satuan(self):
        satuan_list = []
        satuan_data = self.db.session.query(Satuan).all()
        for data in satuan_data:
            satuan_list.append({"satuan_id":data.satuan_id , "nama_satuan":data.nama_satuan , "keterangan":data.keterangan})
        return satuan_list

    def save_all_satuan(self , nama_satuan , keterangan):
        satuanobject = Satuan()
        #setattr(satuan , satuan_id , "satuan_id")
        setattr(satuanobject , "nama_satuan" , nama_satuan)
        setattr(satuanobject , "keterangan" ,keterangan)
        self.db.session.add(satuanobject)
        self.db.session.commit()


    def get_all_barang(self):
        barang_list = []
        barang_data = self.db.session.query(Barang).all()
        for data in barang_data:
            barang_list.append({"id_barang":data.id_barang , "nama_barang":data.nama_barang , "nama_satuan":data.satuan.nama_satuan , "satuan_id":data.satuan.satuan_id , "keterangan":data.keterangan})
        return barang_list

    def save_all_barang(self , nama_barang , satuan_id , keterangan):
            barang = Barang()
            setattr(barang, "nama_barang", nama_barang)
            setattr(barang, "satuan_id", satuan_id)
            setattr(barang, "keterangan", keterangan)
            self.db.session.add(barang)
            self.db.session.commit()

    def get_all_stok(self):
        barang_list = []
        stok_barang = self.db.session.query(Stok).all()
        for data in stok_barang:
            barang_list.append({"stock_id":data.stock_id , "nama_barang":data.barang.nama_barang , "nama_satuan":data.barang.satuan.nama_satuan , "jumlah":data.jumlah})
        return barang_list

    def save_all_stok(self , id , jumlah , keterangan):
        stok = self.db.session.query(Stok).filter(Stok.id_barang == id).first()
        if stok:
            jumlahstok = int(stok.jumlah) + int(jumlah)
            setattr(stok , "jumlah" , jumlahstok)
            self.db.session.commit()

        else:
            stok = Stok()
            setattr(stok , "id_barang" , id)
            setattr(stok , "jumlah" , jumlah)
            setattr(stok , "keterangan" , keterangan)
            self.db.session.add(stok)
            self.db.session.commit()

    def edit_all_stok(self , id):
        stockdata = self.db.session.query(Stok).filter(Stok.stock_id == id).first()
        return stockdata

    def update_stok(self ,id,**data):
        stok = self.db.session.query(Stok).filter(Stok.stock_id == id).first()
        print(stok)
        for key, val in data.items():
             setattr(stok, key, val)
        self.db.session.commit()

    def delete_stok(self , id):
        stok = self.db.session.query(Stok).get(id)
        self.db.session.delete(stok)
        self.db.session.commit()