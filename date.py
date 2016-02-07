"""
File: date.py
Author: Yang Zhao
"""

class Date(object):
    """
    This class represents date in year, month, day.
    """
    # Class variable
    month2days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, \
                  8:31, 9:30, 10:31, 11:30, 12:31, 0:0}
    # Constructor
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    # Accessor
    def __sub__(self, other):
        """
        This function compares two Date object and
        returns the number of days between them.

        Precondition: self is bigger(later) than other
        ==============================================
        How to compute the day difference:
        if self and other are in the same year, we use
         diff = (self - start of the year) - (other - start of the year)
        if self and other are in different year, we use
         diff = (self - start of the year) -
                    (end of other year - other)

        When we compute the difference of dates in the same year, we compute
        the difference to the start of the year for both dates first, then we
        substract the difference.
        """
        if self._year == other._year:
            diff = abs(self.day2startOfYear() - other.day2startOfYear())
        elif self._year > other._year:
            diff = self.day2startOfYear() - other.day2endOfYear() + \
                   self._year - other._year
        else:
            diff = other.day2startOfYear() - self.day2endOfYear() + \
                   other._year - self._year
        return diff

    def __eq__(self, other):
        return self - other == 0

    def __str__(self):
        return "Year: " + str(self._year) + "\n" + \
               "Month: " + str(self._month) + "\n" + \
               "Day: " + str(self._day) + "\n"

    def getYear(self):
        return self._year

    def getMonth(self):
        return self._month

    def getDay(self):
        return self._day

    # Helper methods
    def day2startOfYear(self):
        days = 0
        for i in range(1, self._month):
            if i == 2 and self.isLeapYear():
                days += 29
            else:
                days += Date.month2days[i]
        days += self._day
        return days

    def day2endOfYear(self):
        if self.isLeapYear():
            return 366 - self.day2startOfYear()
        else:
            return 365 - self.day2startOfYear()

    def isLeapYear(self):
        if self._year % 4 != 0:
            return False
        elif self._year % 100 != 0:
            return True
        elif self._year % 400 != 0:
            return False
        else:
            return True

if __name__ == "__main__":
    d1 = Date(2015, 1, 1)
##    print(d1.day2startOfYear())
    d2 = Date(2015, 1, 1)
    print(d2 - d1)
    print(d2 == d1)
##    d3 = Date(2012, 12, 31)
##    print(d3.day2startOfYear())
