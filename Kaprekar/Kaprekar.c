/* 
	A.Woodward 

	October 2016
	
	Kaprekar's Routine
	Challenge 287 Easy
*/

#include <stdio.h>
#include <ctype.h>



int largest_digit(char input[]){
	
	int i;
	int largest = 0;
	
	for(i=0;i<4;i++){
		if(largest < input[i] - '0'){
			largest = input[i] - '0';
		}
	}
	return largest;
}




int desc_digits(char input[]){
	
	int i;
	int j;
	for(i=0;i<4;i++){
		if(input[i] == 0){
			for(j=3;j>0;j--){
				input[j] = input[j-1];
			}
			input[0] = '0';
		}
	}
	
	for(i=1;i<4;i++){
		for(j=0;j<4-i;j++){
			if((int)input[j] < (int)input[j+1]){
				char temp = input[j];
				input[j] = input[j+1];
				input[j+1] = temp;
			}
		}
	}
	
	int return_num = (input[0]-'0')*1000 + (input[1]-'0')*100 + (input[2]-'0')*10 + (input[3]-'0');
	
	
	return return_num;
}




int main(){

	char c[4];
	
	printf("Enter a character: ");
	
	scanf("%s", c);

	int i;
	for(i=0;i<4;i++){
		printf("%d ",c[i]);
	}
	printf("\n");
	
	
	
	printf("c: %s\n",c);
	
	int largest = largest_digit(c);
	
	printf("largest digit of %s: %d\n",c,largest);
	
	int descending = desc_digits(c);
	
	printf("descending digits of %s: %d\n",c,descending);
	
	


	return 0;
}