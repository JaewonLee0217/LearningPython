def Fibo(n):
    arr = [0,1]
    i=0
    while (arr[i]+arr[i+1])<n:
        arr.append(arr[i+1]+arr[i])
        i+=1
    print(arr)

num = int(input("정수 n을 입력세요. 피노나치수열 출력!"))
Fibo(num)
