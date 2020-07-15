#random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해보자.

import random

result = []

while len(result) <6:
    num = random.randint(1,45)
    if num not in result :
        result.append(num)

print(result)
