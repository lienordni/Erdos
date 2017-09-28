import math

def check(a,b,c):
	return c*c==a*a+b*b
'''
for p in range(1,5):
	for q in range(1,100):
		h=p*q*q
		if p%2==0:
			d=p*q
		else:
			d=2*p*q
		for k in range(int(math.sqrt(2)*h/d)+1,100):
			a=h+d*k
			b=int(d*k+(d*d*k*k)/(2*h))
			c=int(h+d*k+(d*d*k*k)/(2*h))
			print(p,q,h,d,k,":",a,b,c,check(a,b,c))
			# if check(a,b,c)==False:
			input()
'''

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


s=1

def position(x,l): # Needs nothing
	if(len(l)==0):
		return None
	if(len(l)==1 and l[0]==x):
		return [0,True]
	low=0
	high=len(l)-1
	if(x==l[low]):
		return [low+1,True]
	if x==l[high]:
		return [high+1,True]
	if(x>l[high]):
		return [high+1,False]
	while True:
		mid=(low+high)//2
		if(mid==low):
			return [low+1,False]

		if(x>l[mid]):
			low=mid
			continue
		elif(x<l[mid]):
			high=mid
			continue
		else:
			return [mid,True]

'''
print(position(7,[1,3,4,5,6,8,9]))
exit()
'''
def ins(x,a):
	if len(a)==0:
		a.append(x)
		return
	if len(a)==1 and x>=a[0]:
		a.append(x)
		return
	if len(a)==1 and x<a[0]:
		a.append(a[0])
		a[0]=x
		return	 
	y=position(x,a)
	if y[1]:
		return
	a.insert(y[0],x)
	# print("Position : ",y[0])

'''
a=[5]
b=[6,13,7,20,14,15,21]

for i in b:
	ins(i,a)
	print(a)
	input()
exit()
'''

a=[]
while s<=10**4:
	t=s+2
	while t<=10**4:
		print(t*s,((t*t)-(s*s))//2,((t*t)+(s*s))//2,primefac(((t*t)+(s*s))//2))
		# input()
		if ((t*t)+(s*s))//2<=10**8:
			c=((t*t)+(s*s))//2
			for q in range(1,1+(10**8)//c):
				ins(c*q,a)
			print(c)
			# input()
		t+=2
	print(s)
	s+=2

print(sum(a))
# print(a[-1])
