from abc import *

class StudentBase(metaclass=ABCMeta): #추상클래스 : 메소드 목록만 가지고 있는 클래스
    @abstractmethod
    def study(self):
        pass
    @abstractmethod
    def go_to_school(self):
        pass
class Student(StudentBase):
    def study(self):
        print('공부하기')
    def go_to_school(self):
        print('학교가기')

#왜 쓰냐하냐면, 같은 이름의 메소드인데 다르게 기능을 출력하고 싶다