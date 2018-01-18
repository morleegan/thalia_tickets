from thalia.order import Patron, Order, Ticket

patron = Patron("name", "email", "phone", "bill", "cc_num", "cc_exp")
p = {
            "name": "None",
            "phone": None,
            "email": None,
            "billing_address": None,
            "cc_number": None,
            "cc_expiration_date": None
        }

o={
            "oid": None,
            "wid": None,
            "show_info": None,
            "date_ordered": None,
            "order_amount": None,
            "number_of_tickets": None,
            "tickets": None,
            "patron_info": None

        }

t = {"tid": None,
     "price": None,
     "status": None,
     "cid": None,
     "seat": None}

ticket = Ticket(price=80, cid=123, seat=10)
ticket2 = Ticket(price=100, cid=123, seat=11)
tickets = [ticket, ticket2]

order = Order(wid=2, tickets=tickets, patron=patron)


def test_search():
    assert order.search('order', 'name') is order
    assert order.search('order', '2') is order


def test_date_check():
    assert order.check_date() is True
    assert order.check_date(start='20000220', end='20010110') is False
    assert order.check_date(start='20171123', end='20171123') is True


def test_get_total():
    assert order.get_total() == 180

def test_set_status():
    ticket.set_status('test')
    assert ticket.get_status() =='test'

if __name__ == '__main__':
    test_search()
    test_date_check()
    test_get_total()
    test_set_status()