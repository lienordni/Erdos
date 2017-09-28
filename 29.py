import math

def p(n,k):
	# print(n,k)
	# input()
	if n==0 and k==0:
		return 0
	if n<=0 or k<=0:
		return 0
	if n==k:
		return 1
	# print("*")
	return p(n-1,k-1)+p(n-k,k)

def f(n):
	return math.factorial(n)

def ncr(n,r):
	return f(n)//(f(n-r)*f(r))

def parts(n,k):
	return ncr(n+k-1,k-1)

def a(n):
	return parts(n,n+1)

s=0
for i in range(1,61):
	print(i,a(i))
	s+=a(i)
print(s)
