#객체변수 value가 100이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator클래스를 만들어보자

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self,val):
        self.value += val


class MaxLimitCalculator(Calculator): ##즉 calculator의 add 메소드를 오버라이드 해서 조건을 넣어주어야 한다
   
    def add(self,val):
        self.value += val
        if self.value > 100 :
            self.value = 100

        

        
    
