import sys
import math

lien=500000003

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


if(len(sys.argv)==2):
	m=int(sys.argv[1])

else:
	m=7+10**9

G=[-1]*12345680
F=[-1]*12345680
FF=[-1]*12345680


def g(x):
	if(G[x]!=-1):
		return G[x]

	e=2*power_modulo(x,3,lien)
	e%=lien
	z=power_modulo(2,e)-1
	G[x]=z%m

	return G[x]

def f(x):

	if(F[x]!=-1):
		return F[x]


	s=0
	for i in range(1,x+1):
		# print(i)
		s+=g(x//i)
		s%=m
		# print(i,z,s)
	F[x]=s
	return s;


def ff(x):
	if(FF[x]!=-1):
		return FF[x]

	s=0
	for i in range(1,x+1):
		if(i%1000==0):
			print(i)
		s+=f(i)
		s%=m

	FF[x]=s
	return s

def power_modulo(x,y,n=m):
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=power_modulo(x,y//2,n)
		return (z*z)%n
	return (x*power_modulo(x,y-1,n))%n


# t=2
# c=1
# while(True):
# 	print(c,t)
# 	if(t==1):
# 		input()
# 	t*=2
# 	t%=m
# 	c+=1

# for i in factors(m-1):
# 	z=power_modulo(2,i)
# 	if(z==1):
# 		print(i)
# exit()


print(ff(12345678))
exit()

s=0
for i in range(1,1000):
	q=f(i)
	s+=q
	s%=m
	print(i,q,s,end="")
	if s==0:
		input()
	else:
		print()
