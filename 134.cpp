#include <iostream>
#include <math.h>
#include <stdlib.h>
#include "/home/lienordni/Desktop/Code/inc/matrix.h"
#include <algorithm>

int limit;

matrix<int> A(3,3), B(3,3), C(3,3);

bool check(std::vector<int> x) {
	return (x[0]*x[0]+x[1]*x[1]==x[2]*x[2]);
}

struct node {
	std::vector<int> v;
	node* a;
	node* b;
	node* c;

	node() {
		a=NULL;
		b=NULL;
		c=NULL;
	}

	node(std::vector<int> x) {
		v=x;
		a=NULL;
		b=NULL;
		c=NULL;
	}

};

void print(std::vector<int> v) {
	int i;
	for(i=0;i<v.size();++i)
		std::cout<<v[i]<<"  ";
	std::cout<<std::endl;
}

std::vector<int> HypotenuseNumbers;

void lien(node* rootPtr) {

	int h=rootPtr->v[2];

	HypotenuseNumbers.push_back(h);
	
	matrix<int> m=(MatrixOperations::VectorToMatrix(rootPtr->v));
	
	matrix<int> M[3];

	int i;
	std::vector<int> v;
	node* c;

	M[0]=A*m;
	M[1]=B*m;
	M[2]=C*m;

	for(i=0;i<3;++i) {
		v=MatrixOperations::MatrixToVector(M[i]);
		if(v[2]>limit)
			continue;
		// print(v[i]);
		c=new node(v);
		lien(c);
	}
}

void lien(std::vector<int> x) {
	std::cout<<std::endl;
	print(x);
	// std::cout<<check(x)<<std::endl;
	HypotenuseNumbers.push_back(x[2]);
	std::cout<<"size : "<<HypotenuseNumbers.size()<<std::endl;
	matrix<int> m=(MatrixOperations::VectorToMatrix(x));
	
	matrix<int> M[3];

	int i;
	std::vector<int> v;

	M[0]=A*m;
	M[1]=B*m;
	M[2]=C*m;

	for(i=0;i<3;++i) {
		v=MatrixOperations::MatrixToVector(M[i]);
		std::cout<<"    :  ";
		print(v);
		if(v[2]>limit)
			continue;
		// print(v[i]);
		lien(v);
	}
}

int main(int argc, char* argv[]) {

	A.SetElement(0,0,-1);
	A.SetElement(0,1,2);
	A.SetElement(0,2,2);
	A.SetElement(1,0,-2);
	A.SetElement(1,1,1);
	A.SetElement(1,2,2);
	A.SetElement(2,0,-2);
	A.SetElement(2,1,2);
	A.SetElement(2,2,3);

	B.SetElement(0,0,1);
	B.SetElement(0,1,2);
	B.SetElement(0,2,2);
	B.SetElement(1,0,2);
	B.SetElement(1,1,1);
	B.SetElement(1,2,2);
	B.SetElement(2,0,2);
	B.SetElement(2,1,2);
	B.SetElement(2,2,3);

	C.SetElement(0,0,1);
	C.SetElement(0,1,-2);
	C.SetElement(0,2,2);
	C.SetElement(1,0,2);
	C.SetElement(1,1,-1);
	C.SetElement(1,2,2);
	C.SetElement(2,0,2);
	C.SetElement(2,1,-2);
	C.SetElement(2,2,3);

	// A.print('\n');
	// B.print('\n');
	// C.print('\n');

	limit=((argc==2)?atoi(argv[1]):100);


	node* rootPtr=new node;
	rootPtr->v={3,4,5};

	// HypotenuseNumbers.push_back(5);
	lien(rootPtr->v);

	std::sort(HypotenuseNumbers.begin(), HypotenuseNumbers.end());

	// print(HypotenuseNumbers);

}

