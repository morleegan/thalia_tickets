from thalia.section import Section

section = Section(name='hi', price=20, sid=2)
s = Section(name='main', price=80)
test_wid = 12
test_price = 21
test = [{'row': '1',
        'seats': ['1', '2', '3', '4', '5']}]


def test_create_section():
    s.create_section(test)
    s_row = s.get_rows()
    assert s_row[0].get_id() == str(1)


def test_check_sid():
    s2 = Section(sid=1)
    assert s2.check_id(1)
    assert s2.check_id(2) is False


def test_to_dict():
    assert sorted(list(section.to_dict().keys())) == sorted(['section_name', 'price', 'seating', 'sid'])


def test_set_price():
    section.set_price(3)
    assert section.get_price() == 3


if __name__ == '__main__':
    test_check_sid()
    test_to_dict()
    test_set_price()
    test_create_section()