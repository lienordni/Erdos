import math

def totient_array(n): # Needs nothing
	phi=[0]+[1]+[i for i in range(2,n+1)]
	
	for i in range(2,n+1):
		if phi[i]==i:
			j=i
			while j<=n:
				phi[j]=(phi[j]//i)*(i-1)
				j+=i
	return phi

phi=totient_array(100002)

def primefac(n): # Needs math
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

def inc(x,y): # Increments a number array x with variable base array y # Needs nothing
	l=len(y)
	if(x[l-1]!=y[l-1]-1):
		x[l-1]+=1
		return x

	p=l-1
	while p>=0:
		if(x[p]!=y[p]-1):
			x[p]+=1
			for k in range(p+1,l):
				x[k]=0
			return x
		p-=1
	for i in range(0,l):
		x[i]=0
	return x

def power(a,b,m=None): # = product(a[i]**b[i]) # Needs Nothing
	if m==None:
		s=1
		for i in range(0,len(a)):
			s*=a[i]**b[i]
		return s

	s=1
	for i in range(0,len(a)):
		s*=(a[i]%m)**b[i]
		s%=m
	return s

def factors(n): # Needs primefac(), inc(), power(), math
	f=primefac(n)
	p=f[0]
	i=f[1]
	y=[]
	number=1
	for k in range(0,len(i)):
		y.append(i[k]+1)
		number*=i[k]+1
	x=[0]*len(p)
	ans=[]
	for k in range(0,number):
		ans.append(power(p,x))
		inc(x,y)
	ans.sort()
	return ans

def fact(n):
	return math.factorial(n)

def bla(n,e):
	return fact(n)//(fact(n-e)*fact(e))

def F(n):
	N=3*(n+1)
	s=0
	f=factors(N)
	for d in f:
		if 3*n/d==int(3*n/d):
			s+=phi[d]*bla(N//d,3*n//d)

	return s//N

a=F(100000)
b=F(100001)
print(a,'\n',b,'\n',a*b//2)

