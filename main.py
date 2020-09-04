import urllib.request
import datetime

from enum import Enum
from beautifulsoup4 import BeautifulSoup
from html.parser import HTMLParser

SCHEDULE_LINK = "http://rasp.sstu.ru/group/120"


def get_schedule_information():
    with urllib.request.urlopen(SCHEDULE_LINK) as connect:
        page = connect.read()
        schedule = page.decode("utf8")

    return schedule


def process_schedule(schedule):
    week_count = datetime.date.today().isocalendar()[1]


class LessonType(Enum):
    LECTURE = 0
    PRACTICE = 1
    LABORATORY = 2


class WeekType(Enum):
    EVEN = 0
    ODD = 1


class Lesson:
    def __init__(self, number, name, teacher, classroom, lesson_type, begin_time, end_time):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.classroom = classroom
        self.lesson_type = lesson_type
        self.begin_type = begin_time
        self.end_type = end_time


class Day:
    def __init__(self, lessons, weekday):
        self.lessons = lessons
        self.weekday = weekday


class Week:
    def __init__(self, lessons, week_type):
        self.lessons = lessons
        self.week_type = week_type


if __name__ == '__main__':
    get_schedule_information()
