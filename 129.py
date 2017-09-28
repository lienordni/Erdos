import math

def lithium(a,b): # 2x2 Matrix Multiplication 
	return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]]

def rhenium(x,y,n=None):	# 2x2 Modular Matrix Exponentiation, Needs Lithium()
	if n is None:
		if(y==0):
			return [1,0,0,1];
		if(y==1):
			return x
		if(y%2==0):
			z=rhenium(x,y//2)
			return lithium(z,z)

		return lithium(rhenium(x,y-1,n),x)


	else:
		if(y==0):
			return [1,0,0,1];
		if(y==1):
			z=[]
			for i in range(0,4):
				z.append(x[i]%n)
			return z
		if(y%2==0):
			z=rhenium(x,y//2,n)
			p=(lithium(z,z))
			q=[]
			for i in range(0,4):
				q.append(p[i]%n)
			return q

		f=lithium(rhenium(x,y-1,n),x)
		g=[]
		for i in range(0,4):
			g.append(f[i]%n)
		return g

def fibonacci(n,m=None): #Needs lithium(), rhenium()
	a=[1,1,1,0]

	if m is None:
		b=rhenium(a,n)
	else:
		b=rhenium(a,n,m)

	return b[1]

def f(n):
	return fibonacci(n+1)

phi=(1+math.sqrt(5))/2

def isfibo(i):
	return invfib(i)==int(invfib(i))

def nfsum(n):
	return n*fibonacci(n+2)-fibonacci(n+3)+2

def invfib(n):
	a=int(math.log(math.sqrt(5)*(n+0.5),phi))
	b=int(math.log(math.sqrt(5)*(n-0.5),phi))
	if a!=b:
		return a
	return (math.log(math.sqrt(5)*(n+0.5),phi))

def lastfibo(n):
	return fibonacci(int(invfib(n)))

def gee(n):
	if n<4:
		return n
	if isfibo(n):
		return G[invfib(n)]
	l=lastfibo(n)
	return (n-l)+gee(n-l)+gee(l)

G=[-1]*(66)
def g(n):
	i=invfib(n)
	if G[i]!=-1:
		return G[i]
	if n<4:
		return n
	if isfibo(n):
		q=fibonacci(i-2)
		G[i]=g(n-q)+g(q)+q-1
		return G[i]
	x=fibonacci(int(i))
	G[n]=g(n-x)+g(x)+n-x
	return G[n]

def fragger(n):
	c=n
	l=[]
	while c>0:
		q=lastfibo(c)
		l.append(invfib(q))
		c-=q
	s=[0]*l[0]
	for i in l:
		s[i-1]=1
	s.reverse()
	s.pop()
	return s

def countones(l):
	c=0
	for i in l:
		if i==1:
			c+=1
	return c

for i in range(1,100):
	x=fibonacci(i+2)
	g(x)
	if nfsum(i)>10**15:
		break
x=5703724904740
print(gee(fibonacci(64)+x))
exit()
w=fragger(fibonacci(64)+x+1)
w.pop()
w.pop()
w.pop()
w.pop()
w.pop()
w.pop()
w.pop()
w.pop()
w.pop()
print(w,len(w),countones(w))
exit()

# 285275069672862+13

'''
Until fibonacci( 64 ) = 10610209857723 ,
Total number of digits : 640665331001326 '
Total number of ones : 183441668320643 

Until fibonacci( 65 ) = 17167680177565 ,
Total number of digits : 1053785961151373 '
Total number of ones : 301559884395266 
'''
