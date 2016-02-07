"""
File: counter.py
Author: Yang Zhao
"""

"""
This class has two attributes:
    1.time in seconds.
    2. date in year, month, day.
"""
from date import Date

class Counter(object):
    # Constructor
    def __init__(self, message = None):
        """
        The constructor initialize a Counter instance from a
        str message contains year, month, day and time in seconds.
        """
        # If the message is a str, it contains both time and date
        if type(message) == type(""):
            info = message.split()
            self._date = Date(int(info[0]), int(info[1]), int(info[2]))
            self._time = (int(info[3]))
        # If the meesage is a list, it contains only date
        elif type(message) == type([1]):
            self._date = Date(message[0], message[1], message[2])
            self._time = 0
        # If no message is provided, a dummy Counter is created
        else:
            self._date = Date(0, 0, 0)
            self._time = 0

    # Accessor
    def __str__(self):
        [hours, minutes, seconds] = self.convertTime()
        return str(hours) + " h, " + str(minutes) +\
               " min."

    def __add__(self, other):
        """ Compute the total time stored in two Counters. """
        result = Counter("0 0 0 " + str(self._time + other._time))
        return result

    def __sub__(self, other):
        """ Comopute the day difference between two dates stored in self
        and other. """
        return self._date - other._date

    def __eq__(self, other):
        """ Check if the date stored in self and other represent the same
        day. """
        return self._date == other._date

    def __ne__(self, other):
        return not self == other

    def getDate(self):
        return self._date

    def getTime(self):
        return self._time

    # Mutator
    def addTime(self, time):
        self._time += time
        
    # Helper methods
    def convertTime(self):
        hours = self._time // 3600
        minutes = (self._time - hours * 3600) // 60
        seconds = self._time - hours*3600 - minutes*60
        return hours, minutes, seconds

if __name__ == "__main__":
    c1 = Counter("2015 3 2 3000")
    c2 = Counter("2015 3 3 2000")
    print(c1)
    print(c2)
    print(c1+c2)
    print(c1 - c2)
    print(c1 == c2)
    print(c1 != c2)
