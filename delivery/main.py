from thalia.show import Show, ShowInfo
from thalia.theater import Theater
from thalia.order import Ticket, Order, Patron
from thalia.report import RevenueReport, OccupancyReport, DonatedReport
from helpers.helper import Helper
from thalia.donate import Donate

""" holds all the classes made by the rest"""


class Emulate:
    def __init__(self):
        self.shows_list = list()
        self.tickets_list = list()
        self.orders_list = list()
        self.donated = list()
        self.donors = list()

    @staticmethod
    def get_seating(sid=None):
        seating = Theater().get_seating()
        if sid is not None:
            sec = Helper.get_specific(sid, seating)
            return Helper.delete_keys(sec.to_dict(), ['price'])
        return list(map(lambda x: Helper.delete_keys(x.to_dict(), ['price', 'seating']), seating))

    @staticmethod
    def get_reports():
        r = RevenueReport()
        o = OccupancyReport()
        d = DonatedReport()
        reports = [o, r, d]
        return reports

    def get_tickets(self, tid=None):
        if tid is not None:
            ticket = Helper.get_specific(tid, self.tickets_list)
            return ticket.to_dict()

    def get_orders(self, oid=None):
        if oid is not None:
            order = Helper.get_specific(oid, self.orders_list)
            if order:
                show = self.get_shows(order.get_wid())
                show = show.to_dict()
                o_dict = order.to_dict()
                o_dict = Helper.delete_keys(o_dict, ['sid', 'number_of_tickets'])
                o_dict['tickets'] = list(map(lambda t: Helper.delete_keys(t, ['cid', 'seat', 'price']),
                                             o_dict['tickets']))
                o_dict['show_info'] = show['show_info']
                return o_dict
            return "does not exist"
        orders = list()
        for o in self.orders_list:
            for s in self.shows_list:
                if s.check_id(o.get_wid()):
                    o_dict = o.to_dict()
                    si_dict = s.get_show_info()
                    o_dict['show_info'] = si_dict
                    o_dict = Helper.delete_keys(o_dict, ['sid', 'tickets'])
                    orders.append(o_dict)
        return orders

    def order_by_date(self, start='20000220', end='22000220'):
        orders = list()
        for o in self.orders_list:
            if o.check_date(start=start, end=end):
                for s in self.shows_list:
                    if s.check_id(o.get_wid()):
                        o_dict = o.to_dict()
                        si_dict = s.get_show_info()
                        o_dict['show_info'] = si_dict
                        o_dict = Helper.delete_keys(o_dict, ['sid', 'tickets'])
                        orders.append(o_dict)
            return orders

    def get_shows(self, wid=None):
        if wid is not None:
            show = Helper.get_specific(wid, self.shows_list)
            return show if show else "does not exist"
        return list(map(lambda x: Helper.delete_keys(x.to_dict(), ['seating_info']), self.shows_list)) if \
            self.shows_list else list()

    def get_show_section(self, wid=0):
        show_dict = self.get_shows(wid=wid)
        show_dict = show_dict.to_dict()
        if show_dict == "does not exist":
            return show_dict
        sect = show_dict.get('seating_info', None)
        if sect:
            return list(map(lambda x: Helper.delete_keys(x, ['seating']), sect))
        return show_dict

    def get_show_section_by_id(self, wid=0, sid=0):
        show_sec = self.get_shows(wid=wid)
        show_sec = show_sec.to_dict()
        if show_sec == "does not exist":
            return show_sec
        seating = show_sec.get('seating_info')
        for sec in seating:
            if sec["sid"] == str(sid):
                s = {"wid": wid, "show_info": show_sec.get('show_info')}
                s.update(sec)
                return s

    def post_get_donations(self, patron=None, amount=0, wid=0):
        patron = Patron(name=patron['name'], phone=patron['phone'], email=patron['email'],
                        cc_exp=patron['cc_expiration_date'],
                        cc_num=patron['cc_number'], bill_add=patron['billing_address'])
        donor = Donate(patron=patron, amount=amount, wid=wid)
        self.donors.append(donor)
        return {"did": donor.get_id()}

    def get_donations_by_id(self, wid=0, did=0):
        for donor in self.donors:
            self.donated = donor.take_tickets(self.donated)
        if did is not None:
            donor = Helper.get_specific(did, self.donors)
            return donor.to_dict()

    def post_show(self, show_info=None, seating=None):
        """post thalia/show/"""
        if show_info and seating:
            theater = Theater()
            theater.update_seating(seating)
            new_info = ShowInfo(name=show_info['name'], web=show_info['web'], date=show_info['date'],
                                time=show_info['time'])
            new_show = Show(show_info=new_info, seating_info=theater)
            self.shows_list.append(new_show)
            return {"wid": new_show.get_id()}
        return None

    def put_show(self, wid, show_info=None, seating=None):
        """put show"""
        if show_info and seating:
            show = Helper.get_specific(wid, self.shows_list)
            if show is None:
                return "not a show"
            self.shows_list.remove(show)
            show.set_show_info(show_info)
            theater = Theater()
            theater.update_seating(seating)
            show.set_seating(theater)
            self.shows_list.append(show)

    def post_ticket(self, tid=None, status="used"):
        if tid:
            ticket = Helper.get_specific(tid, self.tickets_list)
            ticket.set_status(status)
            return {"tid": tid, "status": ticket.get_status()}
        return "does not exist"

    def post_donate(self, tid_list=list()):
        for t in self.tickets_list:
            if t.get_id() in tid_list:
                t.set_status("donated")
                self.donated.append(t)
        return "does not exist"

    def post_order(self, wid=None, sid=None, seats=None, patron=None):
        patron = Patron(name=patron['name'], phone=patron['phone'], email=patron['email'], cc_num=patron['cc_number'],
                        cc_exp=patron['cc_expiration_date'], bill_add=patron['billing_address'])
        s = self.get_show_section_by_id(wid, sid)
        tickets = list(map(lambda x: Ticket(wid=wid, sid=sid, seat=x['seat'], cid=x['cid'], price=s['price']), seats))
        order = Order(wid=wid, tickets=tickets, patron=patron)
        list(map(lambda t: self.tickets_list.append(t), tickets))
        self.orders_list.append(order)

        order_re = order.to_dict()
        order_re['show_info'] = s['show_info']
        order_re = Helper.delete_keys(order_re, ['patron_info', 'number_of_tickets'])
        order_re['tickets'] = list(map(lambda t: t['tid'], order_re['tickets']))
        return order_re

    def show_seats_request(self, wid=0, sid=0, count=1, start_id=None):
        show = Helper.get_specific(wid, self.shows_list)
        section = show.get_seating().find_section(sid)
        order = section.find_seats(req_num=count, start_id=start_id)
        if order:
            return show.to_dict()
        return ''

    def search(self, topic, key):
        search_list = list()
        if topic and key:
            for attr, value in self.__dict__.items():
                for v in value:
                    s = v.search(topic, key)
                    if s:
                        search_list.append(s)
            if search_list:
                return {(str(topic) + 's'): list(map(lambda x: Helper.delete_keys(x.to_dict(), ['tickets', 'sid']),
                                                     search_list))}
