import datetime
from thalia.show import Show, ShowInfo
from thalia.theater import Theater

test_show = Show(show_info=2, seating_info=2)
showinfo = ShowInfo(name="test", web="test")
theater = Theater()
test_show2 = Show(show_info=showinfo, seating_info=theater)


def test_show_get():
    assert test_show.get_show_info() == 2
    assert test_show.get_seating() == 2


def test_show_set():
    test_show.set_seating(3)
    test_show.set_show_info(4)
    assert test_show.get_show_info() == 4
    assert test_show.get_seating() == 3


def test_show_to_dict():
    assert sorted(test_show2.to_dict().keys()) == ["seating_info", "show_info", "wid"]


def test_show_info_get():
    assert showinfo.get_name() == "test"
    assert showinfo.get_web() == "test"
    assert showinfo.get_date() == datetime.date.today()


def test_show_info_to_dict():
    assert sorted(showinfo.to_dict().keys()) == ["date", "name", "time", "web"]


def test_show_info_set_all():
    showinfo.set_all(name="hi", web="www", date='2017-10-12', time='20:30')
    assert showinfo.get_name() == "hi"
    assert showinfo.get_web() == "www"
    assert showinfo.get_date() == datetime.date(year=2017, month=10, day=12)
    assert showinfo.get_time() == datetime.time(20, 30)


if __name__ == '__main__':
    test_show_get()
    test_show_set()
    test_show_to_dict()

    test_show_info_get()
    test_show_info_to_dict()
    test_show_info_set_all()
