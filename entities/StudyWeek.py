from entities.StudyDay import StudyDay


class StudyWeek:
    def __init__(self, study_days, week_type):
        self.study_days = study_days
        self.week_type = week_type

    @staticmethod
    def convert_from_html(week, week_type):
        week = week[0]
        study_days_html = week.select(".rasp-table-col")

        study_days = []

        for i in range(0, len(study_days_html)):
            study_week = StudyDay.convert_from_html(study_days_html[i], i)
            study_days.append(study_week)

        return StudyWeek(study_days, week_type)
