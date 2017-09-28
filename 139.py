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
print(sum([6,28,496,8128,33550336,8589869056,137438691328,2305843008139952128])%(7+10**9))