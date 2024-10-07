#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <limits.h>

// 1-task
void sum_digit(char a[]) {
    int sum = 0;
    for(int i=0; a[i] != '\n' && a[i] != '\0'; i++) {
        if(isdigit(a[i]))
            sum += a[i] - '0';
    }
    printf("Sum of digits: %d\n",sum);
}

// 2-task
void fill_the_missings(char a[], char b[]) {
    int j=0;
    for(int i=0; a[i] != '\n' && a[i] != '\0'; i++) {
        if(a[i] == '#') {
            while(b[j] != '\0' && b[j] != '\n') {
                a[i] = b[j];
                j++;
                break;
            }
        }
    }
    printf("Result: ");
    for(int k=0; a[k] != '\n' && a[k] != '\0'; k++) {
        printf("%c",a[k]);
    }
    puts("");
}

// 3-task
void length_min(char a[]) {
    int min = INT_MAX, count = 0;
    for(int i=0; a[i] != '\0'; ++i) {
        if(a[i] == ' ') {
            if(count < min) {
                min = count;
            }
            count = 0;
        } else if(a[i] != '\n') {
            count++;
        }
    }
    if(count < min)
        min = count;
    printf("The min length: %d\n",min);
}

// 4-task
void letters(char a[]) {
    int count = 0;
    for(int i=0; a[i] != '\0'; i++) {
        if(isalpha(a[i]))
            ++count;
    }
    printf("The number of letters: %d\n",count);
}

// 5-task
void date(char a[]) {
    int day, month, year;
    for(int i=0; a[i] != '\0' && a[i] != '\n'; i++) {
        if(a[2] == 46 && a[5] == 46) {
            day = (a[0] - '0') * 10 + (a[1] - '0');
            month = (a[3] - '0') * 10 + (a[4] - '0');
            year = (a[6] - '0') * 1000 + (a[7] - '0') * 100 + (a[8] - '0') * 10 + (a[9] - '0');
        }
    }
    if(day > 0 && day < 32) {
        if(month > 0 && month < 13) {
            printf("True\n");
            return ;
        }
    }
    printf("False\n");
}

int main() {
    system("clear");
    char str[50];
    printf("Enter a string: ");
    fgets(str,sizeof(str),stdin);

    //sum_digit(str);
    
    // char key[50];
    // printf("Enter keys(without space): "); fgets(key,sizeof(key),stdin);
    // fill_the_missings(str,key);

    //length_min(str);

    // scanf("%s",str);
    // letters(str);

    date(str);

    return 0;
}
