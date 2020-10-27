from enum import Enum


class LessonType(Enum):
    LECTURE = 0
    PRACTICE = 1
    LABORATORY = 2

    @classmethod
    def parse(string):
        return {
            "(лек)": LessonType.LECTURE,
            "(прак)": LessonType.PRACTICE,
            "(лаб)": LessonType.LABORATORY
        }.get(string, None)
