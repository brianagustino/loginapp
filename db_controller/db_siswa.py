from models.siswa import Siswa

class SiswaController(db_controller):
    def __init__(self , db_construct):
        self.db = db_construct

    def get_all_siswa(self):
        siswa_list = []
        siswa_data = self.db.session.query(Siswa).all()
        for result in siswa_data:
            siswa_list.append({"id":result.id , "nama":result.nama , "umur":result.umur , "kelamin":result.kelamin , "agama":result.agama , "alamat":result.alamat , "email":result.email , "kelas":result.kelas , "nilai":result.nilai , "lulus":result.lulus})
        return siswa_list

    def save_siswa_new(self, **data):
        sis = Siswa()
        for key , value in data.items:
            setattr(sis , key , value)
        self.db.session.add(sis)
        self.db.session.commit()

    def get_siswa_edit(self):
        siswa_data = self.db.session.query(Sisa).filter(Siswa.id == id).first()
        return siswa_data

    def update_siswa(self):
        siswa_data = self.db.session.query(Siswa).filter(Siswa.id == id).first()
        for key , val in data.items():
            setattr(siswa_data , key , val)
        self.db.session.commit()

    def delete_siswa(self):
        siswa_data = self.db.session.query(Siswa).get(id)
        self.db.session.delete(siswa_data)
        self.db.session.commit()