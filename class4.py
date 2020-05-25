def cube(n=0):
	"""
	Input: an integer
	Returns the cube value of the given number
	"""
	return n*n*n

def f2(x, y=23):
	print(f"x={x}, y={y}")

def f1(x, y):
	print(f"x={x} y={y}")
	return 4

def add(*paras, **kargs):
	sum = 0
	for n in paras:
		sum += n;
	print(f"triangle={triangle}")
	return sum

#nbr = 9
#print("nbr: {0}".format(cube(nbr))) 
#print("nbr: {0}".format(cube()))
#print("f1: {0}".format(f1(x=1,y=2)))
print(add(2, -6))
print(add(3, 1, 4, 1, 5, 8, 6))
print(add(1, 2, triangle=3))