#include <iostream>

typedef long long lien;

lien F[200][200];

lien f(int m, int n) {
	// std::cout<<m<<" "<<n<<std::endl;
	lien x=1;

	if(m){
		if(F[m][n]!=-1)
			return F[m][n];

		if(m>n)
			return 0;

		if(2*m+1>n)
			return 1;

		for(int i=m;i<=n/2;++i){
			std::cout<<"this is f("<<m<<","<<n<<") calling f("<<i+1<<","<<n-i<<")"<<std::endl;
			x+=f(i+1,n-i);
		}

		F[m][n]=x;
		return x;
	}

	return f(1,n);

}

int main() {
	int i,j,m,n;

	for(i=0;i<200;++i)
		for(j=0;j<200;++j)
			F[i][j]=-1;

	std::cout<<f(0,196)<<std::endl;
}