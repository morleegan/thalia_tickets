from thalia.order import Patron, Order, Ticket

patron = Patron("name", "email", "phone", "bill", "cc_num", "cc_exp")
p = {
            "name": None,
            "phone": None,
            "email": None,
            "billing_address": None,
            "cc_number": None,
            "cc_expiration_date": None
        }

o={
            "oid": None,
            "wid": None,
            "sid": None,
            "show_info": None,
            "date_ordered": None,
            "ordered_amount": None,
            "tickets": None,
            "patron": None
        }
ticket = Ticket(price=80, cid=123, seat=10)
ticket2 = Ticket(price=100, cid=123, seat=11)
tickets = [ticket, ticket2]

order = Order(wid=2, sid=2, tickets=tickets, patron=patron)


def test_ticket_to_dict():
    assert sorted(ticket.to_dict().keys()) == ['cid', 'seat', 'tid']


def test_patron_to_dict():
    assert sorted(patron.to_dict().keys()) == sorted(p.keys())


def test_order_to_dict():
    assert o.keys() == order.to_dict().keys()


if __name__ == '__main__':
    test_patron_to_dict()
    test_ticket_to_dict()
    test_order_to_dict()