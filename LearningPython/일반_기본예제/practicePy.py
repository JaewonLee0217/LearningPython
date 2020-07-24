class animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def crawling(self):
        print("으르렁")
    def introduce(self):
        print("이 애완견의 이름은 "+self.name+"입니다")
        print("그리고 "+str(self.age)+"살 입니다")

class dog(animal):
    def love(self,to_master):
        print(to_master+"을 위해 충성합니다")

class lion(animal):
    def fight(self):
        print("건들면 싸웁니다")

lionking= lion("lionking",3)
lionking.crawling()
lionking.introduce()

hawl = dog("하울",4)
hawl.introduce()
hawl.love("재원")