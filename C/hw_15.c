#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <stdbool.h>

void latin_letters(FILE *a) {
    char b[50];
    int count = 0;
    while(fgets(b,sizeof(b),a)) {
        for(int i=0; i < strlen(b); i++) {
            if(isalpha(b[i])) {
                count++;
            }
        }
    }
    printf("Latin letters in the file: %d\n",count);
}

void digits(FILE *a) {
    char b[50];
    int count = 0;
    while(fgets(b,sizeof(b),a)) {
        for(int i=0; i < strlen(b); i++) {
            if(isdigit(b[i])) {
                count++;
            }
        }
    }
    printf("Digits in the file: %d\n",count);
}

bool check_palindrome(char a[]) {
    char b[50];
    int index = 0;
    for(int i = strlen(a)-1; i >= 0; i--) {
        b[index++] = a[i];
    }
    b[index] = '\0';
    return strcmp(a,b) == 0 ? true : false;
}

int main() {
    system("clear");
    chdir("/home/ibrohim/Files");
    FILE *task1 = fopen("task_1.txt","r");
    // 1-task
    // latin_letters(task1);

    // 2-task
    // digits(task1);
    fclose(task1);

    // 3-task
    /*
    char name[50];
    printf("Enter a name for a file: "); scanf("%s",name);
    FILE *task3 = fopen(name,"w");
    char inc[50], dec[50], temp;
    strcpy(inc,name);
    strcpy(dec,name);
    for(int i=0; i < strlen(name)-1; i++) {
        for(int j=i; j < strlen(name); j++) {
            if(inc[i] > inc[j]) {
                temp = inc[i];
                inc[i] = inc[j];
                inc[j] = temp;
            }
            if(dec[i] < dec[j]) {
                temp = dec[i];
                dec[i] = dec[j];
                dec[j] = temp;
            }
        }
    }
    inc[strlen(inc)] = '\0';
    dec[strlen(dec)] = '\0';
    fclose(task3);
    FILE * i = fopen("new2.txt","w");
    for(int k=0; k < strlen(inc); k++) {
        fprintf(i,"%c ",inc[k]);
    }
    fclose(i);
    FILE * d = fopen("new1.txt","w");
    for(int l=0; l < strlen(dec); l++) {
        fprintf(d,"%c ",dec[l]);
    }
    fclose(d);
    */

    // 4-task
    /*
    char name2[50];
    printf("Enter a name for a file: "); fgets(name2,50,stdin);
    FILE *task4 = fopen(name2,"w");
    char inc2[50], dec2[50], temp2;
    strcpy(inc2,name2);
    strcpy(dec2,name2);
    for(int i=0; i < strlen(name2)-1; i++) {
        for(int j=i; j < strlen(name2); j++) {
            if(inc2[i] > inc2[j]) {
                temp2 = inc2[i];
                inc2[i] = inc2[j];
                inc2[j] = temp2;
            }
            if(dec2[i] < dec2[j]) {
                temp2 = dec2[i];
                dec2[i] = dec2[j];
                dec2[j] = temp2;
            }
        }
    }
    inc2[strlen(inc2)] = '\0';
    dec2[strlen(dec2)] = '\0';
    fclose(task4);
    FILE * right_order = fopen("new2.txt","w");
    for(int k=0; k < strlen(inc2); k++) {
        if(isspace(inc2[k]) == false)
            fprintf(right_order,"%c ",inc2[k]);
    }
    fclose(right_order);
    FILE * reverse_order = fopen("new1.txt","w");
    for(int l=0; l < strlen(dec2); l++) {
        if(isspace(dec2[l]) == false)
            fprintf(reverse_order,"%c ",dec2[l]);
    }
    fclose(reverse_order);
    */

    // 5-task
    /*
    FILE * task5 = fopen("task_5.txt","r");
    if(task5 == NULL) {
        puts("Couldn't open the file");
        return 0;
    }
    char line[100], nums[25][25], res[100] = "";
    int row = 0, col = 0, sum = 0;
    while(fscanf(task5,"%s",line) > 0) {
        for(int i=0; i < strlen(line); i++) {
            if(isdigit(line[i])) {
                nums[row][col++] = line[i];
            } else {
                row++;
                col = 0;
            }
        }
        row++;
        col = 0;
    }
    for(int i=0; i < row; i++) {
        sum += atoi(nums[i]);
        if(atoi(nums[i])) {
            strcat(res,nums[i]);
            if(i != row-1)
                strcat(res," + ");
        }
    }
    strcat(res," = ");
    printf("%s%d\n",res,sum);
    fclose(task5);
    */
    
    // 6-task
    /*
    FILE * task6 = fopen("task_6.txt","r");
    if(task6 == NULL) {
        puts("Couldn't open the file");
        return 0;
    }
    char line[50], res[50][50];
    int row = 0, col = 0;
    while(fgets(line,50,task6)) {
        for(int i=0; i < strlen(line); i++) {
            if(isupper(line[i])) {
                res[row][col++] = tolower(line[i]);
            } else if(islower(line[i])) {
                res[row][col++] = toupper(line[i]);
            } else {
                res[row][col++] = line[i];
            }
        }
        col = 0;
        row++;
    }
    fclose(task6);
    FILE * f = fopen("change_letters.txt","w");
    for(int i=0; i < row; i++) {
        fprintf(f,"%s",res[i]);
    }
    fclose(f);
    */
   
    // 7-task
    FILE * task7 = fopen("task_7.txt","r");
    if(task7 == NULL) {
        puts("Couldn't open the file");
        return 0;
    }
    char line[50], res[50][50];
    int index = 0;
    while(fgets(line,50,task7)) {
        char * token = strtok(line," \n\0");
        while(token != NULL) {
            if(check_palindrome(token)) {
                strcpy(res[index++],token);
            }
            token = strtok(NULL," \n\0");
        }
    }
    fclose(task7);
    FILE * f = fopen("palindromes.txt","w");
    for(int i=0; i < index; i++) {
        fprintf(f,"%s ",res[i]);
    }
    fclose(f);
    return 0;
}