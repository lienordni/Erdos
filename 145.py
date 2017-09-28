def inc(x,low,up): # Increments a number array x with variable base array ranges low->up # Needs nothing
	l=len(up)
	if(x[l-1]!=up[l-1]-1):
		x[l-1]+=1
		return
	p=l-1
	while p>=0:
		if(x[p]!=up[p]-1):
			x[p]+=1
			for k in range(p+1,l):
				x[k]=low[k]
			return
		p-=1
	for i in range(0,l):
		x[i]=low[i]
	return

low=[1,1,1,1,1]
high=[7,7,7,7,7]
x=[1,1,1,1,1]

def check1(a):
	x=list(a)
	x.sort()
	for i in range(0,4):
		if x[i]==x[i+1]:
			return False
	return True

def check2(a):
	for i in range(0,5):
		if i+1==a[i]:
			return False
	return True	

def check3(a):
	if a[0]==6:
		return False
	return True

count=0
for i in range(0,7776):
	if check1(x) and check2(x) and check3(x):
		print(x)
		count+=1
	inc(x,low,high)
print(count)

