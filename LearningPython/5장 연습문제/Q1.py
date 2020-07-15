#클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus메소드를 만들자.

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


