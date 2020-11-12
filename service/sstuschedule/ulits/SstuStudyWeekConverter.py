from entities.StudyWeek import StudyWeek
from service.sstuschedule.ulits.SstuStudyDayConverter import SstuStudyDayConvertor


class SstuStudyWeekConverter:

    @staticmethod
    def convert_from_html(week, week_type):
        week = week[0]
        study_days_html = week.select(".rasp-table-col")

        study_days = []

        for i in range(0, len(study_days_html)):
            study_week = SstuStudyDayConvertor.convert_from_html(study_days_html[i], i)
            study_days.append(study_week)

        return StudyWeek(study_days, week_type)