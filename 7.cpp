#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <vector>

typedef long long lien;

lien DoubleExponential(lien x, lien n, lien m) {
	if(n==1)
		return (x*x)%m;

	lien y=DoubleExponential(x,n-1,m);
	return (y*y)%m;
}

int main(int argc, char* argv []) {

	lien x,y,s;
	lien m,n,p;
	// lien i,j;
	// m=atoll(argv[1]);
	// n=atoll(argv[2]);
	// p=13;
	s=0;
	// lien mod=atoll(argv[1]);

	// lien base=3;
	// for(int i=1;i<701;++i) {
	// 	s+=DoubleExponential(base,i,mod);
	// 	s%=mod;
	// 	std::cout<<s<<std::endl;
	// }
		

	// return 0;
	
	lien mod=23;

	for(y=1;y<=500;++y) {
		for(x=2;x<=10;++x) {
			s+=DoubleExponential(x,y,mod);
			s%=mod;
		}

		// std::cout<<"Sum till "<<y<<" = "<< s <<std::endl;
		std::cout<<s<<std::endl;
	}

	std::cout<<s<<std::endl;


}