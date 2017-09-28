import os
import math 

prime=[]

def setprimes(n): # Needs prime[]
	for x in range(2,n+1):
		if(x<11):
			if(x==2 or x==3 or x==5 or x==7):
				prime.append(x)
				continue
			else:
				continue

		i=0
		c=True
		while(prime[i]**2<=x):
			if(x%prime[i]==0):
				c=False
				break
			i+=1

		if(c):
			prime.append(x)

def period(a):
	i=1
	a.reverse()
	while 3*i<=len(a):
		if a[i]==a[0] and a[2*i]==a[0] :
			repeat=True
			for j in range(1,i):
				if a[j]!=a[j+i] or a[j]!=a[j+2*i]:
					repeat=False
					break
			if repeat :
				a.reverse()
				q=0
				while True:
					if(a[q:(q+i)]==a[(q+i):(q+2*i)]):
						return [a[:q],a[q:(q+i)]]
					q+=1
		i+=1
	a.reverse()
	print("Not enough information")
	return 0

def power_modulo(x,y,n):
	if(x==1):
		return 1
	if(x==0):
		return 0
	if(y==0):
		return 1
	if(y==1):
		return x%n
	if(y%2==0):
		z=power_modulo(x,y//2,n)
		return (z*z)%n
	return (x*power_modulo(x,y-1,n))%n

setprimes(1000)

# num=int(input()
print('\n')
for mod in prime[5:]:
	# mod=257
	print(" "*40,"MODULO ",mod,end=" : \n")
	x=[[]]*(mod+2)
	for z in range(1,mod+1):
		x[z]=[]

	for i in range(1,400):
		for z in range(1,mod+1):
			x[z].append(power_modulo(z,2**i,mod))

	print()
	s=[0]*(mod+1)
	for z in range(1,mod+1):
		print(z,x[z][:22],sum(x[z][:mod])%mod)
	
	for q in range(1,mod+1):
		s[q]=0
		for z in range(1,mod+1):
			s[q]+=sum(x[z][:(q*mod)])%mod

	y=[[[],[]]]*(mod+2)
	for z in range(1,mod+1):
		y[z]=period(x[z])
	
	print()
	for z in range(1,mod+1):
		print("Base : ",z)
		print("Period :",len(y[z][0]),",",len(y[z][1])," "*12,end="Sum :  ")
		print(sum(y[z][0])," + [",sum(y[z][1]),"]")
		print()
	print("\nMod : ",mod)
	for q in range(1,mod):
		print("Sum ",q,": ",s[q]%mod)

	# print("_"*99)
	# if(s%mod!=0):
	input()
	# os.system("clear")