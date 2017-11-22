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

