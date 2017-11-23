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
        self.create_section(rows)

    def get_name(self):
        return self.__name

    def get_rows(self):
        return self.__rows

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def create_section(self, rows):
        if not self.__rows:
            row_list = list()
            for r in rows:
                # iterates through a list of dicts
                r_created = Row(row=r['row'], seats=r['seats'])
                row_list.append(r_created)
            self.__rows = row_list

    def find_seats(self, start_id=None, req_num=1):
        for row in self.get_rows():
            order = row.find_seats(start_id=start_id, req_num=req_num)
            if order is not None:
                return order

    def to_dict(self):
        return {
            "sid": self.get_id(),
            "section_name": self.get_name(),
            "price": self.get_price(),
            "seating": list(map(lambda x: x.to_dict(), self.get_rows())) if self.get_rows() else list()
        }