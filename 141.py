import math

def mediant(l1,l2):
	return [l1[0]+l2[0],l1[1]+l2[1]]

def farey(n,l1=[0,1],l2=[1,1]): # Returns Farey Sequence of order n between the fractions l1 and l2 # Needs mediant()
	[a,b]=l1
	[c,d]=l2
	f=[l1,l2]
	while True:
		i=len(f)-1
		change=False
		while i>0:
			if(mediant(f[i],f[i-1])[1]<=n):
				f.insert(i,mediant(f[i],f[i-1]))
				change=True
			i-=1
		if(change==False):
			return f

mu=[]
def setmobius(n):
	life=open("../Mobius Function.txt","r")
	x=0
	for i in range(0,n):
		x=int(((life.readline()).split(" "))[1])
		mu.append(x)

setmobius(100)

def S(n):
	return mu[n]

def round(n):
	return math.floor(n+0.5)

s=0
for i in range(1,100):
	s+=(i*S(i))%3
	print(i,s%3)


