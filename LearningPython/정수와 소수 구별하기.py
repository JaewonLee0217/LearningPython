#프로그래머 X는 입력값을 숫자를 입력하거나 문자를 입력하려고 하는데,
#1. 만약 숫자를 입력하였으면 그것이 정수인지, 소수인지 구별하는 프로그램 구현
#2. 만약 문자를 입력하였으면 숫자가 아니므로 math error를 표시하게 하라.
try:
    number =float(input("숫자를 입력하거나 문자를 입력하세요!"))
    key = number-int(number)
    if key == 0:
        print("이 수는 정수입니다")
    elif key <1:
        print(" 이 수는 소수입니다")
    
except:
    print("math error")

    
    
