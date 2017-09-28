#include <iostream>

typedef long long lien;

lien power(lien n,lien k,lien m){
	if(k==0)
		return 1;
	if(k==1)
		return n%m;

	lien t=power(n,k/2,m);

	if(k%2==0)
		return (t*t)%m;

	lien p=(t*n)%m;
	return (p*t)%m;
}

int main() {
	lien m=1000000007;
	lien limit=1000000000;
	lien exp=1000000;
	lien s=0;
	int i;
	for(i=1;i<=limit;++i){
		if(i%1000000==0)
			std::cout<<i<<std::endl;
		s+=power(i,exp,m);
		s%=m;
	}

	std::cout<<s<<std::endl;
	
}