import datetime

from helpers.helper import ID
from thalia.show import ShowInfo


class Order(ID):
    def __init__(self, wid=0, tickets=list(), patron=None):
        ID.__init__(self)
        self.__wid = wid
        self.__tickets = tickets
        self.__patron = patron
        self.__date_ordered = datetime.datetime.today()

    def get_wid(self):
        return self.__wid

    def get_tickets(self):
        return self.__tickets

    def get_patron(self):
        return self.__patron

    def get_date(self):
        return self.__date_ordered

    def check_date(self, start='20000220', end='20200220'):
        start_date = datetime.datetime.strptime(start, '%Y%m%d').date()
        end_date = datetime.datetime.strptime(end, '%Y%m%d').date()
        if start_date <= self.get_date().date() <= end_date:
            return True
        return False

    def get_total(self):
        total = 0
        for ticket in self.get_tickets():
            total += ticket.get_price()
        return total

    def to_dict(self):
        show = ShowInfo()
        return {
            "oid": self.get_id(),
            "wid": self.get_wid(),
            "show_info": show.to_dict(),
            "date_ordered": str(self.get_date())[:16],
            "order_amount": self.get_total(),
            "number_of_tickets": len(self.get_tickets()),
            "patron_info": self.get_patron().to_dict(),
            "tickets": list(map(lambda x: x.to_dict(), self.get_tickets())),

        }


class Ticket(ID):
    def __init__(self, price=0, wid=0, sid=0, cid=None, seat=None):
        ID.__init__(self)
        self.__wid = wid
        self.__sid = sid
        self.__cid = cid
        self.__seat = seat
        self.__price = price
        self.__status = "open"

    def get_wid(self):
        return self.__wid

    def get_sid(self):
        return self.__sid

    def get_cid(self):
        return self.__cid

    def get_seat(self):
        return self.__seat

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    def set_status(self, status="open"):
        self.__status = status

    def to_dict(self):
        return {"tid": self.get_id(),
                "price": self.get_price(),
                "status": self.get_status(),
                "cid": self.get_cid(),
                "seat": self.get_seat(),
                }


class Patron(ID):
    def __init__(self, name="", email="", phone="", bill_add="", cc_num="", cc_exp=""):
        ID.__init__(self)
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__bill_adr = bill_add
        self.__cc_num = cc_num
        self.__cc_exp = cc_exp

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_bill_adr(self):
        return self.__bill_adr

    def get_cc_num(self):
        return self.__cc_num

    def get_cc_exp(self):
        return self.__cc_exp

    def cover_cc(self):
        return 'xxxxxxxxxxxx' + self.get_cc_num()[12:]

    def to_dict(self):
        return {
            "name": self.get_name(),
            "phone": self.get_phone(),
            "email": self.get_email(),
            "billing_address": self.get_bill_adr(),
            "cc_number": self.cover_cc(),
            "cc_expiration_date": self.get_cc_exp()
        }