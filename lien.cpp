class lien {
	
public:

	std::vector<ll> e;
	int no_of_primes;

	lien();
	lien(ll);

	ll value(ll);
	ll value();
	void print();

	void append(ll);

	void operator=(lien);
	lien operator*(lien);
	lien operator/(lien);
	lien operator^(ll);

	void trim();

};

lien::lien() {
	e.clear();
	no_of_primes=0;
}

lien::lien(ll n) {
	ll i=0,prime;
	while(true){
		prime=primes[i];

		if(prime>n){
			break;
		}

		ll exp=0,c=n;
		while(c) {
			c/=prime;
			exp+=c;
		}

		e.push_back(exp);
		i++;
		if(i==5761455){
			break;
		}
	}

	no_of_primes=i;
	return;

}	

void lien::print(){
	ll i,n=no_of_primes;

	// std::cout<<n<<std::endl;

	std::cout<<"{";
	for(i=0;i<n-1;++i)
		std::cout<<primes[i]<<",";
	std::cout<<primes[n-1]<<"}"<<std::endl;

	std::cout<<"{";
	for(i=0;i<n-1;++i)
		std::cout<<e[i]<<",";
	std::cout<<e[n-1]<<"}"<<std::endl;
	std::cout<<std::endl;
}

ll lien::value(ll mod){
	ll val=1;
	ll n=no_of_primes,i;

	for(i=0;i<n;++i) {
		val*=power(primes[i],e[i],mod);
		if(val<0){
			std::cout<<"FUCK"<<std::endl<<primes[i]<<"  "<<e[i]<<"  "<<mod<<"  "<<power(primes[i],e[i],mod);
			std::cin.get();
		}
		val%=mod;
	}

	return val;
}

ll lien::value(){
	ll val=1;
	ll n=no_of_primes,i;

	for(i=0;i<n;++i) {
		val*=power(primes[i],e[i]);
		if(val<0){
			std::cout<<"FUCK"<<std::endl<<primes[i]<<"  "<<e[i]<<"  "<<power(primes[i],e[i]);
			std::cin.get();
		}
	}

	return val;
}

void lien::append(ll y) {
	no_of_primes++;
	e.push_back(y);
}

void lien::operator=(lien x) {
	no_of_primes=x.no_of_primes;
	e=x.e;
}

lien lien::operator*(lien x) {
	int s1=no_of_primes, s2=x.no_of_primes;
	int i;

	std::vector<ll> *e2=&(x.e);

	std::vector<ll> *max, *min;

	if(s1>=s2){
		max=&e;
		min=e2;
	}

	else {
		max=e2;
		min=&e;
	}

	lien z;

	i=0;

	while(i<min->size()) {
		z.append(e[i]+(*e2)[i]);
		i++;
	}

	while(i<max->size()) {
		z.append((*max)[i]);
		i++;
	}

	z.trim();

	return z;
}

lien lien::operator/(lien x) {
	int s1=no_of_primes, s2=x.no_of_primes;
	int i;

	std::vector<ll> *e2=&(x.e);

	lien z;

	if(s1>=s2){
		i=0;
		while(i<s2){
			z.append(e[i]-(*e2)[i]);
			i++;
		}

		while(i<s1) {
			z.append(e[i]);
			i++;
		}
	}

	else{
		i=0;
		while(i<s1){			
			z.append(e[i]-(*e2)[i]);
			i++;
		}

		while(i<s2){
			z.append(-(*e2)[i]);
			i++;
		}
	}

	z.trim();

	return z;
}

lien lien::operator^(ll n){
	lien z;

	if(n==0)
		return z;

	for(int i=0;i<no_of_primes;++i)
		z.append(e[i]*n);

	z.trim();

	return z;
}

void lien::trim() {
	while(e[no_of_primes-1]==0)
		no_of_primes--;
}