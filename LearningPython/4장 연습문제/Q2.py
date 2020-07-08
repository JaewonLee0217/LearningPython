#입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
#함수 이름은 avg_numbers

def avg_numbers(*nums): #nums라는 배열을 가리키는 포인터
    result = 0
    for a in nums:
        result +=a
    return result/len(nums)

    
