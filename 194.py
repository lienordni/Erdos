import math

def power_modulo(x,y,n):
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=power_modulo(x,y//2,n)
		return (z*z)%n
	return (x*power_modulo(x,y-1,n))%n

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

def perfect(n):
	return n==(int(math.sqrt(n)))**2

def qwe(n):
	count=0
	for i in range(0,n+1):
		if(i*i>n):
			break
		if(perfect(n-i*i)):
			count+=1
	return count

def f(a,d,k):
	bases=[2,3,5,17,79,509,859,1123,2017]
	exp=[3*k,2*a+k,a,k,a,a,a,d]
	pf=[bases,exp]
	for i in range(0,len(pf[0])):
		if(pf[0][i]%4==3 and pf[1][i]%2==1):
			return 0

	p=4

	for i in range(0,len(pf[0])):
		if(pf[0][0]==2):
			continue

		if(pf[0][i]%4==1):
			p*=(1+pf[1][i])

	return p

# 3^2×5×79×509×859×1123
# 2017
# 2^3×3×17

s=0
for a in range(1,101):
	for d in range(1,101):
		for k in range(1,101):
			s+=power_modulo(a*d*k,f(a,d,k),7+10**9)
			s%=7+10**9

print(s)
