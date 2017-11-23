from helpers.helper import ID


class Donate(ID):
    def __init__(self, wid=0, amount=1, patron=None):
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

    def to_dict(self):
        pat = self.get_patron().to_dict()
        pat['cc_number'] = self.get_patron().get_cc_num()
        return {
                "did": self.get_id(),
                "wid": self.get_wid(),
                "count": self.get_amount(),
                "status": self.get_status(),
                "tickets": list(map(lambda x: x.get_id(), self.get_tickets())),
                "patron_info": pat}
