n=5
s=0
for n in range(3,16):
	s=0
	for i in range(0,n+1):
		for j in range(0,n+1):
			s+=i^j

	print(n,s)