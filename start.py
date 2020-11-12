from datetime import datetime

import jsonpickle
from flask import Flask

from entities import Constants
from entities.enums.WeekType import WeekType
from service.WeekReverseDefiner import WeekReverseDefiner
from service.sstuschedule.SstuScheduleAggregator import SstuScheduleAggregator

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/schedule')
def get_schedule():
    schedule = SstuScheduleAggregator().get_schedule(Constants.IBS_51_SCHEDULE_LINK)

    jsonpickle.set_preferred_backend('json')
    jsonpickle.set_encoder_options('json', ensure_ascii=False)
    return jsonpickle.encode(schedule, unpicklable=False)


@app.route('/schedule/today')
def get_schedule_today():

    schedule = SstuScheduleAggregator().get_schedule(Constants.IBS_51_SCHEDULE_LINK)

    now = datetime.now()
    week_type = WeekReverseDefiner().defineWeekType(now)
    weekday = now.weekday()

    if week_type == WeekType.EVEN:
        week = schedule.even
    else:
        week = schedule.odd

    day = week.study_days[weekday]

    jsonpickle.set_preferred_backend('json')
    jsonpickle.set_encoder_options('json', ensure_ascii=False)
    return jsonpickle.encode(day, unpicklable=False)




