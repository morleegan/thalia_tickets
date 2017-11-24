from thalia.section import Section
from thalia.theater import Theater

s = [
      {
        "sid": "123",
        "price": 600
      },
      {
        "sid": "124",
        "price": 75
      },
      {
        "sid": "125",
        "price": 60
      }
    ]

test_theater = Theater()
test_theater.update_seating(s)


def test_make_seating():
    assert test_theater.get_seating() is not None
    assert isinstance(test_theater.get_seating()[0], Section)

def test_find_section():
    assert test_theater.find_section(111) is None
    assert test_theater.get_seating()[1] == test_theater.find_section(124)

if __name__ == '__main__':
    test_make_seating()
    test_find_section()