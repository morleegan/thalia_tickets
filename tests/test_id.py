from helpers.helper import ID

new_id = ID()

def test_get_id():
    assert new_id.get_id() is not None

def test_check_id():
    o_id = new_id.get_id()
    assert new_id.check_id(o_id) is True
    assert new_id.check_id(1) is False

def test_set_id():
    new_id.set_id(2)
    assert new_id.get_id() == 2

def test_search():
    assert new_id.search('id', 'id') is new_id
    o_id = new_id.get_id()
    assert new_id.search('id', o_id) is new_id

if __name__ == '__main__':
    test_check_id()
    test_get_id()
    test_set_id()
    test_search()