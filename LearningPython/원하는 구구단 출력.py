def GuGu(num):
    result = []
    i=1
    while i<10 :
        result.append(num*i)
        i+=1
    return result

num = int(input("원하는 단의 숫자를 입력하세요"))
print(GuGu(num))


#input함수는 다른 언어와 달리 'num'문자열 처리가 되기 때문에 int형으로 형변환해야 한다는 것을 주의하자.

    

    
