def show_info_helper_v1(show_info):
    return {
            "name": show_info.get_name(),
            "web": show_info.get_web(),
            "date": show_info.get_date(),
            "time": show_info.get_time()
            }


def patron_helper_v1(patron):
    return {
        "name": patron.get_name(),
        "phone": patron.get_phone(),
        "email": patron.get_email(),
        "billing_address": patron.get_bill_adr(),
        "cc_number": patron.get_cc_num(),
        "cc_expiration_date": patron.get_cc_exp()
    }


def seating_price_helper_v1(seating):
    return list(map(lambda sec: {
        "sid": sec.get_id(),
        "price": sec.get_price()
    }, seating))


def seating_row_helper_v1(row_list):
    return list(map(lambda row: {
        "row": row.get_id(),
        "seats": seats_helper_v1(row.get_seats_as_list())
    }, row_list))


def seats_helper_v1(seat_list):
    return list(map(lambda seat: {
        "cid": seat.get_id(),
        "seat": seat.get_name(),
        "status": seat.get_status()
    }, seat_list))


def show_wid_api_v1(show):
    """GET http://localhost:8080/thalia/shows/{wid}"""
    return {
        "wid": show.get_id(),
        "show_info": show_info_helper_v1(show_info=show.get_show_info()),
        "seating_info": seating_price_helper_v1(seating=show.get_seating())
    }


def show_create_api_v1(show):
    """POST Create Show"""
    return {
        "wid": show.get_id()}


def show_all_api_v1(shows_list):
    """GET http://localhost:8080/thalia/shows"""
    return list(map(lambda show: {
        "wid": show.get_id(),
        "show_info": show_info_helper_v1(show.get_show_info())
    }, shows_list))


def show_section_api_v1(show):
    """GET http://localhost:8080/thalia/shows/{wid}/sections"""
    return list(map(lambda section: {
        "sid": section.get_id(),
        "section_name": section.get_name(),
        "price": section.get_price()
    }, show.get_seating()))


def seating_with_sid_api_v1(show, section):
    """GET http://localhost:8080/thalia/shows/{wid}/sections/{sid}"""
    return {
        "wid": show.get_id(),
        "show_info": show.get_show_info(),
        "sid": section.get_id(),
        "section_name": section.get_name(),
        "price": section.get_price(),
        "seating": seating_row_helper_v1(section.get_rows())
    }


def show_donation_create_api_v1(donation):
    """POST http://localhost:8080/thalia/shows/308/donations"""
    return {
        "did": donation.get_id()
    }


def ticket_post_api_v1(ticket):
    return {
        "tid": ticket.get_id(),
        "status": ticket.get_status()}


# show_sec = show_sec.to_dict()
# if show_sec == "does not exist":
#     return show_sec
# seating = show_sec.get('seating_info')
# for sec in seating:
#     if sec["sid"] == str(sid):
#         s = {"wid": wid, "show_info": show_sec.get('show_info')}
#         s.update(sec)
#         return s

# show section
# return list(map(lambda x: Helper.delete_keys(x.to_dict(), ['seating_info']), self.shows_list)) if \
#     self.shows_list else list()

# order by date
# for s in self.shows_list:
#     if s.check_id(o.get_wid()):
#         o_dict = o.to_dict()
#         si_dict = s.get_show_info()
#         o_dict['show_info'] = si_dict
#         o_dict = Helper.delete_keys(o_dict, ['sid', 'tickets'])

# order
# if order:
#     show = self.get_shows(order.get_wid())
#     show = show.to_dict()
#     o_dict = order.to_dict()
#     o_dict = Helper.delete_keys(o_dict, ['sid', 'number_of_tickets'])
#     o_dict['tickets'] = list(map(lambda t: Helper.delete_keys(t, ['cid', 'seat', 'price']),
#                                  o_dict['tickets']))
#     o_dict['show_info'] = show['show_info']
#     return o_dict
# return "does not exist"

# post order
# order_re = order.to_dict()
#         order_re['show_info'] = s['show_info']
#         order_re = Helper.delete_keys(order_re, ['patron_info', 'number_of_tickets'])
#         order_re['tickets'] = list(map(lambda t: t['tid'], order_re['tickets']))
#         return order_re

# for o in self.orders_list:
#     for s in self.shows_list:
#         if s.check_id(o.get_wid()):
#             o_dict = o.to_dict()
#             si_dict = s.get_show_info()
#             o_dict['show_info'] = si_dict
#             o_dict = Helper.delete_keys(o_dict, ['sid', 'tickets'])
#             orders.append(o_dict)

# search
# if search_list:
#     return {(str(topic) + 's'): list(map(lambda x: Helper.delete_keys(x.to_dict(), ['tickets', 'sid']),
#                                          search_list))}

# seating by request
#  s_dict = self.get_show_section_by_id(wid, sid)
# if not isinstance(order, str):
#     s_dict['starting_seat_id'] = order[0].get_id()
#     s_dict['status'] = 'ok'
#     s_dict['amount_total'] = s_dict['price'] * len(order)
#     s_dict['seating'] = order.to_dict()
#     Helper.delete_keys(s_dict, ['price'])
# else:
#     status = str("Error: " + str(count) + " contiguous seats not available")
#     s_dict['starting_seat_id'] = order
#     s_dict['status'] = status
#     s_dict['seating'] = list()
#     Helper.delete_keys(s_dict, ['price'])
# return s_dict
