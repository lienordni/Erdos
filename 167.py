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

def sod(n):
	s=n
	for i in range(1,n//2+1):
		if(n%i==0):
			s+=i
	return s

def threeperfect(n):
	return (sod(n)==3*n)

l=[120,672,523776,459818240,1476304896,51001180160]

for i in l:
	print(i,primefac(i))