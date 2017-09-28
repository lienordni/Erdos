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

l=[]
p=13
for j in range(1,100):
	l+=[((fibonacci(j))**3)%p]

print(l)

exit()

def fibcubediff(n):
	for i in range(0,100):
		if(n<=l[i]):
			break

	for j in range(0,i):
		if(l[i]-l[j]==n):
			return True
	return False

# print(fibcubediff(18))


# exit()
for i in range(1,20):
	print(i,fibcubediff(fibonacci(3**i)-(fibonacci(i))**3))
