import math

pi=3.1415926535898

def area(b):
	if(b>=8):
		return 8*pi
	r1=4
	r2=min(math.sqrt(b*b+16)-4,4)
	r3=min(b-4,4-r2)
	return (pi/4)*(r1*r1+r2*r2+r3*r3)

s=0
for i in range(4,1001):
	s+=area(i)

print(s)