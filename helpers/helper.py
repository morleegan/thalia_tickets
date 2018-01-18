import uuid
import re

#
# class Helper:
#     @staticmethod
#     def delete_keys(dic=dict(), key_list=list()):
#         for key in key_list:
#             if key in dic.keys():
#                 del dic[key]
#         return dic


class ID:
    def __init__(self, new_id=None):
        self.id = uuid.uuid4().hex if not new_id else new_id

    def get_id(self):
        return self.id

    def set_id(self, o_id):
        self.id = o_id

    def check_id(self, o_id):
        if str(self.id) == str(o_id):
            return True
        return False

    def search(self, topic, key):
        if re.search(str(topic), str(self.__class__), re.I):
            reg = str(key)
            for attr, value in self.__dict__.items():
                if re.search(reg, attr, re.I):
                    return self
                if isinstance(value, ID):
                    if value.search(topic, key) == value:
                        return self
                if re.search(reg, str(value), re.I):
                    return self

