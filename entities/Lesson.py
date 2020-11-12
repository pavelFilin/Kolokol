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
