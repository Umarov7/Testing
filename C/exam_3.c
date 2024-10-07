#include <stdio.h>
//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
int main() {
    int mx[5][5], row = 5, col = 5;
    printf("Enter 25 numbers: ");
    for(int i=0; i < row; i++) {
        for(int j=0; j < col; j++) {
            scanf("%d",&mx[i][j]);
        }
    }
    for(int i=0; i < row; i++) {
        for(int j=0; j < col; j++) {
            if(i == 0 || j == 0 || i == row-1 || j == col-1) {
                printf("%4d",0);
            } else {
                printf("%4d",mx[i][j]);
            }
        }
        printf("\n");
    }
}