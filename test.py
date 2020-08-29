import numpy

list_mat = [[1,2,3],[3,6,9],[2,4,6]]
matrix = numpy.array(list_mat)
print(matrix)
print(matrix.shape)

matrix = numpy.random.rand(3,3)
print(matrix)

matrix = numpy.zeros((3,3))
print(matrix)

numpy.savetxt("temp.txt",matrix)

a=numpy.loadtxt("temp.txt")
print(a)