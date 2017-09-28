def convergent(cf): # Needs Nothing
	A=cf[0]
	a=cf[1]
	n=len(a)
	p=1
	q=a[n-1]
	for i in range(1,len(a)):
		pn=q
		qn=a[n-1-i]*q+p
		p=pn
		q=qn
	return [q*A+p,q]

p=convergent([0,[i for i in range(1,1001)]])[0]
q=convergent([0,[i for i in range(1,1001)]])[1]
print((p*q)%(7+10**9))
