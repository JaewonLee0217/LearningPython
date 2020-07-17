#1000미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

result = 0
for i in range(1,1000):
    
    if i % 3 ==0 or i % 5==0:
        result +=i
    
    
print(result)
