#include <iostream>
#include <vector>
#include <stdlib.h>
#include <fstream>

typedef long long ll;

std::vector<ll> primes;

ll power(ll x,ll y,ll m) {

	if(y==0)
		return 1;
	
	if(y==1) 
		return x%m;

	ll z=power(x,y/2,m);

	if(y%2==0)
		return (z*z)%m;

	ll t=(x*z)%m;
	return (z*t)%m;
	
}

ll power(ll x, ll y) {
	
	if(y==0)
		return 1;

	if(y==1)
		return x;

	ll z=power(x,y/2);

	if(y%2==0)
		return z*z;
	
	return z*z*x;

}

#include "./lien.cpp"

lien ncr(ll n, ll r) {
	lien a(n),b(r),c(n-r);
	return (a/(b*c));
}

int main(int argc, char* argv[]){
	std::fstream fin("./153.out", std::ios::in);
	ll prime;
	while(fin){
		fin>>prime;
		primes.push_back(prime);
	}

	int n=primes.size();
	primes.pop_back();

	lien z=ncr(1403,52);	
	z.print();
	// std::cout<<z.value()<<std::endl;
	return 0;
	// std::cout<<qwe.value(128517281)<<std::endl;
}

