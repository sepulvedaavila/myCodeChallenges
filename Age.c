/*
 *********************************************************************************************************************
 * If they're from 0 to 2 the child should be with parents print : 'Still in Mama's arms'                            *
 *If they're 3 or 4 and should be in preschool print : 'Preschool Maniac'					     *
 *If they're from 5 to 11 and should be in elementary school print : 'Elementary school'			     *
 *From 12 to 14: 'Middle school'										     *
 *From 15 to 18: 'High school'											     *
 *From 19 to 22: 'College'											     *
 *From 23 to 65: 'Working for the man'										     *
 *From 66 to 100: 'The Golden Years'										     *
 *If the age of the person less than 0 or more than 100 - it might be an alien - print: "This program is for humans" *
 *********************************************************************************************************************
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]){
		char line[12] ;
		strcpy(line,"");
		int age;
		age = atoi(line);
		
            if (age <=	 0 || age >= 100){
	        	printf("This program is for humans\n");
	        } if (age > 0 && age < 3){
	    	    printf("Still in Mama's arms\n");
	        } if (age == 3 || age == 4){
        		printf("Preschool Maniac\n");
	        } if (age > 4 && age < 12){
        		printf("Elementary school\n");
	        } if (age > 11 && age < 15){
	        	printf("Middle school\n");
	        } if (age > 14 && age < 19){
	        	printf("High school\n");
	        } if (age > 18 && age <23){
	        	printf("College\n");
        	} if (age >22 && age < 66){
        		printf("Working for the man\n");
	        } if (age > 65 && age < 100){
	        	printf("The Golden Years\n");
	        }
        
	return 0;
}
