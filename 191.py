mod=10**9+7
prime=[]

def setprimes(n): # Needs prime[]
	life=open("./primes2.txt","r")
	x=0
	while True:
		x=int(life.readline())
		if x>n:
			return
		# print(x)
		prime.append(x)

setprimes(10**2)

def exponent(n,p): # Exponent of prime p in n! # Needs nothing
	i=p
	s=0
	while True:
		if n//i==0:
			break
		s+=n//i
		i*=p
	return s

def factorial_factorization(n): # Needs setprimes(), exponent()
	setprimes(n)
	bases=[]
	exponents=[]
	for	p in prime:
		if(p>n):
			break
		bases.append(p)
		exponents.append(exponent(n,p))
	prime.clear()
	return [bases,exponents]

def lienordni(n): # Awesome Lienordni Function (ALF)
	if(n<2047):
		return [2]
	if(n<1373653):
		return [2,3]
	if(n<9080191):
		return [31,73]
	if(n<25326001):
		return [2,3,5]
	if(n<4759123141):
		return [2,7,61]
	if(n<1122004669633):
		return [2,13,23,1662803]
	if(n<2152302898747):
		return [2,3,5,7,11]
	if(n<3474749660383):
		return [2,3,5,7,11,13]
	if(n<341550071728321):
		return [2,3,5,7,11,13,17]
	if(n<3825123056546413051):
		return [2,3,5,7,11,13,17,19,23]
	if(n<318665857834031151167461):
		return [2,3,5,7,11,13,17,19,23,29,31,37]
	if(n<3317044064679887385961981):
		return [2,3,5,7,11,13,17,19,23,29,31,37,41]

def power_modulo(x,y,n):
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=power_modulo(x,y//2,n)
		return (z*z)%n
	return (x*power_modulo(x,y-1,n))%n

def lienprime(n): # Needs lienordni() and power_modulo()
	if(n<2):
		return False
	if(n==2):
		return True
	d=n-1
	s=0
	while(d%2==0):
		d//=2
		s+=1
	
	for a in lienordni(n):
		x=power_modulo(a,d,n)
		if(x==1):
			continue
		over=False
		for r in range(0,s):
			if(x==n-1):
				over=True
				break
			x=(x*x)%n

		if(over):
			continue

		return False

	return True

prime=[]

def ncr_factors(n,r2): # Prime factorization of binomial_coefficients(n,r) # Needs lienprime() and exponent()
	if(r2<n-r2):
		r=r2
	else:
		r=n-r2
	s=0
	a=[]
	b=[]
	for i in range(2,r+1):
		if(lienprime(i)):
			e=exponent(n,i)-exponent(r,i)-exponent(n-r,i)				
			if(e>0):
				a+=[i]
				b+=[e]
	for i in range(r+1,n+1-r):
		if(lienprime(i)):
			e=exponent(n,i)-exponent(n-r,i)
			if(e>0):
				a+=[i]
				b+=[e]
	for i in range(n+1-r,n+1):
		if(lienprime(i)):
			e=exponent(n,i)
			if(e>0):
				a+=[i]
				b+=[e]
	return [a,b]

def extend(qwe,n):
	qwe[1]+=[0]*(n-len(qwe[1]))

def func(n,k):
	one=factorial_factorization(n+k)
	two=factorial_factorization(n-k)
	three=factorial_factorization(k)

	two[0]=one[0]
	three[0]=one[0]

	N=len(one[1])
	extend(two,N)
	extend(three,N)

	exp=[]

	for i in range(0,N):
		exp.append(one[1][i]-two[1][i]-2*three[1][i])

	return [one[0],exp]

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

def fuck(n):
	s=0
	for k in range(0,n+1):
		print(k)
		f=func(n,k)
		s+=power(f[0],f[1],mod)
		s%=mod
	return s

print(fuck(10**7))