class Date:
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    def getDay(self):
        return self._day

    def getYear(self):
        return self._year

    def getMonth(self):
        return self._month
