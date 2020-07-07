coffee = 10
while True:
    money = int(input("자판기에 돈을 넣어주세요"))
    if money ==300:
        print("커피를 줍니다")
        coffee -=1
    elif money>=300:
        print("거스름돈 %d원을 주고 커피를 드립니다."%(money-300))
    else:
        print("돈을 더 넣어주세요")
        print("남은 커피의 양은 %d개입니다."% coffee)
    if coffee==300:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

    
