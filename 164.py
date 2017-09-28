prime=[]

def setprimes(n): # Needs prime[]
	for x in range(2,n+1):
		if(x<11):
			if(x==2 or x==3 or x==5 or x==7):
				prime.append(x)
				continue
			else:
				continue

		i=0
		c=True
		while(prime[i]**2<=x):
			if(x%prime[i]==0):
				c=False
				break
			i+=1

		if(c):
			prime.append(x)

def exponent(n,p): # Exponent of prime p in n! # Needs nothing
	i=p
	s=0
	while True:
		if n//i==0:
			break
		s+=n//i
		i*=p
	return s

def factorial_factorization(n): # Needs setprimes()
	setprimes(n)
	bases=[]
	exponents=[]
	for	p in prime:
		bases.append(p)
		exponents.append(exponent(n,p))
	return [bases,exponents]

def pow(x,y,m=None):
	if m==None:
		if(y==0):
			return 1
		if(y==1):
			return x
		t=pow(x,y//2)
		if(y%2==0):
			return t*t
		return t*t*x

	if(y==0):
		return 1
	if(y==1):
		return x
	t=pow(x,y//2,m)
	if(y%2==0):
		return (t*t)%m
	return (t*t*x)%m

def power(a,b,m=None): # = product(a[i]**b[i]) # Needs Nothing
	if m==None:
		s=1
		for i in range(0,len(a)):
			s*=pow(a[i],b[i])
		return s

	s=1
	for i in range(0,len(a)):
		s*=pow(a[i],b[i],m)
		s%=m
	return s
  
k=9449771607341027425
mod=9449771616229914661

x=(factorial_factorization(100))

for i in range(0,len(x[1])):
	x[1][i]*=k

Y=(power(x[0],x[1],mod))
print(Y)
print(Y%1000000008)