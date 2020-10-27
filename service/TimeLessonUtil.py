class TimeLessonUtil:
    start_time = {
        0: "9:30",
        1: "11:15",
        2: "13:00",
        3: "15:10",
    }

    end_time = {
        0: "8:00",
        1: "9:45",
        2: "11:30",
        3: "13:40",
    }

    @classmethod
    def parse_time_ends(cls, lesson_number):
        return cls.start_time.get(lesson_number, "")

    @classmethod
    def parse_time_begins(cls, lesson_number):
        return cls.end_time.get(lesson_number, "")
