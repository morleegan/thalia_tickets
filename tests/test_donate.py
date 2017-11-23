from thalia.donate import Donate
from thalia.order import Ticket

d = {
        "did": '',
        "wid": '',
        "count": '',
        "status": '',
        "tickets": '',
        "patron_info": ''}

donate_test = Donate(wid=10, amount=2)
don = Donate(wid=10, amount=0)
ticket = Ticket(wid=10)
tickets = [ticket]


def test_to_dict():
    assert donate_test.to_dict().keys() == d.keys()


def test_take_ticket():
    leftover = don.take_tickets(tickets)
    leftover = donate_test.take_tickets(leftover)
    assert len(leftover) == 0
    assert donate_test.get_tickets()[0] == ticket


if __name__ == '__main__':
    test_to_dict()
    test_take_ticket()