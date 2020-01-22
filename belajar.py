from flask import Flask,flash, render_template, request, redirect , session
import os, json
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask import Flask, current_app, jsonify, make_response, request

from db_controller.db_karyawan import KaryawanController
from db_controller.db_test import TestController
from db_controller.db_test2 import Test2Controller
from db_controller.db_barang import BarangController
from db_controller.db_user import UserController

import hashlib

app = Flask(__name__)
config = {
    "lokal": "config.LocalConfig",
    "development": "config.DevelopmentConfig",
    "production":"config.ProductionConfig"
}
api = Api(app)
config_name = os.getenv('APP_CONFIG', 'lokal')
app.config.from_object(config[config_name])
APP_PORT = app.config['APP_PORT']
BASE_API_URL = app.config['BASE_API_URL']
DB_URL = app.config['DB_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "sip"
db = SQLAlchemy(app)

@app.route("/login")
def get_login():
    return render_template("login/login.html")

@app.route("/logout")
def get_logout():
    session['loggedin'] = False
    session['username'] = ""
    session['level'] = ""
    return redirect("/login")

@app.route("/post_login" , methods=['POST'])
def post_login():
    _username = request.form['username']
    _password = request.form['password']
    h = hashlib.md5(_password.encode())
    _password = h.hexdigest()
    user = UserController(db)
    checklogin = user.login(_username , _password)
    if checklogin is not None:
        session['loggedin'] = True
        session['username'] = checklogin.username
        session['level'] = checklogin.level
        return redirect("/")
    else:
        return redirect('/login')

@app.route("/register")
def register_user():
    return render_template("login/register.html")

@app.route("/post_register" , methods=['POST'])
def post_register():
    _username = request.form['username']
    _password = request.form['password']
    _level = request.form['level']
    h = hashlib.md5(_password.encode())
    _password = h.hexdigest()
    user = UserController(db)
    user.register(_username , _password , _level)
    return redirect('/login')

@app.route("/forgetpassword")
def forgetpassword():
    return render_template("login/loggededitpassword.html")

@app.route("/edit_password" , methods=['POST'])
def editpassword():
    _password = request.form['password']
    _repassword = request.form['repassword']
    print(_password)
    if _password == _repassword:
        h = hashlib.md5(_password.encode())
        _password = h.hexdigest()
        print(_password)
        user = UserController(db)
        user.forgetpassword(session['username'] , _password)
        return redirect('/login')
    else:
        return redirect('/forgetpassword')

@app.route ('/forgetoutpassword')
def forgetoutpassword():
    return render_template('login/loggedoutpassword.html')

@app.route('/outedit_password' , methods=['POST'])
def outedit_password():
    _username = request.form['username']
    _password = request.form['password']
    _repassword = request.form['repassword']
    table = UserController(db)
    data = table.get_username()
    print(data)
    checkcondition = False
    for bebas in data:
        if _username == bebas["username"]:
            checkcondition = True

    if _password == _repassword and checkcondition:
        h = hashlib.md5(_password.encode())
        _password = h.hexdigest()
        user = UserController(db)
        user.forgetpassword(_username , _password)
        return redirect('/login')
    else:
        return redirect('/forgetoutpassword')



@app.route("/test2")
def get_test2():
    table = Test2Controller(db)
    data = table.get_all_test2()
    return render_template("test2.html" , bebas = data)

@app.route("/stokbarang")
def get_stockbarang():
    if session.get('loggedin') == True:
        table = BarangController(db)
        data = table.get_all_stok()
        return render_template("barang/stok.html" , bebas = data)
    else:
        return redirect('/login')

@app.route("/stokbarang/add")
def add_stockbarang():
    if session.get('loggedin') == True:
        table = BarangController(db)
        datas = table.get_all_barang()
        return render_template("barang/addstok.html" , bebas = datas)
    else:
        return redirect('/login')

@app.route('/stokbarang/edit/<int:stock_id>')
def edit_stokbarang(stock_id):
    if session.get('loggedin') == True:
        table = BarangController(db)
        datastok = table.get_all_stok()
        databarang = table.get_all_barang()
        datasatuan = table.get_all_satuan()
        data = table.edit_all_stok(stock_id)
        print(data)
        return render_template('barang/editstok.html' , bebas = data, satuan=datasatuan , barang=databarang , stok=datastok)
    else:
        return redirect('/login')

@app.route('/update_stok' , methods = ['POST'])
def update_stok():
    if session.get('loggedin') == True:
        _id = request.form['id']
        _barang = request.form['barang']
        _jumlah = request.form['jumlah']
        data = {
            "id_barang": _barang,
            "jumlah": _jumlah
        }

        table = BarangController(db)
        table.update_stok(id=_id,**data)
        return redirect('/stokbarang')
    else:
        return redirect('/login')

@app.route('/save_stok' , methods = ['POST'])
def save_stockbarang():
    if session.get('loggedin') == True:
        _namabarang = request.form['barang']
        _jumlah = request.form["jumlah"]
        _keterangan = request.form['keterangan']
        table = BarangController(db)
        table.save_all_stok(_namabarang , _jumlah , _keterangan)
        return redirect('/stokbarang')
    else:
        return redirect('/login')

@app.route('/stokbarang/delete/<int:stock_id>')
def delete_stok(stock_id):
    if session.get('loggedin') == True:
        table = BarangController(db)
        table.delete_stok(stock_id)
        return redirect('/stokbarang')
    else:
        return redirect('/login')

@app.route("/barang")
def get_barang():
    if session.get('loggedin') == True:
        table = BarangController(db)
        data = table.get_all_barang()
        return render_template('barang/barang.html', bebas = data)
    else:
        return redirect('/login')

@app.route('/barang/add')
def add_barang():
    if session.get('loggedin') == True:
        table = BarangController(db)
        data = table.get_all_satuan()
        return render_template("barang/addbarang.html" , bebas = data)
    else:
        return redirect('/login')

@app.route('/save_barang' , methods = ['POST'])
def save_barang():
    if session.get('loggedin') == True:
        _namabarang = request.form['barang']
        _satuan = request.form['satuan']
        _keterangan = request.form['keterangan']

        table = BarangController(db)
        table.save_all_barang(_namabarang , _satuan , _keterangan)
        print("suksess")
        return redirect('/barang')
    else:
        return redirect('/login')


@app.route('/satuan')
def get_satuan():
    if session.get('loggedin') == True:
        table = BarangController(db)
        data = table.get_all_satuan()
        return render_template("barang/satuan.html" , bebas = data)
    else:
        return redirect('/login')

@app.route('/satuan/add')
def add_satuan():
    if session.get('loggedin') == True:
        return render_template("barang/addsatuan.html")
    else:
        return redirect('/login')

@app.route('/save_satuan' , methods = ['POST'])
def save_satuan():
    if session.get('loggedin') == True:
        #_satuanid = request.form['satuan_id']
        _satuan = request.form['satuan']
        _keterangan = request.form['keterangan']
        table = BarangController(db)
        table.save_all_satuan( _satuan , _keterangan)
        return redirect('/satuan')
    else:
        return redirect('/login')


@app.route("/test")
def get_test():
    if session.get('loggedin') == True:
        table = TestController(db)
        data = table.get_all_test()
        return render_template("test.html" , bebas = data)
    else:
        return redirect('/login')


@app.route('/')
def index():
    if session.get('loggedin') == True:
        return render_template('index.html')
    else:
        return redirect('/login')

@app.route('/karyawan')
def karyawan():
    table = KaryawanController(db)
    data = table.get_all_karyawan()
    return render_template('karyawan/karyawan.html',datanya=data)

@app.route('/karyawan/add')
def add_karyawan():
    return render_template('karyawan/add.html')

@app.route('/siswa/add')
def add_siswa():
    return render_template("siswa/add.html")

@app.route('/save_karyawan', methods=['POST'])
def save_karyawan():
    _nama = request.form['nama']
    _umur = request.form['umur']
    _alamat = request.form['alamat']
    table = KaryawanController(db)
    table.save_karyawan_new(nama =_nama, alamat =_alamat, umur=_umur)
    return redirect('/karyawan')

@app.route('/save_siswa' , methods=['POST'])
def save_siswa():
    _nama = request.form['nama']
    _umur = request.form['umur']
    _kelamin = request.form['kelamin']
    _agama = request.form['agama']
    _alamat = request.form['alamat']
    _email = request.form['email']
    _kelas = request.form['kelas']
    _nilai = request.form['nilai']
    _lulus = request.form['lulus']
    table = SiswaController(db)
    table.save_siswa_new(nama = nama, umur = umur, kelamin = kelamin, agama = agama, alamat = alamat , email = email , kelas = kelas , nilai = nilai , lulus = lulus)
    return redirect('/siswa')

@app.route('/karyawan/edit/<int:id>')
def edit_view(id):
    table = KaryawanController(db)
    data = table.get_edit_karyawan(id)
    return render_template("karyawan/edit.html",data=data)

@app.route('/siswa/edit/<int:id>')
def edit_view_siswa(id):
    table = SiswaController(db)
    data = table.get_siswa_edit(id)
    return render_template("siswa/edit.html" , data=data)

@app.route('/karyawan/delete/<int:id>')
def delete_view(id):
    table = KaryawanController(db)
    table.delete_karyawan(id)
    return redirect('/karyawan')

@app.route('/siswa/delete/<int:id>')
def delete_view_siswa(id):
    table = SiswaController(db)
    table.delete_siswa(id)
    return redirect('siswa')

@app.route('/update_karyawan', methods=['POST'])
def update_karyawan():
    _id = request.form['id']
    _nama = request.form['nama']
    _umur = request.form['umur']
    _alamat = request.form['alamat']
    datas = {
         "nama":_nama,
         "umur":_umur,
         "alamat":_alamat
    }
    table = KaryawanController(db)
    table.update_karyawan(id =_id,**datas)
    return redirect('/karyawan')


class KaryawanPostApi(Resource):
    def post(self):
        _nama = request.form['nama']
        _umur = request.form['umur']
        _alamat = request.form['alamat']
        table = KaryawanController(db)
        table.save_karyawan_new(nama=_nama, alamat=_alamat, umur=_umur)

api.add_resource(KaryawanPostApi, BASE_API_URL + '/karyawan/post')

class KaryawanApi(Resource):
    def get(self):
        table = KaryawanController(db)
        data = table.get_all_karyawan()
        return make_response(json.dumps(data), 200)
api.add_resource(KaryawanApi, BASE_API_URL + '/karyawan/list')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))

    app.run(host="0.0.0.0", debug=True, port=APP_PORT, threaded=True)
