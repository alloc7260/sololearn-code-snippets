/*
You are a secret agent, and you receive an encrypted message that needs to be decoded. The code that is being used flips the message backwards and inserts non-alphabetic characters in the message to make it hard to decipher.

Task: 
Create a program that will take the encoded message, flip it around, remove any characters that are not a letter or a space, and output the hidden message.

Input Format:  
A string of characters that represent the encoded message.

Output Format: 
A string of character that represent the intended secret message.

Sample Input: 
d89%l++5r19o7W *o=l645le9H

Sample Output: 
Hello World

Explanation: 
If you remove everything that isn't a letter or space from the original message and flip it around, you get 'Hello World'.
*/

#include <stdio.h>
#include <string.h>
int main(){
	int a,b,c,i,j,k;
	char alp[]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ";
	char str[200];
	char opt[200]="";
	char arr[2];	
	gets(str);	
	a=strlen(alp);
	b=strlen(str);	
	for(i=0;i<b;i++){
		for(j=0;j<a;j++){
			if(str[i]==alp[j]){
				arr[0]=str[i];
				arr[1]='\0';
			    strcat(opt,arr);
			}	
		}
	}
	c=strlen(opt);
	for(k=c-1;k>=0;k--){
		printf("%c",opt[k]);
	}
	return 0;
}