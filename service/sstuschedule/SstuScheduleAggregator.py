import urllib.request

from bs4 import BeautifulSoup

from entities import Constants
from entities.Constants import GROUP_NAME_CLASS
from entities.Schedule import Schedule
from entities.enums.WeekType import WeekType
from service.sstuschedule.ulits.SstuParcerUtils import format_sstu_group_name_from_schedule_html
from service.sstuschedule.ulits.SstuStudyWeekConverter import SstuStudyWeekConverter


class SstuScheduleAggregator:

    @staticmethod
    def __get_schedule_information(link):
        with urllib.request.urlopen(link) as connect:
            page = connect.read()
            schedule = page.decode("utf8")

        return schedule

    def get_schedule(self, schedule_link):
        schedule_information_row_html = SstuScheduleAggregator.__get_schedule_information(schedule_link)

        schedule = BeautifulSoup(schedule_information_row_html, 'lxml')

        group_name = format_sstu_group_name_from_schedule_html(schedule.select_one(GROUP_NAME_CLASS).text)

        even = SstuStudyWeekConverter.convert_from_html(schedule.select(Constants.EVEN_CLASS), WeekType.EVEN)
        odd = SstuStudyWeekConverter.convert_from_html(schedule.select(Constants.ODD_CLASS), WeekType.ODD)

        return Schedule(group_name, even, odd)
