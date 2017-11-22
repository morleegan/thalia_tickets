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


def test_make_seating():
    test_theater.update_seating(s)
    assert test_theater.get_seating() is not None
    assert isinstance(test_theater.get_seating()[0], Section)


if __name__ == '__main__':
    test_make_seating()
