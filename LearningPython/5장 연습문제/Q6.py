#map과 lambda를 사용하여 [1,2,3,4]라는 리스트의 각 요솟값에 3이 곱해진 리스트[3,6,9,12]를 만들어보자.

a = [1,2,3,4]
a = list(map(lambda x:x*3 , a))
print(a)
