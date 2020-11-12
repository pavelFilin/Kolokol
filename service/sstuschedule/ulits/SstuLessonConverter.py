from entities.Lesson import Lesson
from service.TimeLessonUtil import TimeLessonUtil


class SstuLessonConverter:

    @staticmethod
    def convert_from_html(lessons_html, lesson_number):
        subject = lessons_html.select(".subject")
        teacher = lessons_html.select(".teacher")
        classroom = lessons_html.select(".aud")
        lesson_type = lessons_html.select(".type")
        begins = TimeLessonUtil.parse_time_begins(lesson_number)
        ends = TimeLessonUtil.parse_time_ends(lesson_number)

        lesson = Lesson(
            lesson_number,
            subject[0].text if len(subject) > 0 else None,
            teacher[0].text if len(teacher) > 0 else None,
            classroom[0].text if len(teacher) > 0 else None,
            lesson_type[0].text if len(teacher) > 0 else None,
            begins,
            ends
        )

        return lesson
