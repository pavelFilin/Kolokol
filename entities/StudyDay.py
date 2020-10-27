from entities.Lesson import Lesson


class StudyDay:
    def __init__(self, lessons, weekday):
        self.lessons = lessons
        self.weekday = weekday

    @staticmethod
    def convert_from_html(study_days_html, weekday):
        lessons_html = study_days_html.select(".rasp-table-row")

        lessons = []

        for i in range(0, len(lessons_html)):
            lesson = Lesson.convert_from_html(lessons_html[i], i)
            lessons.append(lesson)

        return StudyDay(lessons, weekday)
