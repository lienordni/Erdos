import math

a=3*(10**6)//4
b=2000

def q(x,b=2000):
	return b*x-x*x/2

z=(a*math.log(3)+q(500)+q(2000)-q(0)-q(1500))
print(z//100)
