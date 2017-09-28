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

setprimes(10**7)
n=664579
# n=10
count=0
asasda=0
for i in range(0,n):
	for j in range(i,n):
		# print(prime[i],prime[j],prime[i]*prime[j])
		product=prime[i]*prime[j]
		if(product>10**7):
			break
		asasda+=product
		# print(count)
		# print()
		# input()

print(asasda)
