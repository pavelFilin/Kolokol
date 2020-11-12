import json

import jsonpickle as jsonpickle
from flask import Flask, jsonify

from entities import Constants
from sstuschedule.SstuScheduleAggregator import SstuScheduleAggregator

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




