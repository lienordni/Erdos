import math

# x= 194163712

def primefac(n): # Needs nothing
	d=2
	i=-1
	factors=[]
	indices=[]
	while(n>1):
		if(n%d==0):
			i+=1
			factors.append(d)
			indices.append(0)
		while(n%d==0):
			indices[i]+=1
			n//=d
		d+=1
		if(d>int(math.sqrt(n))):
			break
	if(n>1):
		factors.append(n)
		indices.append(1)
	return [factors,indices]


def f(n):
	pf=primefac(n)
	primes=pf[0]
	exp=pf[1]
	product=1
	for i in range(0,len(primes)):
		product*=(primes[i]**(2*exp[i]+2)-1)//(primes[i]**2-1)
	return product

lim=10
s=0
for i in range(1,lim+1):
	s+=f(i)
	print(i,f(i),s)
