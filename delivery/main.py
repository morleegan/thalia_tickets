from thalia.show import Show, ShowInfo
from thalia.theater import Theater
from thalia.order import Ticket, Order, Patron
from helpers.helper import Helper

""" holds all the classes made by the rest"""


class Emulate:
    def __init__(self):
        self.shows_list = list()
        self.tickets_list = list()
        self.orders_list = list()

    @staticmethod
    def get_seating(sid=None):
        seating = Theater().get_seating()
        if sid is not None:
            sec = Helper.get_specific(sid, seating)
            return Helper.delete_keys(sec.to_dict(), ['price'])
        return list(map(lambda x: Helper.delete_keys(x.to_dict(), ['price', 'seating']), seating))

    def get_orders(self, oid=None):
        if oid is not None:
            order = Helper.get_specific(oid, self.orders_list)
            return order.to_dict if order else "does not exist"
        return list(map(lambda x: x.to_dict, self.orders_list))

    def get_shows(self, wid=None):
        if wid is not None:
            show = Helper.get_specific(wid, self.shows_list)
            return show.to_dict() if show else "does not exist"
        return list(map(lambda x: Helper.delete_keys(x.to_dict(), ['seating_info']), self.shows_list)) if \
            self.shows_list else list()

    def get_show_section(self, wid=0):
        show_dict = self.get_shows(wid=wid)
        if show_dict == "does not exist":
            return show_dict
        sect = show_dict.get('seating_info', None)
        if sect:
            return list(map(lambda x: Helper.delete_keys(x, ['seating']), sect))
        return show_dict

    def get_show_section_by_id(self, wid=0, sid=0):
        show_sec = self.get_shows(wid=wid)
        if show_sec == "does not exist":
            return show_sec
        seating = show_sec.get('seating_info')
        for sec in seating:
            if sec["sid"] == str(sid):
                s = {"wid": wid, "show_info": show_sec.get('show_info')}
                s.update(sec)
                return s

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

    def post_order(self, wid=None, sid=None, seats=None, patron=None):
        patron = Patron(name=patron['name'], email=patron['email'], cc_exp=patron['cc_expiration_date'],
                        cc_num=patron['cc_number'], bill_add=patron['billing_address'])
        tickets = list(map(lambda x: Ticket(seat=x['seat'], cid=x['cid']), seats))
        order = Order(wid=wid, sid=sid, tickets=tickets, patron=patron)
        self.tickets_list.append(tickets)
        self.orders_list.append(order)
        return order.to_dict()

    def show_seats_request(self, wid=0, sid=0, count=1):
        show = Helper.get_specific(wid, self.shows_list)
        section = show.get_seating().find_section(sid)
        order = section.find_seats(req_num=count)
        if order:
            return show.to_dict()
