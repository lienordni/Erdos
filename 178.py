import math
import time
prime=[]

def setprimes(n):
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

def iss(x):
	return (int(math.sqrt(x))**2==x)

'''
for i in range(0,100):
	print(i,iss(i))

exit(0)
'''

def condom(i,j):
	if(len(i)==0):
		return j

	if(len(i)==1):
		a=i[0][0]
		b=i[0][1]
		c=j[0][0]
		d=j[0][1]
		e=int(math.fabs(b*d-a*c))
		f=a*d+b*c
		g=int(math.fabs(a*d-b*c))
		h=b*d+a*c
		
		if(e<f):
			l1=[e,f]
		else:
			l1=[f,e]
		if(g<h):
			l2=[g,h]
		else:
			l2=[g,h]

		l=[l1,l2]
#		if(int(math.fabs(b*d-a*c))>a*d+b*c or int(math.fabs(a*d-b*c))>b*d+a*c):
#			return 5
		return l;

#	return 5

	crap=[]
	for fuck in i:
		crap+=condom([fuck],j)
	return crap

'''
q=[[4,7],[1,8]]
w=[[1,4]]

print(condom(q,w))
exit(0)
'''

def sutta(x):
	for a in range(0,int(math.sqrt(x/2)+1)):
		if(iss(x-a**2)):	
			return[[a,int(math.sqrt(x-a**2))]]

'''
print(sutta(5))
print(sutta(13))
exit(0)
'''

def mofo(vagina):
	cum=0
	for dick in vagina:
		cum+=dick[0]
	return cum

'''
print(mofo([[1,3],[4,7],[9,10]]))
exit(0)
'''

start=time.clock()

setprimes(123)

c=0
p=1
lien=[]
for i in range(0,len(prime)):
	if(prime[i]%4==1):
		lien.append(prime[i])

print(len(lien))
print(lien)




#		print(prime[i])
#		c+=1;
#		p*=prime[i];

#print(c)
#print(p)
#print(math.log10(p))
#print(bin(69))
#print(lien)
#exit(0)

#yo_mama=[]
lienordni=0
size=2**14
for i in range(1,size):
	s=bin(i)
	lol=[int(x) for x in s[2:]]
	yolo=[0]*(14-len(lol))+lol
	
#	yolo.reverse()

#	print(lien)
#	print(yolo)
	
#	yolo=[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#	p=1
	ass=[]
	for n in range(0,len(yolo)):
		if(yolo[n]==1):
#			p*=lien[n]
			ass=condom(ass,sutta(lien[n]))

#	print(i)
	lienordni+=mofo(ass)
#	yo_mama.append(p)

#	if(i%1000==0):
#		print(i)
#	print(p)
#	print(i,p," +",mofo(ass)," =",lienordni,end="")
#	print(ass)
#	print(mofo(ass))
#	print(lienordni)
#	print()
#	input()

end=time.clock()
brrr=open("273.txt","w")
brrr.write(str(lienordni))
print()
print(end-start)
'''
yo_mama.sort()
#exit(0)

for i in range(0,size):
#	print(i,"=")
	count=0
	for a in range(0,int(math.sqrt(yo_mama[i]/2)+1)):
		if(iss(yo_mama[i]-a**2)):	
			if(count>0):
				print(' '*(int(math.log10(yo_mama[i]))+3),a,"^2 + ",int(math.sqrt(yo_mama[i]-a**2)),"^2",end="")
			else:
				print(yo_mama[i],"=",a,"^2 + ",int(math.sqrt(yo_mama[i]-a**2)),"^2",end="")
			count+=1
			if(count>=0):
				input()
			else:
				print()
'''
'''
#	if(yes==False):
#		print("nothing")
	if(yes):
		print(i,"=")
		input()



for i in range(0,size):
	print(yo_mama[i],"=")
	yes=False
	for a in range(0,int(math.sqrt(yo_mama[i])/2+1)):
		if(iss(yo_mama[i]-a**2)):	
			print(a,"^2 + ",int(math.sqrt(yo_mama[i]-a**2)),"^2")
			yes=True
	if(yes==False):
		print("nothing")
	input()
'''
