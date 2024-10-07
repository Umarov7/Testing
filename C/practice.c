#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

// int main() {
//     system("clear");
//     srand(time(NULL));
    // int arr[3][3], row = 3, col = 3, min;
    // for(int i=0; i<row; i++) {
    //     for(int j=0; j<col; j++) {
    //         arr[i][j] = rand() % 91;
    //         printf("%3d",arr[i][j]);
    //     }
    //     puts("");
    // }
    // for(int i=0; i<row; i++) {
    //     min = arr[i][0];
    //     for(int j=0; j<col; j++) {
    //         if(arr[i][j] < min)
    //             min = arr[i][j];
    //     }
    //     puts("");
    //     printf("Min(%d-row) = %d",i+1,min);
    // }
    // puts(""); 

    // int arr[10][10] = {{1,2,3}, {4,5,6}, {7,8,9};
    // for(int i=0; i<3; i++) {
    //     for(int j=0; j<3; j++) {
    //         printf("%d ",arr[j][i]);
    //     }
    //     puts("");
    // }
    // return 0;

//     int arr[10][10] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
//     for(int i=0; i<3; i++) {
//         for(int j=0; j<4; j++) {
//             printf("%d ",arr[i][j]);
//         }
//         puts("");
//     }
//     puts("");
//     for(int i=0; i<3; i++) {
//         for(int j=0; j<4; ++j) {
//             if(i % 2 != 0)
//                 printf("%d ",arr[i][j]);
//         }
//     }
//     puts("");

//     return 0;
// }

int length(char a[]) {
    int count = 0;
    for(int i=0; a[i] != '\0' && a[i] != '\n'; i++) {
        count++;
    }
    return count;
}


int factorial(int a) {
    if(a == 1) {
        return 1;
    } else {
        return a * factorial(a-1);
    }
}

void decrease(int a) {
    if(a < 0) {
        return ;
    }
    printf("%d | ",a);
    decrease(a-1);
}

int sum_digits(int a) {
    static int sum = 0;
    if(a > 0) {
        sum += a % 10;
        a /= 10;
    } else {
        return sum;
    }
    return sum_digits(a);
}

void increase(int a) {
    static int i = 0;
    if(i <= a) {
        printf("%d | ",i);
        i++;
    } else {
        return ;
    }
    increase(a);
}

void reverse(char *a) {
    if(*a != '\0') {
        reverse(a+1);
        printf("%c",*a);
    } else {
        return ;
    }
}

bool palindrome(char *a, int b, int c) {
    if(b >= c) {
        return true;
    } else {
        if(a[b] != a[c])
            return false;
        else
            palindrome(a, b+1, c-1);    
    }
}

int main() {
    system("clear");
    char str[50];
    printf("Enter a string: "); fgets(str, sizeof(str), stdin);
    // printf("The length: %d\n",length(str));

    // int n;
    // printf("Enter a number: "); scanf("%d",&n);

    //printf("Result: %d\n",factorial(n));
    //decrease(n);
    //printf("Result: %d\n",sum_digits(n));
    //increase(n);

    //reverse(str);
    int start = 0, end = length(str) - 1;
    printf("Palindrome check: %s\n",palindrome(str,start,end) == true ? "True" : "False");
    return 0;
}