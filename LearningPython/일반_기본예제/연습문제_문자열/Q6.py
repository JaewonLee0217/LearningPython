#url = portal.ac.kr 에서kr만출력하세요. (split함수사용)

url = "portal.ac.kr"

a = url.split(".")
print(a[-1])
