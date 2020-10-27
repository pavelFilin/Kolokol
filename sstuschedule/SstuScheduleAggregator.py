import urllib.request

from bs4 import BeautifulSoup

from entities import Constants
from entities.StudyWeek import StudyWeek
from entities.enums.WeekType import WeekType


class SstuScheduleParser:
    even = None
    odd = None

    def __init__(self):
        schedule_information = self.__get_schedule_information(Constants.SCHEDULE_LINK)

        schedule = BeautifulSoup(schedule_information, 'lxml')

        even_html = schedule.select(Constants.EVEN_CLASS)
        odd_html = schedule.select(Constants.ODD_CLASS)

        self.even = StudyWeek.convert_from_html(even_html, WeekType.EVEN)
        self.even = StudyWeek.convert_from_html(odd_html, WeekType.ODD)

    def __get_schedule_information(self, link):
        with urllib.request.urlopen(link) as connect:
            page = connect.read()
            schedule = page.decode("utf8")

        return schedule

