from entities.enums.WeekType import WeekType


class WeekReverseDefiner:
    def defineWeekType(self, data):
        number_of_week = data.isocalendar()[1]
        return WeekType.EVEN if number_of_week % 2 != 0 else WeekType.ODD
