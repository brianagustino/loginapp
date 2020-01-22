from models.user import User
from flask import session
import hashlib

class UserController():
    def __init__(self , db_construct):
        self.db = db_construct

    def get_username(self):
        datalist = []
        data = self.db.session.query(User).all()
        for result in data:
            datalist.append({"username": result.username , "password": result.password})
        return datalist

    def login(self , username , password):
        login = self.db.session.query(User).filter(User.username == username , User.password == password).first()
        return login

    def register(self , username , password , level):
        user = User()
        setattr(user , "username" , username)
        setattr(user , "password" , password)
        setattr(user , "level" , level)
        self.db.session.add(user)
        self.db.session.commit()

    def forgetpassword(self , username , password):
        user_data = self.db.session.query(User).filter(User.username == username).first()
        setattr(user_data , "username" , username)
        setattr(user_data , "password" , password)
        self.db.session.commit()


