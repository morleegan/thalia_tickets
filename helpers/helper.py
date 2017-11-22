import uuid

class Helper:
    @staticmethod
    def delete_keys(dic=dict(), key_list=list()):
        for key in key_list:
            if key in dic.keys():
                del dic[key]
        return dic

    @staticmethod
    def get_specific(wid=0, obj_list=list()):
        for obj in obj_list:
            if obj.check_id(wid):
                return obj


class ID:
    def __init__(self):
        self.id = uuid.uuid4().hex

    def get_id(self):
        return self.id

    def set_id(self, o_id):
        self.id = o_id

    def check_id(self, o_id):
        if str(self.id) == str(o_id):
            return True
        return False

