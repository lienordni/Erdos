import math

def x(n):
	if n<2:
		return n
	if n%2==0:
		return (n//2)+x(n//4)
	else:
		return (n//2)+1+x(n//4)

print(x(4444444444))
exit()
for i in range(1,20):
	print(i,x(i))