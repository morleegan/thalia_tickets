from helpers.helper import ID
from datetime import datetime


class Report(ID):
    def __init__(self, new_id=str(800), start=None, end=None, name='Reporter', shows=list()):
        ID.__init__(self, new_id=new_id, )
        self.__name = name
        self.__start_date = datetime.strptime(start, '%Y%m%D') if start else None
        self.__end_date = datetime.strptime(end, '%Y%m%D') if end else None
        self.__shows = shows

    def get_name(self):
        return self.__name

    def to_dict(self):
        return {
            "mrid": self.get_id(),
            "name": self.get_name()
        }


class OccupancyReport(Report):
    def __init__(self, ):
        Report.__init__(self, new_id='801', name='Theatre occupancy')


class RevenueReport(Report):
    def __init__(self):
        Report.__init__(self, new_id='802', name="Revenue from ticket sales")


class DonatedReport(Report):
    def __init__(self):
        Report.__init__(self, new_id='803', name="Donated tickets report")

