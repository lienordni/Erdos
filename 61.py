M=7+10**9

def modulo_inverse(a,b): # Copied from Wikipedia. No fucking idea how it works.
    s=0
    old_s=1
    r=b
    old_r=a
    while r!=0:
        quotient= old_r//r

        prov=r
        r=old_r-quotient*prov
        old_r=prov

        prov=s
        s=old_s-quotient*prov
        old_s=prov

    if(old_s<0):
        return old_s+b
    return old_s

def factorial_modulo(n,modulus): # Might need modulo_inverse()
    if n>=modulus :
        return 0

    ans=1
    if n <= modulus//2:
        # Calculate the factorial normally (right argument of range() is exclusive)
        for i in range(1,n+1):
            ans = (ans * i) % modulus   
    else:
        # Fancypants method for large n
        for i in range(n+1,modulus):
            ans = (ans * i) % modulus
        ans = modulo_inverse(ans, modulus)
        ans = -1*ans + modulus
    return ans % modulus

# print(factorial_modulo(654,1000000007))

def A(n,k):
    b=factorial_modulo(n-k,M)
    c=1

    s=(((-1)**(k+1))*b*c)%M

    for m in range(1,k):
        b=(b*(n+m-k)*modulo_inverse(m,M))%M
        c=(c*(k+1-m))%M
        s=(s+(((-1)**(k+1-m))*b*c))%M
    return s

def S(n,k):
    return (factorial_modulo(n,M)-A(n,k))%M

print(S(654321,123456))
