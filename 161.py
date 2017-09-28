import math
import sys 

def nice(s):
	n=len(s)
	for i in range(0,n-1):
		if(s[i]==s[i+1] and s[i]=='1'):
			return False
	return True

def binary(n):
	return (bin(n)[2:])


def S(n):
	l=[]
	count=1
	for i in range(0,2**n):
		if(nice(binary(i))):
			print(count,binary(i),i)
			count+=1
			input()
			l.append(binary(i))
	return l

(S(30))
