import uuid
import datetime

class Show:
    def __init__(self, show_info=None, seating_info=None):
        self.__wid = uuid.uuid4().hex
        self.__show_info = show_info
        self.__seating_info = seating_info

    def get_wid(self):
        return self.__wid

    def get_show_info(self):
        return self.__show_info

    def get_seating(self):
        return self.__seating_info

    def set_show_info(self, new_info):
        self.__show_info = new_info

    def set_seating(self, new_info):
        self.__seating_info = new_info

    def check_id(self, wid):
        if str(wid) == str(self.get_wid()):
            return True
        return False

    def to_dict(self):
        return {
            "wid": self.get_wid(),
            "show_info": self.get_show_info().to_dict() if not isinstance(self.get_show_info(),
                                                                          dict) else self.get_show_info(),
            "seating_info": self.get_seating().to_dict() if not isinstance(self.get_seating(),
                                                                           dict) else self.get_seating()
        }


class ShowInfo:
    def __init__(self, name=None, web=None, date=None, time=None):
        self.__name = name
        self.__web = web
        self.__date = datetime.datetime.strptime(date, '%Y-%m-%d').date() if date else datetime.date.today()
        self.__time = datetime.datetime.strptime(time, '%H:%M').time() if time else datetime.time()

    def get_name(self):
        return self.__name

    def get_web(self):
        return self.__web

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def set_all(self, name=None, web=None, date=None, time=None):
        self.__name = name
        self.__web = web
        self.__date = datetime.datetime.strptime(date, '%Y-%m-%d').date() if date else datetime.date.today()
        self.__time = datetime.datetime.strptime(time, '%H:%M').time() if time else datetime.time()

    def to_dict(self):
        return {
            "name": self.get_name(),
            "web": self.get_web(),
            "date": str(self.get_date()),
            "time": str(self.get_time())
        }