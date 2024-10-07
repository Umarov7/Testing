#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int random_num(int a, int b) {
    return a + rand() % (b - a + 1);
}
bool prime(int x) {
    for(int i=2; i*i <= x; i++) {
        if(x % i == 0)
            return false;
    }
    return true;
}

// int main()
// {
//     system("clear");
//     char l; int n;
//     printf("Enter a letter and a number: ");
//     scanf("%c%d", &l, &n);
//     if (l == 'a' || l == 'c' || l == 'e' || l == 'g') {
//         if (n % 2 != 0) {
//             printf("black\n");
//         } else
//         {
//             printf("white\n");
//         }
        
//     } else if (l == 'b' || l == 'd' || l == 'f' || l == 'h') {
//         if (n % 2 != 0) {
//             printf("white\n");
//         } else {
//             printf("black\n");
//         }
        
//     } else {
//         printf("Try again\n");
//     }
//     return 0;
// }


void replace_prime(int a[][10], int b, int c) {
    for(int i=0; i<b; i++) {
        for(int j=0; j<c; ++j) {
            if(prime(a[i][j]) == true)
                printf("%4c",42);
            else    
                printf("%4d",a[i][j]);    
        }
        printf("\n");
    }
}

int main() {
    system("clear");
    srand(time(NULL));
    int row, col, mx[10][10];
    printf("Enter 2 numbers: "); scanf("%d%d",&row,&col);
    for(int i=0; i<row; ++i) {
        for(int j=0; j<col; j++) {
            mx[i][j] = random_num(1,50);
            printf("%4d",mx[i][j]);
        }
        printf("\n");
    }
    printf("Result:\n");
    replace_prime(mx,row,col);
}