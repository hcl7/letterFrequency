#include <stdio.h>
#include <string.h>

int letterFrequency(char* sentence, char letter);
void sentenceFrequency(char* sentence, char* alphabeth);
void usage(){ printf("usage: ./lfreq <message>\n"); }

void main(int argc, char *argv[]){
	if (argc > 1){
		char* alphabeth="abcdefghijklmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ0123456789!@#$^&*/";
		sentenceFrequency(argv[1], alphabeth);
	}
	else usage();
}

int letterFrequency(char* sentence, char letter){
	int count = 0;
	for(int i=0;i<strlen(sentence);i++){
		if (sentence[i]==letter){
			count+=1;
		}
	}
	return count;
}

void sentenceFrequency(char* sentence, char* alphabeth){
	int count = 0;
	for (int i=0;i<strlen(alphabeth);i++){
		count = letterFrequency(sentence,alphabeth[i]);
		if (count > 0){
			printf("%c %s %d\n", alphabeth[i], "=", count);
		}
	}
}