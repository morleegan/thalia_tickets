from thalia.row import Row
from thalia.row import Seat

s1 = Seat(1)
row1 = Row(row=1, seats=[1, 2, 3, 4, 5])


def test_get_row_number():
    assert row1.get_id() == 1


def test_search_row():
    s = row1.get_seats()
    s2 = s.r_seat
    sid = s.get_id()
    assert s == row1.search_row(sid)
    assert s2 == row1.search_row(s2.get_id())
    assert row1.search_row(1) is None


def test_get_as_list():
    test = list(map(lambda x: x.get_name(), row1.get_seats_as_list()))
    assert test == sorted([5,4,3,2,1])


def test_check_availability():
    s2 = Seat(1)
    assert s2.check_availability() is True
    s1.bought_seat()
    assert s1.check_availability() is False


def test_bought_seat():
    s1.bought_seat()
    assert s1.get_status() == "sold"


def test_find_seats():
    seats = row1.find_seats(req_num=2)
    cids = list(map(lambda x: x.get_name(), seats))
    assert cids == [1, 2]
    cid = row1.get_seats_as_list()[1].get_id()
    assert list(map(lambda s: s.get_name(), row1.find_seats(req_num=3, start_id=cid))) == [2, 3, 4]
    assert row1.find_seats(req_num=8) is row1.get_seats_as_list()[0].get_id()


def test_order_seats():
    seats = row1.find_seats(req_num=2)
    cids = list(map(lambda x: x.get_id(), seats))
    row1.order_seats(cids)
    r = row1.get_seats()
    while r.r_seat is not None:
        if r.get_id() in cids:
            assert r.get_status() == 'sold'
        r = r.r_seat

if __name__ == '__main__':
    test_get_row_number()
    test_search_row()
    test_find_seats()
    test_get_as_list()
    test_check_availability()
    test_bought_seat()
    test_order_seats()
