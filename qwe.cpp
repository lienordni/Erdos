#include "iostream"
#include "math.h"

using namespace std;

long long po(long long n, long long m, long long mod) {
     if(m == 0) return 1;
     if(m == 1) return n%mod;
     long long r = po(n,m/2,mod)%mod;
     if(m%2 == 0) return (r*r)%mod;
     return (((r*r)%mod)*n)%mod;
}
void foo(){
     unsigned long long i, res =1, m= 1000000 , c=0,j,res1 = 1, mod;
     mod = ceil(pow(10,9));
     cout<<mod<<endl;
     long long a =0 , a2 =0, a5=0;
     for(i= 1 ;i<=m;i++){
        j = i;
        while (j%10==0)    j /= 10;
        while (j%2==0)
        {
              j /= 2;
              a2++;
        }
        while (j%5==0)
        {
              j/=5;
              a5++;
        }
        res = (res * j ) % mod;
     }

    a=a2-a5;

    for (i = 1; i <= a; i++)
        res=(res * 2) %mod;
     for(i= 1;i<=1000000;i++){
        res1 = (res1 * res ) % mod;
     }
     cout<<res1<<endl;

}