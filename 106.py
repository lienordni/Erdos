def gcd(a,b): # Copied From Wikipedia, No fucking idea how it works.
	r=b
	old_r=a
	while r!=0:
		quotient= old_r//r

		prov=r
		r=old_r-quotient*prov
		old_r=prov

	return old_r

def interpolation(x,y,xn): # x and y are arrays. # Returns the y element corresponding to xn
	s=0
	n=len(x)
	for i in range(0,n):
		p=y[i]
		for j in range(0,n):
			if j==i:
				continue
			p*=(xn-x[j])/(x[i]-x[j])
		s+=p
	if s==int(s):
		return int(s)
	return s

def add(q,w):
	a,b,c,d=q[0],q[1],w[0],w[1]
	return [a*d+b*c,b*d]

def ADD(l):
	s=l[0]
	for i in range(1,len(l)):
		s=add(s,l[i])
	g=gcd(s[0],s[1])
	s[0]//=g
	s[1]//=g
	return s

def f(x):
	return ADD([[(283*(x**9)),7560],[-(943*(x**8)),576],[+(25969*(x**7)),840],[-(158077*(x**6)),480],[+(781127*(x**5)),360],[-(1749965*(x**4)),192],[+(183167009*(x**3)),7560],[-(28026817*(x**2)),720],[+(1421755*x),42],[-11908,1]])

l=[]
for i in range(-19,1):
	l.append(f(i))

print(ADD(l)[0]%(7+10**9))


