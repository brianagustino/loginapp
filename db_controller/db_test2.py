from models.test2 import Test2

class Test2Controller:
    def __init__(self , db_constructor):
        self.db = db_constructor

    def get_all_test2(self):
        test2_list = []
        test2_data = self.db.session.query(Test2).all()
        for data in test2_data:
            test2_list.append({"id":data.id , "keterangan":data.keterangan})
        return test2_list