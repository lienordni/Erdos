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

def check(f):
	for x in f:
		if x%4==1:
			return True
	return False

s=0
for i in range(1,101):
	f=primefac(i)[0]
	if check(f):
		print(i)
		s+=i

print(s)

