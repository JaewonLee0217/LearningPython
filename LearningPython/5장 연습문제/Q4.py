#filter 와 lambda 를 사용하여 리스트[1,-2,3,-4,8,-3]에서 음수를 모두 제거하라.

a = [1,-2,3,-4,8,-3]
a = list(filter(lambda x:x>0, a))
print(a)
