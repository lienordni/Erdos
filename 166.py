import sys

def f(n):
	return 1+2**(2**n)

def sod(n):
	s=0
	c=n
	while c>0:
		s+=c%10
		c//=10

	return s

def g(n):
	return sod(f(n))%9

def ans(n):
	if(n%2==0):
		return 13*(n//2)

	return 13*(n//2)+5

print(ans(999999999999))
exit()

for i in range(1,31):
	print(i,g(i),ans(i))

# print(sod(int(sys.argv[1])))