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

def func(l):
	count_late=0
	for i in l:
		if i==0:
			count_late+=1

	if(count_late>1):
		return False

	if(l==[2,2,2,2]):
		return False

	return True

y=[3,3,3,3]
x=[0,0,0,0]
count=0
for c in range(0,81):
	print(c,x)
	if(func(x)):
		count+=1
	inc(x,y)

print(count)
