#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

int sum(int a, int b) {
    static int res = 0;
    if(a > b) {
        return res;
    }
    res += a;
    return sum(a+1,b);
}

typedef struct mobile_phone {
    char model[20];
    int price;
    char date[11];
}Phone;

void show(struct mobile_phone p) {
    printf("Model: %s\n",p.model);
    printf("Price: %d$\n",p.price);
    printf("Date: %s\n",p.date);
}




void max_min_dynamic(int *a, int b) {
    int max = INT_MIN, min = INT_MAX;
    puts("Enter the elements: ");
    for(int i=0; i<b; i++) {
        scanf("%d",&*(a+i));
    }
    for(int i=0; i < b; ++i) {
        if(*(a+i) > max)
            max = *(a+i);
        if(*(a+i) < min)
            min = *(a+i);    
    }
    printf("Max = %d\nMin = %d\n",max,min);
}

void max_removal(int *a, int b) {
    int max = INT_MIN, index = -1;
    printf("Enter the elements: ");
    for(int i=0; i<b; i++) {
        scanf("%d",&*(a+i));
    }
    for(int i=0; i < b; ++i) {
        if(*(a+i) > max) {
            max = *(a+i);
            index = i;
        }  
    }
    printf("Max = %d\n",a[index]);
    for(int i = index; i < b; i++)
        a[i] = a[i+1];
    a[b-1] = '\0';
    for(int i=0; i<b; i++) {
        printf("%4d",a[i]);
    }
    puts("");
}

void n_removal(int *a, int b, int c) {
    int swap;
    printf("Enter the elements: ");
    for(int i=0; i<b; i++) {
        scanf("%d",&*(a+i));
    }
    for(int i=0; i < b-1; i++) {
        for(int j=i; j < b; ++j) {
            if(*(a+i) < *(a+j)) {
                swap = *(a+i);
                *(a+i) = *(a+j);
                *(a+j) = swap;
            }
        }
    }
    for(int i=0; i<b; i++) {
        printf("%d  ",a[i]);
    }
    for(int j=0; j<b; j++) {
        if(j >= c) {
            a[j] = '\0';
        }
    }
    puts("");
    for(int i=0; i < b-1; i++) {
        for(int j=i; j < b; ++j) {
            if(*(a+i) > *(a+j)) {
                swap = *(a+i);
                *(a+i) = *(a+j);
                *(a+j) = swap;
            }
        }
    }
    puts("Result:");
    for(int i=0; i<b; i++) {
        printf("%d  ",a[i]);
    }
    puts("");
}

bool compare_strings(char a[], char b[]) {
    char temp;
    if(strlen(a) == strlen(b)) {
        for(int i=0; i<strlen(a) - 1; i++) {
            for(int j=i; j<strlen(b); j++) {
                if(a[i] < a[j]) {
                    temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }
            }
        }
        for(int i=0; i<strlen(a) - 1; i++) {
            for(int j=i; j<strlen(b); j++) {
                if(b[i] < b[j]) {
                    temp = b[i];
                    b[i] = b[j];
                    b[j] = temp;
                }
            }
        }
    } else {
        return false;
    }
    if(strcmp(a,b) == 0)
        return true;
    else
        return false;    
}




void even_file(char evens[50], int a) {
    FILE * f = fopen(evens,"w");
    fprintf(f,"Even numbers: ",evens);
    for(int i=2; i<a; i+=2) {
        fprintf(f,"%d | ",i);
    }
    if(f == NULL) {
        puts("Error");
        return ;
    }
    puts("The information has been successfully written");
    fclose(f);
}

void pyramid_file(char a[], int b) {
    FILE * f = fopen(a,"w");
    for(int i=1; i<=b; i++) {
        for(int j=1; j<=i; j++) {
            fprintf(f,"%c ",64+j);
        }
        for(int k=i; k < b; k++) {
            fprintf(f,"* ");
        }
        fprintf(f,"\n");
    }
    puts("The information has been successfully written");
    fclose(f);    
}

/*void count_average_min(FILE *a) {
    int count = 0, index = 0;
    float average_length = 0;
    char min[50] = "", words[50];
    while(fscanf(a,"%s",words) > 0) {
        count++;
        average_length += strlen(words);
        if(strlen(words) < strlen(min)) {
            strcpy(min,words);
        }
    }
    printf("The number of words: %d\nThe average length: %.2f\nThe min length word: %s\n",count,average_length/count,min);
}*/

void sum_file(FILE *a) {
    char nums[50];
    int sum = 0;
    while(fgets(nums,50,a))
        sum += atoi(nums);
    printf("Sum = %d\n",sum);
}


