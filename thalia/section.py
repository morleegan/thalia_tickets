from thalia.row import Row
from helpers.helper import ID


class Section(ID):
    """Section class: holds seats and row values"""
    def __init__(self, sid=None, price=None, rows=list(), name=None):
        """Initialization of Section Class"""
        ID.__init__(self, sid)
        self.__name = name
        self.__price = price
        self.__rows = list()
        self.__bought_seats = 0
        self.__seats_total = 0
        self.create_section(rows)

    def get_total_seats(self):
        return self.__seats_total

    def get_bought_seats(self):
        return self.__bought_seats

    def get_name(self):
        return self.__name

    def get_rows(self):
        return self.__rows

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def get_revenue(self):
        return self.__bought_seats * self.get_price()

    def get_seats_available(self):
        return self.__seats_total - self.__bought_seats

    def create_section(self, rows):
        if not self.__rows:
            row_list = list()
            for r in rows:
                # iterates through a list of dicts
                r_created = Row(row=r['row'], seats=r['seats'])
                row_list.append(r_created)
                self.__seats_total += len(r_created.get_seats_as_list())
            self.__rows = row_list

    def find_seats(self, start_id=None, req_num=1):
        for row in self.get_rows():
            return row.find_seats(start_id=start_id, req_num=req_num)

    def buy_seats(self, cid_list):
        for row in self.get_rows():
            row.order_seats(cid_list=cid_list)
        self.__bought_seats += len(cid_list)

    def to_dict(self):
        return {
            "sid": self.get_id(),
            "section_name": self.get_name(),
            "price": self.get_price(),
            "seating": list(map(lambda x: x.to_dict(), self.get_rows())) if self.get_rows() else list()
        }

    def report(self):
        return {
            "sid": self.get_id(),
            "section_name": self.get_name(),
            "section_price": self.get_price(),
            "seats_available": self.get_seats_available(),
            "seats_sold": self.__bought_seats,
            "section_revenue": self.get_revenue()
        }