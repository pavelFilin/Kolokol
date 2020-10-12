import urllib.request
import datetime

from bs4 import BeautifulSoup
from html.parser import HTMLParser

SCHEDULE_LINK = "http://rasp.sstu.ru/group/120"
EVEN_CLASS = ".chet"
ODD_CLASS = ".nechet"


soup = None

def get_schedule_information(link):
    with urllib.request.urlopen(link) as connect:
        page = connect.read()
        schedule = page.decode("utf8")

    return schedule


def process_schedule():
    # week_count = datetime.date.today().isocalendar()[1]

    even = soup.select(EVEN_CLASS)
    odd = soup.select(ODD_CLASS)
    parse_week(even)


def parse_week(week):
    if len(week) > 0:
        week = week[0]
    else:
        raise Exception

    study_days_html = week.select(".rasp-table-col")
    print(study_days_html)


if __name__ == '__main__':
    schedule_information = get_schedule_information(SCHEDULE_LINK)
    soup = BeautifulSoup(schedule_information, 'lxml')
    process_schedule()
