#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
// 1-task
char increasing(int a) {
    char res[50][50], temp[10];
    int j, sum, index = 0;
    for(int i=1; i <= a; i++) {
        j = 0;
        sum = 0;
        while(j != i) {
            sum += i;
            j++;
            sprintf(temp, "%d", i);
            strcpy(res[index++],temp);
            if(j < i) {
                strcpy(res[index++],"+");
            }
        }
        strcpy(res[index++],"=");
        sprintf(temp, "%d", sum);
        strcpy(res[index++],temp);
        strcpy(res[index++],"\n");
    }
    strcpy(res[index],"\0");
}
char decreasing(int a) {
    char res[50][50], temp[10];
    int j, sum, index = 0;
    for(int i = a; i > 0; i--) {
        j = i;
        sum = 0;
        while(j > 0) {
            sum += i;
            j--;
            sprintf(temp, "%d", i);
            strcpy(res[index++],temp);
            if(j > 0) {
                strcpy(res[index++],"+");
            }
        }
        strcpy(res[index++],"=");
        sprintf(temp, "%d", sum);
        strcpy(res[index++],temp);
        strcpy(res[index++],"\n");
    }
    strcpy(res[index],"\0");
}

// 2-task
bool isPrime(int a) {
    if(a == 1)
        return false;
    for(int i = 2; i*i <= a; i++) {
        if(a % i == 0)
            return false;
    }
    return true;
}
void prime_numbers(FILE * a, int b) {
    for(int i=1; i < b; i++) {
        if(isPrime(i))
            fprintf(a, "%d  ", i);
    }
}

int main() {
    chdir("/home/ibrohim/Files");

    // int n;
    // printf("Enter a number: "); scanf("%d",&n);

    // FILE * f = fopen("task1.txt","w");
    // if(n % 2) {
    //     fprintf(f,"%s",increasing(n));
    // } else {
    //     fprintf(f,"%s",decreasing(n));
    // }

    // FILE * f = fopen("task2.txt","w");
    // prime_numbers(f,n);

    // 3-task
    /*
    FILE * f = fopen("task3.txt","r");
    char str[100];
    int sum = 0;
    while(fscanf(f,"%s",str) > 0) {
        sum += atoi(str);
    }
    printf("Sum of numbers in the file = %d\n",sum);
    */

    // 4-task
    /*
    FILE * f = fopen("task4.txt","r");
    char str[100];
    while(fscanf(f, "%s", str) > 0) {
        if(isupper(str[0])) {
            printf("%s\n",str);
        }
    }
    */
   
    // 5-task
    /*
    FILE * f = fopen("task5.txt","r");
    char str[50];
    int count = 0;
    while(fscanf(f, "%s", str) > 0) {
        count = 0;
        for(int i=0; i<strlen(str); i++) {
            if(isalpha(str[i])) {
                count++;
            }
        }
        if(count == 3) {
            printf("%s\n",str);
        }
    }
    */

    // 6-task
    /*
    FILE * f = fopen("task6.txt","r");
    char str[50];
    int count = 0;
    while(fscanf(f, "%s", str) > 0) {
        count = 0;
        for(int i=0; i<strlen(str); i++) {
            if(isalpha(str[i])) {
                count++;
            }
        }
        if(count > 3) {
            printf("%s\n",str);
        }
    }
    */

    // 7-task
    /*
    FILE * f = fopen("task7.txt","r");
    char str[50];
    int count = 0;
    while(fscanf(f, "%s", str) > 0) {
        count = 0;
        for(int i=0; i<strlen(str); i++) {
            if(isalpha(str[i])) {
                count++;
            }
        }
        if(count < 6) {
            printf("%s\n",str);
        }
    }
    */

    // 8-task
    FILE * f = fopen("task8.txt","r");
    char str[50];
    bool n;
    while(fscanf(f, "%s", str) > 0) {
        n = false;
        for(int i=0; i<strlen(str); i++) {
            if(isdigit(str[i])) {
                n = true;
            }
        }
        if(n == true) {
            printf("%s\n",str);
        }
    }
    fclose(f);
    return 0;
}