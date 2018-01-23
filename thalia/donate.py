from thalia.id import ID
from thalia.order import Patron


class Donate(ID):
    def __init__(self, wid=0, amount=1, patron=Patron()):
        ID.__init__(self)
        self.__patron = patron
        self.__wid = wid
        self.__amount = amount
        self.__tickets = list()
        self.__status = "pending"

    def get_patron(self):
        return self.__patron

    def get_wid(self):
        return self.__wid

    def get_tickets(self):
        return self.__tickets

    def get_amount(self):
        return self.__amount

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def take_tickets(self, tickets):
        for t in tickets:
            if len(self.get_tickets()) == self.get_amount():
                break
            if t.get_wid() == self.get_wid():
                self.set_status("assigned")
                self.get_tickets().append(t)
                tickets.remove(t)
        return tickets
