from thalia.section import Section


class Theater:
    """Theater/Seating section."""
    theater = [{"section_name": "Front right",
                "seating": [{
                    "row": "1",
                    "seats": ["1", "2", "3", "4"]
                },
                    {"row": "2",
                     "seats": ["1", "2", "3", "4"]
                     },
                    {"row": "3",
                     "seats": ["1", "2", "3", "4"]
                     },
                    {"row": "4",
                     "seats": [
                         "1",
                         "2",
                         "3",
                         "4"
                     ]
                     }
                ]
                },
               {
                   "section_name": "Front center",
                   "seating": [{
                       "row": "1",
                       "seats": [
                           "5",
                           "6",
                           "7",
                           "8"
                       ]
                   },
                       {
                           "row": "2",
                           "seats": [
                               "5",
                               "6",
                               "7",
                               "8"
                           ]
                       },
                       {
                           "row": "3",
                           "seats": [
                               "5",
                               "6",
                               "7",
                               "8",
                               "9"
                           ]
                       },
                       {
                           "row": "4",
                           "seats": [
                               "5",
                               "6",
                               "7",
                               "8",
                               "9",
                               "10"
                           ]
                       }
                   ]
               },
               {
                   "section_name": "Front left",
                   "seating": [{
                       "row": "1",
                       "seats": [
                           "9",
                           "10",
                           "11",
                           "12"
                       ]
                   },
                       {
                           "row": "2",
                           "seats": [
                               "9",
                               "10",
                               "11",
                               "12"
                           ]
                       },
                       {
                           "row": "3",
                           "seats": [
                               "9",
                               "10",
                               "11",
                               "12"
                           ]
                       },
                       {
                           "row": "4",
                           "seats": [
                               "9",
                               "10",
                               "11",
                               "12"
                           ]
                       }
                   ]
               },
               {
                   "section_name": "Main right",
                   "seating": [{
                       "row": "5",
                       "seats": [
                           "1",
                           "2",
                           "3",
                           "4",
                           "5"
                       ]
                   },
                       {
                           "row": "6",
                           "seats": [
                               "1",
                               "2",
                               "3",
                               "4",
                               "5"
                           ]
                       },
                       {
                           "row": "7",
                           "seats": [
                               "1",
                               "2",
                               "3",
                               "4",
                               "5"
                           ]
                       }
                   ]
               },
               {
                   "section_name": "Main center",
                   "seating": [{
                       "row": "5",
                       "seats": [
                           "6",
                           "7",
                           "8",
                           "9",
                           "10",
                           "11"
                       ]
                   },
                       {
                           "row": "6",
                           "seats": [
                               "6",
                               "7",
                               "8",
                               "9",
                               "10",
                               "11",
                               "12"
                           ]
                       },
                       {
                           "row": "7",
                           "seats": [
                               "6",
                               "7",
                               "8",
                               "9",
                               "10",
                               "11",
                               "12",
                               "13"
                           ]
                       }
                   ]
               },
               {
                   "section_name": "Main left",
                   "seating": [{
                       "row": "5",
                       "seats": [
                           "12",
                           "13",
                           "14",
                           "15",
                           "16"
                       ]
                   },
                       {
                           "row": "6",
                           "seats": [
                               "13",
                               "14",
                               "15",
                               "16",
                               "17"
                           ]
                       },
                       {
                           "row": "7",
                           "seats": [
                               "14",
                               "15",
                               "16",
                               "17",
                               "18"
                           ]
                       }
                   ]
               }
               ]

    def __init__(self):
        self.__seating = list()
        self.create_theater(self.theater)

    def get_seating(self):
        return self.__seating

    def set_seating(self, seating):
        self.__seating = seating

    def create_theater(self, theater_json):
        """theater is a list of"""
        count = 123
        new_seating = list()
        for section in theater_json:
            new_seating.append(Section(sid=str(count), name=section['section_name'], rows=section['seating']))
            count += 1

        self.set_seating(new_seating)

    def update_seating(self, update_seating):
        create_seating = list()
        for sec in self.get_seating():
            for s in update_seating:
                if sec.check_id(s['sid']):
                    sec.set_price(s['price'])
                    create_seating.append(sec)
        self.set_seating(create_seating)

    def find_section(self, sid):
        for s in self.get_seating():
            if s.check_id(sid):
                return s

    def to_dict(self):
        return list(map(lambda x: x.to_dict(), self.get_seating()))