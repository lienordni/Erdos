def totient_array(n): # Needs nothing
	phi=[0]+[1]+[i for i in range(2,n+1)]
	
	for i in range(2,n+1):
		if phi[i]==i:
			j=i
			while j<=n:
				phi[j]=(phi[j]//i)*(i-1)
				j+=i
	return phi

def totient_array2(n): # Needs nothing
	phi=[0]+[1]+[i for i in range(2,n+1)]
	phi2=[0]*(n+1)
	for i in range(2,n+1):
		if phi[i]==i:
			j=i
			while j<=n:
				phi[j]=(phi[j]//i)*(i-1)
				phi2[j]+=phi[i]
				j+=i
	

	return phi2

x=(totient_array(20))
y=(totient_array2(20))

for i in range(0,20):
	print(i,x[i],y[i])