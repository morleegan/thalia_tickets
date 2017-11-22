from delivery.main import Helper
from thalia.show import Show

show1 = Show()
show2 = Show()
show_list = [show1, show2]

def test_delete_key():
    dic = {"hi": 'hello',
           "hello": 'hi'}
    assert Helper.delete_keys(dic, ['hello']) == {'hi': 'hello'}

def test_get_spec():
    wid = show2.get_wid()
    assert Helper.get_specific(wid, show_list) == show2

if __name__ == '__main__':
    test_delete_key()
    test_get_spec()