from helpers.helper import ID
from datetime import datetime


class Report(ID):
    def __init__(self, new_id=str(800), start=None, end=None, name='Reporter', shows=list()):
        ID.__init__(self, new_id=new_id, )
        self.__name = name
        self.__start_date = datetime.strptime(start, '%Y%m%D') if start else None
        self.__end_date = datetime.strptime(end, '%Y%m%D') if end else None
        self.__shows = shows
        self.__total_seats = 0
        self.__total_sold = 0

    def get_name(self):
        return self.__name

    def get_shows(self):
        return self.__shows

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def set_shows(self, shows):
        self.__shows = shows

    def get_total_seats(self):
        return self.__total_seats

    def get_total_sold(self):
        return self.__total_sold

    def calculate_totals(self):
        self.__total_sold = 0
        self.__total_seats = 0
        for show in self.get_shows():
            show.calculate_totals()
            self.__total_seats += show.get_total_seats()
            self.__total_sold += show.get_sold_total()


class OccupancyReport(Report):
    def __init__(self, shows=list()):
        Report.__init__(self, new_id='801', name='Theatre occupancy', shows=shows)
        self.__occupancy = 0
        self.calculate_report()

    def calculate_report(self):
        self.calculate_totals()
        self.__occupancy = self.get_total_sold() / self.get_total_seats() if self.get_total_seats() > 0 else 0

    def get_occupancy(self):
        return self.__occupancy

    def report(self):
        self.calculate_report()
        return {
            "mrid": self.get_id(),
            "name": self.get_name(),
            "total_shows": len(self.get_shows()),
            "total_seats": self.get_total_seats(),
            "sold_seats": self.get_total_sold(),
            "overall_occupancy": str(self.get_occupancy() * 100)[:4] + '%',
            "shows": list(map(lambda s: {
                "wid": s.get_id(),
                "show_info": s.get_show_info() if isinstance(s.get_show_info(), dict) else s.get_show_info().to_dict(),
                "seats_available": s.get_total_seats() - s.get_sold_total(),
                "seats_sold": s.get_sold_total(),
                "occupancy": str((s.get_sold_total() / s.get_total_seats()) * 100)[:4] + '%' if s.get_total_seats() > 0 else 0
            }, self.get_shows()))
        }


class RevenueReport(Report):
    def __init__(self, shows=list()):
        Report.__init__(self, new_id='802', name="Revenue from ticket sales", shows=shows)
        self.__revenue = 0
        self.calculate_report()

    def get_rev(self):
        return self.__revenue

    def calculate_report(self):
        self.calculate_totals()
        self.__revenue = 0
        for show in self.get_shows():
            for sec in show.get_seating().get_seating():
                self.__revenue += sec.get_revenue()


class DonatedReport(Report):
    def __init__(self, shows=list()):
        Report.__init__(self, new_id='803', name="Donated tickets report", shows=shows)


