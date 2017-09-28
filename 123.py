import math

def f(x,y):
	if x==y:
		return (math.sqrt(y))
	return math.sqrt(x*f(x+1,y))

for i in range(43,100):
	print("f(43,",i,"=",f(43,i))
