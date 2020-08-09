class Flight:
    def __init__(self,number,passenger_num):
        self._number = number
        self._passenger_num = passenger_num

    def number(self):
        return self.__number
    def add_passenger(self,num):
        self._passenger_num +=num

#public 용도로 클래스, 변수를 선언하여 사용할 때는 언더바를 빼고 선언하시면 된다.
# Private 용도로 사용할 때에는 언더바를 두번 붙여서 이름을 지으시면 외부에서 참조가 불가능해진다.
# 이는 함수에 대해서도 마찬가지로 적용이 된다