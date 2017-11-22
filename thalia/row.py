import uuid


class Row:
    """Row Class: linked list implementation"""

    def __init__(self, row=None, seats=list()):
        self.__row = row                # row number
        self.__seats = None             # list of seats
        self.create_row(seats)          # creation of row

    def get_name(self):
        return self.__row

    def get_seats(self):
        return self.__seats

    def get_seats_as_list(self):
        seat_list = []
        r = self.get_seats()
        while r.r_seat is not None:
            seat_list.append(r)
            r = r.r_seat
        seat_list.append(r)
        return seat_list

    def create_row(self, seat_list):
        """Creation of the linked list"""
        for s in seat_list:
            seat = Seat(seat=s)
            if self.__seats is None:
                self.__seats = seat
            else:
                seat.r_seat = self.__seats
                seat.r_seat.l_seat = seat
                self.__seats = seat

    def search_row(self, cid):
        """find cid in the row"""
        r = self.get_seats()
        if r is not None:
            while r.r_seat is not None:
                if r.get_cid() == cid:
                    return r
                r = r.r_seat
            if r.get_cid() == cid:
                return r
        return None

    def order_seats(self, cid_list):
        """give order_seats a list of cids in the row, buys them"""
        for cid in cid_list:
            seat = self.search_row(cid)
            seat.bought_seat()

    def find_seats(self, start_id=None, req_num=1):
        """creates a order of seats for a num requested"""
        order = list()
        if start_id:
            r = self.search_row(start_id)
        else:
            r = self.get_seats()

        while r.r_seat is not None:
            if r.check_availability():
                order.append(r)
                if len(order) == req_num:
                    return order
            else:
                order = list()
            r = r.r_seat
        return None

    def to_dict(self):
        return {
            "row": self.get_name(),
            "seats": list(map(lambda x: x.to_dict(), self.get_seats_as_list()))
        }


class Seat:
    """Seat class: nodes of a linked list"""
    def __init__(self, seat=None):
        """Initializing Seat class: this is a single chair, created as a linked list"""
        self.__cid = uuid.uuid4().hex
        self.__name = seat
        self.l_seat = None
        self.r_seat = None
        self.__status = "available"

    def get_name(self):
        return self.__name

    def get_cid(self):
        return self.__cid

    def get_status(self):
        return self.__status

    def check_availability(self):
        """checks for seat availability """
        if self.__status == "available":
            return True
        return False

    def bought_seat(self):
        """change status to sold"""
        self.__status = "sold"

    def to_dict(self):
        return {
            "cid": self.get_cid(),
            "name": self.get_name(),
            "status": self.get_status()
        }
