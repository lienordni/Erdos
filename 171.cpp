#include <iostream>
#include <stdlib.h>

typedef long long lien;

lien m;
lien lm;

lien powermodulo(lien x, lien y, lien n=m) {
	// std::cout<<x<<"  "<<y<<"  "<<n<<std::endl;
	if(y==0)
		return 1;
	if(y==1)
		return x%n;
	lien z=powermodulo(x,y/2,n);
	if(y%2==0)
		return (z*z)%n;
	return (z*((x*z)%n))%n;
}


lien G[12345680];

lien g(lien x){
	// std::cout<<"G"<<x<<std::endl;

	if(G[x]!=-1)
		return G[x];
	lien e=2*powermodulo(x,3,lm);
	// std::cout<<"G"<<x<<std::endl;
	e%=lm;
	lien z=powermodulo(2,e)-1;
	z%=m;
	G[x]=z;
	return z;
}

lien F[12345680];

lien f(lien x) {
	if(F[x]!=-1)
		return F[x];
	// std::cout<<"F"<<x<<std::endl;

	lien s=0;
	for(int i=1;i<=x;++i){
		s+=g(x/i);
		s%=m;
	}
	F[x]=s;
	return s;
}

lien FF[12345680];

lien ff(lien x) {
	if(FF[x]!=-1)
		return FF[x];
	// std::cout<<"FF"<<x<<std::endl;

	lien s=0;
	for(int i=1;i<=x;++i){
		// if(i%1000==0)
		s+=f(i);
		s%=m;
		if(s==0){
			std::cout<<i<<"  "<<s<<std::endl;
			std::cin.get();
		}
	}
	FF[x]=s;
	return s;
}

int main(int argc, char* argv[]) {
	
	lien size=12345680;

	for(int i=0;i<size;++i){
		G[i]=-1;
		F[i]=-1;
		FF[i]=-1;
	}

	m=19;
	lm=18;
	std::cout<<ff(12345678)<<std::endl;

}