/*void new_file(char *a) {
    char word[50], words[25][25], temp[50];
    int index = 0;
    while(fscanf(a,"%s",word) > 0) {
        strcpy(words[index++],word);
    }
    for(int i=0; i<index-1; i++) {
        for(int j=i; j<index; j++) {
            if(strlen(words[i]) > strlen(words[j])) {
                strcpy(temp,words[i]);
                strcpy(words[i],words[j]);
                strcpy(words[j],temp);
            }
        }
    }
    fputs(words);
}*/

void space(FILE *a, int b) {
    int index = 0;
    char words[50];
    while(fgets(words,sizeof(words),a)) {
        index++;
        if(index == b) {
            fprintf(a,"\n");
        }
    }
}

bool check_mac(char a[]) {
    char b[50];
    strcpy(b,a);
    char * token = strtok(b,"-");
    while(token != NULL) {
        if(isalpha(token[0]) && isalpha(token[1]) || isdigit(token[0]) && isdigit(token[1]))
            return false;
        token = strtok(NULL,"-");
    }
    return true;
}


bool friendly_number(int a) {
    int sum = 0;
    for(int i = 1; i <= a/2; i++) {
        if(a % i == 0) {
            sum += i;
        }
    }
    int b = sum;
    sum = 0;
    for(int j = 1; j <= b/2; j++) {
        if(b % j == 0) {
            sum += j;
        }
    }
    return a == sum;
}

int main() {
    system("clear");
    srand(time(0));
    // int n1, n2;
    // printf("Enter 2 numbers: "); scanf("%d%d",&n1,&n2);
    // printf("Sum = %d\n",sum(n1,n2));
    // Phone phone;
    // int p;
    // char m[20], d[11];
    // printf("Enter a model: "); scanf("%s",m);
    // printf("Enter a price: "); scanf("%d",&p);
    // printf("Enter a date: "); scanf("%s",d);
    // phone.price = p;
    // strcpy(phone.model,m);
    // strcpy(phone.date,d);
    // show(phone);

    // int n, *arr;
    // printf("Enter a number: "); scanf("%d",&n);
    // arr = (int *) malloc (n * sizeof(int));
    // max_min_dynamic(arr,n);
    
    // arr = (int *) calloc(n,sizeof(int));
    // max_removal(arr,n);
    // int num;
    // printf("Enter a number: "); scanf("%d",&num);
    // n_removal(arr,n,num);
    // free(arr);
    // char str1[50], str2[50];
    // printf("Enter 2 strings: "); scanf("%s",str1), scanf("%s",str2);
    // printf("Result: %s\n",compare_strings(str1,str2) == true ? "True" : "False");
    
    chdir("/home/ibrohim/Files");
    // int n;
    // printf("Enter a number: "); scanf("%d",&n);
    /*even_file(file,n);
    pyramid_file(file,n);
    count_average_min(words);

    FILE * f = fopen("numbers","r");
    sum_file(f);
    fclose(f);

    FILE * f = fopen("words","r");
    count_average_min(f);
    fclose(f);*/

    /*FILE * f = fopen("random_words","r");*/

    /*int n;
    printf("Enter a number: "); scanf("%d",&n);
    FILE * f = fopen("random_words","a+");
    space(f,n);
    fclose(f);
    system("start random_words");*/

    /*FILE * f = fopen("random","w+");
    for(int i=0; i<n; i++) {
        fprintf(f,"%d\n",rand() % 100);
    }
    fclose(f);*/

    // FILE * mac = fopen("Mac_adress","r");
    // char arr[50];
    // int count = 0;
    // while(fscanf(mac,"%s",arr) > 0) {
    //     if(check_mac(arr) == true) {
    //         printf("%d. %s\n",++count,mac);
    //     }
    // }
    // fclose(mac);




    /*FILE * bf = fopen("input_numbers.bin","wb+");
    if(bf == NULL) {
        puts("Error occured");
        return 0;
    }
    int n, num;
    printf("Enter a number of numbers: "); scanf("%d",&n);
    for(int i=0; i<n; i++) {
        printf(">>> ");
        scanf("%d",&num);
        fwrite(&num,sizeof(4),1,bf);
    }
    rewind(bf);
    printf("\nThe info in the file: ");
    while(fread(&num,sizeof(int),1,bf)) {
        printf("%d | ",num);
    }
    puts("");
    fclose(bf);*/
    
    int n;
    printf("Enter a number: "); scanf("%d",&n);
    printf("Result: %s\n",friendly_number(n) ? "True" : "False");
    return 0;
}