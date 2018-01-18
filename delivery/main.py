from thalia.show import Show, ShowInfo
from thalia.theater import Theater
from thalia.order import Ticket, Order, Patron
from thalia.report import RevenueReport, OccupancyReport, DonatedReport
from thalia.donate import Donate
""" holds all the classes made by the rest"""


class Thalia:
    def __init__(self):
        self.shows_list = list()
        self.tickets_list = list()
        self.orders_list = list()
        self.donated = list()
        self.donors = list()

    @staticmethod
    def get_seating(sid=None):
        if sid is not None:
            return get_specific(sid, Theater().get_seating())
        return Theater()

    def get_reports(self, mrid=None, show=list(), start=None, end=None):
        r, o, d = RevenueReport(), OccupancyReport(), DonatedReport()
        sr = self.shows_list
        if show:
            sr = list()
            for s in show:
                sr.append(self.get_shows(wid=s))
        elif start and end:
            # TODO: create reports for a start and end time
            pass
        if mrid:
            if mrid == r.get_id():
                return RevenueReport(shows=sr)
            if mrid == o.get_id():
                return OccupancyReport(shows=sr)
            if mrid == d.get_id():
                return DonatedReport(shows=sr)
        return [o, r, d]

    def get_tickets(self, tid=None):
        if tid:
            return get_specific(tid, self.tickets_list)
        return self.tickets_list

    def get_orders(self, oid=None):
        if oid:
            return get_specific(oid, self.orders_list)
        return self.orders_list

    def order_by_date(self, start='20000220', end='22000220'):
        orders = list()
        for o in self.orders_list:
            if o.check_date(start=start, end=end):
                orders.append(o)
        return orders

    def get_shows(self, wid=None):
        if wid:
            return get_specific(wid, self.shows_list)
        return self.shows_list

    def get_show_section_by_id(self, wid=0, sid=0):
        show = self.get_shows(wid=wid)
        return show, sid

    def post_get_donations(self, patron=None, amount=0, wid=0):
        patron = Patron(name=patron['name'], phone=patron['phone'], email=patron['email'],
                        cc_exp=patron['cc_expiration_date'],
                        cc_num=patron['cc_number'], bill_add=patron['billing_address'])
        donor = Donate(patron=patron, amount=amount, wid=wid)
        self.donors.append(donor)
        return donor

    def get_donations_by_id(self, wid=0, did=0):
        for donor in self.donors:
            self.donated = donor.take_tickets(self.donated)
        if did is not None:
            donor = get_specific(did, self.donors)
            return donor

    def post_show(self, show_info=None, seating=None):
        """post thalia/show/"""
        if show_info and seating:
            theater = Theater()
            theater.update_seating(seating)
            new_info = ShowInfo(name=show_info['name'], web=show_info['web'], date=show_info['date'],
                                time=show_info['time'])
            new_show = Show(show_info=new_info, seating_info=theater)
            self.shows_list.append(new_show)
            return new_show
        return None

    def put_show(self, wid, show_info=None, seating=None):
        """put show, updates and returns nothing"""
        if show_info and seating:
            show = get_specific(wid, self.shows_list)
            if show is not None:
                self.shows_list.remove(show)
                show.set_show_info(show_info)
                theater = Theater()
                theater.update_seating(seating)
                show.set_seating(theater)
                self.shows_list.append(show)
        return None

    def post_ticket(self, tid=None, status="used"):
        # TODO: check if status is already set to used, return error
        if tid:
            ticket = get_specific(tid, self.tickets_list)
            ticket.set_status(status)
            return ticket

    def post_donate(self, tid_list=list()):
        for t in self.tickets_list:
            if t.get_id() in tid_list:
                t.set_status("donated")
                self.donated.append(t)
                return t

    def post_order(self, wid=None, sid=None, seats=None, patron=None):
        patron = Patron(name=patron['name'], phone=patron['phone'], email=patron['email'], cc_num=patron['cc_number'],
                        cc_exp=patron['cc_expiration_date'], bill_add=patron['billing_address'])
        show = self.get_shows(wid)
        cids = list(map(lambda x: x['cid'], seats))
        show.get_seating().find_section(sid).buy_seats(cids)
        s = self.get_show_section_by_id(wid, sid)
        tickets = list(map(lambda x: Ticket(wid=wid, sid=sid, seat=x['seat'], cid=x['cid'], price=s['price']), seats))
        order = Order(wid=wid, tickets=tickets, patron=patron)
        list(map(lambda t: self.tickets_list.append(t), tickets))
        self.orders_list.append(order)
        return order

    def show_seats_request(self, wid=0, sid=0, count=1, start_id=None):
        show = get_specific(wid, self.shows_list)
        section = show.get_seating().find_section(sid)
        return section.find_seats(req_num=count, start_id=start_id)

    def search(self, topic, key):
        """Iterates through all of the lists looking for the topic and key"""
        search_list = list()
        if topic and key:
            for attr, value in self.__dict__.items():
                for v in value:
                    s = v.search(topic, key)
                    if s:
                        search_list.append(s)
        return search_list


def get_specific(id=0, obj_list=list()):
    """finds specified object specified by id"""
    for obj in obj_list:
            if obj.check_id(id):
                return obj
