from thalia.row import Row
from thalia.row import Seat

s1 = Seat(1)
row1 = Row(row=1, seats=[1, 2, 3, 4, 5])


def test_get_row_number():
    assert row1.get_name() == 1


def test_search_row():
    s = row1.get_seats()
    s2 = s.r_seat
    sid = s.get_cid()
    assert s == row1.search_row(sid)
    assert s2 == row1.search_row(s2.get_cid())
    assert row1.search_row(1) is None


def test_find_seats():
    test1 = row1.find_seats(num_req=3)

    assert test1[0].get_name() == 5
    assert test1[1].get_name() == 4
    assert test1[2].get_name() == 3
    assert row1.find_seats(num_req=8) is None


def test_get_as_list():
    test = list(map(lambda x: x.get_name(), row1.get_seats_as_list()))
    assert test == [5,4,3,2,1]


def test_check_availability():
    assert s1.check_availability() is True
    s1.bought_seat()
    assert s1.check_availability() is False


def test_bought_seat():
    s1.bought_seat()
    assert s1.get_status() == "sold"


def test_seat_to_dict():
    assert sorted(s1.to_dict().keys()) == ['cid', 'name', 'status']

def test_row_to_dict():
    assert sorted(row1.to_dict().keys()) == ['row', 'seats']

if __name__ == '__main__':
    test_get_row_number()
    test_search_row()
    test_find_seats()
    test_get_as_list()
    test_check_availability()
    test_bought_seat()
    test_seat_to_dict()
    test_row_to_dict()