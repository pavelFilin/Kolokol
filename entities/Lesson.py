from service.TimeLessonUtil import TimeLessonUtil


class Lesson:
    def __init__(self, number, name, teacher, classroom, lesson_type, begin_time, end_time):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.classroom = classroom
        self.lesson_type = lesson_type
        self.begin_type = begin_time
        self.end_type = end_time

    def is_empty(self):
        return self.number is None \
               and self.name is None \
               and self.teacher is None \
               and self.classroom is None \
               and self.lesson_type is None

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
