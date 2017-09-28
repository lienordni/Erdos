import math

def c(n,r):
	return math.gamma(1+n)//((math.gamma(1+r))*(math.gamma(1+n-r)))

def e(n,h,k):
	s=0
	r=list(range(max(0,k-h),1+(min(k,n-h))))
	for l in r:
		# print("l =",l)
		s+=(h-k+2*l)*c(h,k-l)*c(n-h,l)
		# print("done")
	s/=c(n,k)
	return s

prime=[]

def setprimes(n): # Needs prime[]
	life=open("./primes2.txt","r")
	x=0
	while True:
		x=int(life.readline())
		if x>n:
			return
		# print(x)
		prime.append(x)

setprimes(10**8)

for i in prime:
	print(i)

exit()

start=10
num=3
x=start
i=1
while(True):
	print(i,x)
	i+=1
	x=(e(start,x,num))
	input()
