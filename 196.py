def count(a,b,c,d):
	q=0
	if(b<=a):
		q+=1
	if(c<=a):
		q+=1
	if(d<=a):
		q+=1
	return q

cunt=0
for a in range(0,4):
	for b in range(0,4):
		for c in range(0,4):
			for d in range(0,4):
				if(a+b+c+d==3):
					print(a,b,c,d,count(a,b,c,d))
					cunt+=count(a,b,c,d)
print(cunt)


print((13**20)%(7+10**9))