from models.karyawan import Karyawan

class KaryawanController:
    def __init__(self, db_construct):
        self.db = db_construct


    def get_all_karyawan(self, name=None):
        karyawan_list = []
        karyawan_data = self.db.session.query(Karyawan).all() # = select * from karyawan
        for result in karyawan_data:
            karyawan_list.append({'id': result.id, 'nama': result.nama,'umur': result.umur,'alamat': result.alamat})
        return karyawan_list

    def save_karyawan_new(self,**data):
        kar = Karyawan()
        for key, value in data.items():
            setattr(kar, key, value)
        self.db.session.add(kar)
        self.db.session.commit()

    def get_edit_karyawan(self,id):
        karyawan_data = self.db.session.query(Karyawan).filter(Karyawan.id ==id).first()
        return karyawan_data

    def update_karyawan(self,id,**data):
        karyawan_data = self.db.session.query(Karyawan).filter(Karyawan.id == id).first()
        for key, val in data.items():
             setattr(karyawan_data, key, val)
        self.db.session.commit()

    def delete_karyawan(self,id):
        karyawan_data = self.db.session.query(Karyawan).get(id)
        self.db.session.delete(karyawan_data)
        self.db.session.commit()






