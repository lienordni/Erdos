#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <algorithm>

typedef long long lien;

lien m;
lien lm;

lien powermodulo(lien x, lien y, lien n=m) {
	// std::cout<<x<<"  "<<y<<"  "<<n<<std::endl;
	if(y>lm)
		y%=lm;
	if(y==0)
		return 1;
	if(y==1)
		return x%n;
	lien z=powermodulo(x,y/2,n);
	if(y%2==0)
		return (z*z)%n;
	return (z*((x*z)%n))%n;
}

std::vector<lien> factors(lien x) {
	std::vector<lien> v;

	v.push_back(1);
	v.push_back(x);

	int i;
	for(i=2;i<=int(sqrt(x));++i){
		if(x%i==0){
			v.push_back(i);
			v.push_back(x/i);
		}
	}

	if(sqrt(x)==int(sqrt(x)))
		v.pop_back();

	std::sort(v.begin(),v.end());
	return v;

}

template <typename T>
void print(std::vector<T> v){
	for(int i=0;i<v.size();++i)
		std::cout<<v[i]<<" ";
	std::cout<<"\n";
}

lien doubleexponential(lien x, lien n=m) { // 2^2^x
	lien e=powermodulo(2,x,lm);
	// std::cout<<e<<std::endl;
	return powermodulo(2,e,n);

}

int main(int argc, char* argv[]){
	if(argc==1){
		m=1000000007;
		lm=500000003;
	}

	m=atoll(argv[1]);

	lien i=1;
	lien n=4;

	lien s=0;
	lien c=1;

	lien count=0;

	while(true){
		s+=n;
		s%=m;
		n=(n*n)%m;
		// if(i%100000==0 || true && 0)
		// 	std::cout<<i<<"  "<<s<<std::endl;
		
		if(s==0){
			// std::cout<<i<<"  "<<s<<std::endl;
			std::cout<<"----"<<count<<"  :  "<<c<<"----"<<std::endl;
			count++;
			c=0;
			// std::cin.get();
		}
		
		i++;
		c++;

	}

	// std::cout<<doubleexponential(1000)<<std::endl;

	

}