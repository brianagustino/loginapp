from models.test import Test

class TestController:
    def __init__(self, db_constructor):
        self.db = db_constructor

    def get_all_test(self):
        test_list = []
        test_data = self.db.session.query(Test).all()
        for data in test_data:
            test_list.append({"id":data.id , "keterangan":data.keterangan})
        return test_list

