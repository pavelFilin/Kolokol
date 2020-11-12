from entities.StudyDay import StudyDay
from service.sstuschedule.ulits.SstuLessonConverter import SstuLessonConverter


class SstuStudyDayConvertor:

    @staticmethod
    def convert_from_html(study_days_html, weekday):
        lessons_html = study_days_html.select(".rasp-table-row")

        lessons = []

        for i in range(0, len(lessons_html)):
            lesson = SstuLessonConverter.convert_from_html(lessons_html[i], i)
            lessons.append(lesson)

        return StudyDay(lessons, weekday)
