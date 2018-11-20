from matrix import *
from vector import *
from rational import *
#task #6
#m1 = [[[1,2], [-2,7]],[[1,3], [2,8]]]
#print(m1)
print(3+6)
def tests():
	m1 = [[[1,2], [-2,7]],[[1,3], [2,8]]]
	m2 = [[[-1,3], [2,5]],[[2,7], [-1,7]]]
	m3 = [[[2,3], [1,4]],[[3,7], [1,7]]]
	result = __matmul__(m1, m2)
	print(result)
	print(__inverse__(m1))
	print("Associative test")
	r1 = __matmul__(__matmul__(m1, m2), m3)
	r2 = __matmul__(m1, __matmul__(m2, m3))
	print("r1 - r2 = " + (r1 - r2))
	print("Distributive test")
	print(__matmul__(m1, __add__(m2, m3)) - __add__(__matmul__(m1, m2), __matmul__(m1, m3)))
	print(__matmul__( __add__(m1, m2), m3) - __add__(__matmul__(m1, m3), __matmul__(m2, m3)))
	print("Composition of application test")
	v = [5,2]
	print(__matmul__(m1, __matmul__(m2, v)) -__matmul__(__matmul__(m1, m2), v))
	print("Determinant commutes over multiplication")
	print(determinant(m1) * determinant(m2) - determinant(__matmul__(m1, m2)))
	print("Indeed inverse")
	print(__matmul__(m1, __inverse__(m1)))
	print(__matmul__(__inverse__(m2), m2))


#print(A)
