import math

def ca(s):
	l=list(s)
	c=0
	for i in l:
		if i=='a':
			c+=1
	return c

def cb(s):
	l=list(s)
	c=0
	for i in l:
		if i=='b':
			c+=1
	return c

def ishappy(s):
	return ca(s)>cb(s)

def happy(n):
	if n==1:
		return ["a"]
	if n==2:
		return ["aa"]
	l=[]
	for x in happy(n-1):
		# print(x)
		s1=x+"a"
		s2=x+"b"
		# print(s1,s2)
		# if(ca(s1)==2*cb(s1)):
		l.append(s1)
		if ishappy(s2):
			l.append(s2)
	return l

def half(l):
	c=0
	for s in l:
		if ca(s)==2*cb(s):
			c+=1
	return c

def f(n):
	return math.factorial(n)

def c(n,r):
	return f(n)//(f(r)*f(n-r))

for i in range(4,100):
	print(i,half(happy(i)),c(3*(i//3)-1,(i//3)-1))