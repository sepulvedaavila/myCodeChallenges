#include <stdio.h>
#include <string.h>

int main(){
	int base[12];
	int i,j,a;
	char num[4];
	for(i=0;i<12;i++){
		base[i] = i+1;
	}
	for(i=0;i<12;i++){
		for(j=0;j<12;j++){
			a = base[i]*(j+1);
			sprintf(num,"%i", a);
			//len = ;
			if (strlen(num) == 1){
				printf("   %i",a);
			}
			if (strlen(num) == 2){
				printf("  %i",a);
			}
			if (strlen(num) == 3){
				printf(" %i",a);
			}
		}
		printf("\n");
	}
	
	return 0;
}
