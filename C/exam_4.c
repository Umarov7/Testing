#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void increasing(int a) {
    char str[100] = "", temp[50];
    int sum = 0, j;
    for(int i = 1; i <= a; i++) {
        sum = 0;
        j = 0;
        while(j != i) {
            sum += i;
            j++;
            sprintf(temp, "%d", i);
            strcat(str,temp);
            if(j < i) {
                strcat(str,"+");
            }
        }
        strcat(str,"=");
        sprintf(temp, "%d", sum);
        strcat(str,temp);
        strcat(str,"\n");
    }
    FILE * f = fopen("numbers.txt","w");
    fprintf(f, "%s", str);
    fclose(f);
}
void decreasing(int a) {
    char str[100] = "", temp[50];
    int sum = 0, j;
    for(int i = a; i > 0; i--) {
        sum = 0;
        j = 0;
        while(j != i) {
            sum += i;
            j++;
            sprintf(temp, "%d", i);
            strcat(str,temp);
            if(j < i) {
                strcat(str,"+");
            }
        }
        strcat(str,"=");
        sprintf(temp, "%d", sum);
        strcat(str,temp);
        strcat(str,"\n");
    }
    FILE * f = fopen("numbers.txt","w");
    fprintf(f, "%s", str);
    fclose(f);
}


int main() {
    system("clear");
    int n;
    printf("Enter a number: "); scanf("%d",&n);
    if(n % 2) {
        increasing(n);
    } else {
        decreasing(n);
    }
}