#!/usr/bin/env python3
def two_digits(digit: int):
    str_digit = str(digit)
    if len(str_digit) == 1:
        str_digit = '0' + str_digit
    return str_digit


class Timer:

    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.__hh = hours
        self.__mm = minutes
        self.__ss = seconds

    def __str__(self):
        return two_digits(self.__hh) + ':' + two_digits(self.__mm) + ':' + two_digits(self.__ss)

    def next_second(self):
        self.__ss += 1
        if self.__ss >= 60:
            self.__ss = 0
            self.__mm += 1
            if self.__mm >= 60:
                self.__mm = 0
                self.__hh += 1
                if self.__hh > 23:
                    self.__hh = 0

    def prev_second(self):
        self.__ss -= 1
        if self.__ss < 0:
            self.__ss = 59
            self.__mm -= 1
            if self.__mm < 0:
                self.__mm = 59
                self.__hh -= 1
                if self.__hh < 0:
                    self.__hh = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
