import math

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

def factors(n): # Needs primefac(), inc(x,y), power(), math # Extremely fast for large composite numbers.
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

def nof(n):
	return len(factors(n))-1

def S(n):
	s=0
	for f in factors(n)[1:]:
		s+=(nof(f))
		# for i in (factors(f)[:-1]):
			# print("(",i,",",f,")")
	return s

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

setprimes(10000000)

def P(m,n):
	s=1
	for i in range(0,m):
		s*=prime[i]
	return s**n

def t(n):
	return n*(n+1)//2

def A(m,n):
	return (t(n+1))**m-(n+1)**m

def po2(n):
	count=0
	c=int(n)

	while(c%2==0):
		count+=1
		c//=2

	return count

def E(m,n):
	return po2(A(m,n))

def E2(m,n):
	if(n%4==1 or n%4==2):
		return 0

	if(n%4==0):
		return po2(n//2)
	
	return m*po2((n+1)//2)

def lienordni(n):
	c=int(n)
	s=0
	while(c):
		s+=c
		c//=2
	return s

number=904961

def Q(n,m=number):
	x=(m+1)*(lienordni(n//4))
	if(n%4==3):
		return x+m*po2((n+1)//2)
	return x

print(Q(8))
print(Q(10**14))
# exit()

# for n in range(2,51):
# 	print(n,S(n))
# 	input()

for m in range(2,401):
	s=0
	if(m%2==1):
		for n in range(1,501):
				s+=(E2(m,n))
				error=s-Q(n,m)
				# print(m,n,E2(m,n),error//m)
				if(error):
					print("FUCK")
					input()
					# exit()
	# input()