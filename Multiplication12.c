#include <stdio.h>
int main(int argc, const char * argv[]){
	int base [10];
	int i,j=1,res;
	do{
		for(i = 0; i < 10; i++){
			base[i] = i+1;
			res = base[i]*j;
			if (res < 10){
				printf("   %i",res);
			}
			if (res < 100){
				printf("  %i",res);
			}
			else{
				printf(" %i",res);
			}
		}
		j++;
	}while(j < 13);
	return 0;
}