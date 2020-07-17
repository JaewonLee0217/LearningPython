#총 게시물이 83개이고 한 페이지당 보여줄 수 있는 게시물을 5개라고 하자. 그럼 총 페이지수는 얼마가 되는가?

def getTotalPage(m,n):
    return m//n+1

print(getTotalPage(83,5))
    
