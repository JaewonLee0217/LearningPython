class Flight:
    def __init__(self,number,passenger_num):
        self._number = number
        self._passenger_num = passenger_num

    def number(self):
        return self._number
    def add_passenger(self,num):
        self._passenger_num +=num