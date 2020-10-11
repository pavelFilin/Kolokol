import urllib.request
import datetime

from bs4 import BeautifulSoup
from html.parser import HTMLParser

SCHEDULE_LINK = "http://rasp.sstu.ru/group/120"


def get_schedule_information(link):
    with urllib.request.urlopen(link) as connect:
        page = connect.read()
        schedule = page.decode("utf8")

    return schedule


def process_schedule(schedule):
    week_count = datetime.date.today().isocalendar()[1]
    print(week_count)


if __name__ == '__main__':
    schedule_information = get_schedule_information(SCHEDULE_LINK)
    process_schedule(schedule_information)
