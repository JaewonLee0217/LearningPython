import numpy

list_mat = [[1,2,3],[3,6,9],[2,4,6]]
lm = [1,2,3]
matrix = numpy.array(list_mat)
vec = numpy.array(lm)




print(matrix.dot(vec))
print(matrix)
print(matrix.shape)
print(vec)
numpy.savetxt("temp.txt",matrix)

a=numpy.loadtxt("temp.txt")

##############

X = None
W = None
b = None

X = numpy.array(X) # (N,D) n이 배치 사이즈고 D가 히든 디멘션
W = numpy.array(W) # (D, O)
b = numpy.array(b)# (O)

Y = X.dot(W).add(b) # 이게 fully connected layer가 된다.

# 그리디언트
dy = numpy.array(None)
dx = dy.dot(W.T)
dw = X.T.dot(Y)
db = dy.sum(1)
