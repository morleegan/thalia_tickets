def show_info_helper_v1(show_info):
    return {
            "name": show_info.get_name(),
            "web": show_info.get_web(),
            "date": show_info.get_date(),
            "time": str(show_info.get_time())
            }


def cover_cc_helper_v1(self):
    return 'xxxxxxxxxxxx' + self.get_cc_num()[12:]


def patron_helper_v1(patron):
    return {
        "name": patron.get_name(),
        "phone": patron.get_phone(),
        "email": patron.get_email(),
        "billing_address": patron.get_bill_adr(),
        "cc_number": patron.get_cc_num(),
        "cc_expiration_date": patron.get_cc_exp()
    }


def patron_safe_cc_helper_f1(patron):
    return patron_helper_v1(patron=patron).update({"cc_number": cover_cc_helper_v1(patron)})


def seating_price_helper_v1(seating):
    return list(map(lambda sec: {
        "sid": sec.get_id(),
        "price": sec.get_price()
    }, seating.get_seating()))


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
    """POST http://localhost:8080/thalia/shows/{wid}/donations"""
    return {
        "did": donation.get_id()
    }


def show_donation_api_v1(donation):
    """GET http://localhost:8080/thalia/shows/{wid}/donations/{did}"""
    return {
        "did": donation.get_id(),
        "wid": donation.get_wid(),
        "count": donation.get_amount(),
        "status": donation.get_status(),
        "tickets": donation.get_tickets(),
        "patron_info": patron_helper_v1(donation.get_patron())
    }


def seating_all_api_v1(sections):
    """GET http://localhost:8080/thalia/seating"""
    return list(map(lambda sec: {
        "sid": sec.get_id(),
        "section_name": sec.get_name()
    }, sections.get_seating()))


def seating_sid_api_v1(section):
    """GET http://localhost:8080/thalia/seating/{sid}"""
    return {
        "sid": section.get_id(),
        "section_name": section.get_name(),
        "seating": seating_row_helper_v1(section.get_rows())
    }


def seating_request_api_v1(show, section):
    # TODO
    return {
        "wid": show.get_id(),
        "show_info": show_info_helper_v1(show.get_show_info()),
        "sid": section.get_id(),
        "section_name": section.get_name(),
        "starting_seat_id": "202",  # fill in
        "status": "ok",             # fill in
        "total_amount": 180,        # fill in
        "seating": seating_row_helper_v1(section.get_rows())
    }


def ticket_post_api_v1(ticket):
    return {
        "tid": ticket.get_id(),
        "status": ticket.get_status()}


# def report(self):
#     return {
#         "mrid": self.get_id(),
#         "name": self.get_name(),
#         "start_date": str(self.get_start_date()),
#         "end_date": str(self.get_end_date()),
#         "total_shows": len(self.get_shows()),
#         "total_seats": self.get_total_seats(),
#         "sold_seats": self.to_dict(),
#         "donated_tickets": 5,
#         "donated_and_used_tickets": 4,
#         "donated_and_used_value": 220,
#         "shows": list(map(lambda x: {
#             "wid": x.get_id(),
#             "show_info": x.get_show_info(),
#             "seats_available": x.get_total_seats() - x.get_sold_total(),
#             "seats_sold": x.get_sold_total(),
#             "donated_tickets": 3,
#             "donated_and_used_tickets": 2,
#             "donated_and_used_value": 100
#         }, self.get_shows()))
#     }


# def report(self):
#     self.calculate_report()
#     return {
#         "mrid": self.get_id(),
#         "name": self.get_name(),
#         "total_shows": len(self.get_shows()),
#         "total_seats": self.get_total_seats(),
#         "sold_seats": self.get_total_sold(),
#         "overall_revenue": self.get_rev(),
#         "shows": list(map(lambda s: {
#             "wid": s.get_id(),
#             "show_info": s.get_show_info() if isinstance(s.get_show_info(), dict) else s.get_show_info().to_dict(),
#             "sections": list(map(lambda x: x.report(), s.get_seating().get_seating()))
#         }, self.get_shows()))
#     }

# def to_dict(self):
#     show = ShowInfo()
#     return {
#         "oid": self.get_id(),
#         "wid": self.get_wid(),
#         "show_info": show.to_dict(),
#         "date_ordered": str(self.get_date())[:16],
#         "order_amount": self.get_total(),
#         "number_of_tickets": len(self.get_tickets()),
#         "patron_info": self.get_patron().to_dict(),
#         "tickets": list(map(lambda x: x.to_dict(), self.get_tickets())),
#
#     }