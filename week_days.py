class WeekDayError(Exception):
    pass


class Weeker:
    week_days = ('Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom')

    def __init__(self, day):
        if day not in Weeker.week_days:
            raise WeekDayError
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        self.__day = Weeker.week_days[(Weeker.week_days.index(self.__day) + n) % 7]

    def subtract_days(self, n):
        self.__day = Weeker.week_days[(Weeker.week_days.index(self.__day) - n) % 7]


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
