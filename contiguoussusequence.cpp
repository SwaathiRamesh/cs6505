#include<iostream>
using namespace std;
int T[7];
 main(){
	 int A[]={5,10,-30,10,-5,40,10}, i;
	 
	 for(i=0;i<7;i++)
	 {
		 T[i]=(A[i]>=T[i-1]+A[i])?A[i]:T[i-1]+A[i];
	 }

	 int max;
	 for(i=0;i<7;i++)
		 max=(max>T[i])?max:T[i];
	 cout<<endl<<max;
}



