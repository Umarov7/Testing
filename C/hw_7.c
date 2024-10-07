#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

// 1-task
void spiral(int a[][10], int b) {
    int el = 1, count = 0, left = 0, right = b-1, up = 0, down = b-1;
    while(up <= down) {
        for(int j=left; j<right; j++) {
            a[up][j] = el++;
        }
        for(int i=up; i<down; ++i) {
            a[i][right] = el++;
        }
        for(int j=right; j>left; --j) {
            a[down][j] = el++;
        }
        for(int i=down; i>up; i--) {
            a[i][left] = el++;
        }
        left++;
        right--;
        up++;
        down--;
    }
    if(b % 2) {
        a[b/2][b/2] = el;
    }
    for(int i=0; i<b; i++) {
        for(int j=0; j<b; ++j) {
            printf("%4d",a[i][j]);
        }
        printf("\n");
    }    
}

// 2-task
void show_matrix(int a[][10], int b, int c) {
    for(int i=0; i<b; i++) {
        for(int j=0; j<c; ++j) {
            printf("%d  ",a[i][j]);
        }
        puts("");
    }
}

void square(int a[][10], int b, int c) {
    int row_index = -1;
    for(int i=0; i<b; i++) {
        for(int j=0; j<c; ++j) {
            if(a[i][j] % 3 == 0 && a[i][j] % 5 == 0) {
                row_index = i;
                break;
            }
        }
    }
    if(row_index >= 0) {
        for(int j=0; j<c; ++j) 
            a[row_index][j] *= a[row_index][j];
    }
}

// 3-task
void local_max(int a[][10], int b, int c) {
    printf("Result: ");
    for(int i=0; i<b; i++) {
        for(int j=0; j<c; ++j) {
            if(i > 0 && i < b-1 && j > 0 && j < c-1) {
                if(a[i][j] > a[i][j-1] && a[i][j] > a[i][j+1] && a[i][j] > a[i-1][j] && a[i][j] > a[i+1][j]) {
                    printf("%d | ",a[i][j]);
                }
            }
        }
    }
}

// 4-task
void min_maxCol(int a[][10], int b, int c) {
    int max_col = -1, multip = 1, min = a[0][0];
    for(int i=0; i<b; i++) {
        int j = 0;
        while(j < c) {
            multip *= a[i][j];
            if(multip > max_col)
                max_col = j;
            j++;
        }
    }
    for(int i=0; i<b; ++i) {
        if(min > a[i][max_col])
            min = a[i][max_col];
    }
    printf("Max product column: %d\n",max_col);
    printf("Min: %d\n",min);
}

// 5-task
void max_minCol(int a[][10], int b, int c) {
    int min_col = INT_MAX, index = 0, sum, max = INT_MIN;
    for(int j=0; j<c; ++j) {
        sum = 0;
        for(int i=0; i<b; i++) {
            sum += a[i][j];
        }
        if(sum < min_col) {
            min_col = sum;
            index = j;
        }
    }
    for(int i=0; i<b; ++i) {
        if(max < a[i][index])
            max = a[i][index];
    }
    printf("\nMin sum %d-column: %d\n",index,min_col);
    printf("Max: %d\n",max);
}

// 6-task
void equal_positive_negative(int a[][10], int b, int c) {
    int count_pos, count_neg;
    for(int i=0; i<b; i++) {
        count_pos = 0, count_neg = 0;
        for(int j=0; j<c; ++j) {
            a[i][j] < 0 ? count_neg++ : count_pos++;
        }
        if(count_pos == count_neg) {
            printf("Row with equal positive and negative elements: %d\n",i);
            return ;
        } else {
            continue;
        }
    }
    printf("Not found\n");
}

// 7-task
void equal_odd_even(int a[][10], int b, int c) {
    int equal_col = -1 ,count_odd, count_even;
    for(int j=0; j<c; j++) {
        count_odd = 0, count_even = 0;
        for(int i=0; i<b; ++i) {
            a[i][j] % 2 ? count_odd++ : count_even++;
        }
        if(count_odd == count_even)
            equal_col = j;
    }
    if(equal_col >= 0) {
        printf("Result: ");
        for(int i=0; i<b; ++i) {
            printf("%d ",a[i][equal_col]);
        }
    } else {
        printf("Not found\n");
    }
}

int main() {
    system("clear");
    srand(time(NULL));
    int row, col, mx[10][10];
    // printf("Enter 2 numbers: "); scanf("%d%d",&row,&col);
    // for(int i=0; i<row; i++) {
    //     for(int j=0; j<col; ++j) {
    //         mx[i][j] = rand() % 99;
    //     }
    // }
    // show_matrix(mx,row,col);

    int n;
    printf("n = "); scanf("%d",&n);
    spiral(mx,n);

    // square(mx,row,col);
    // puts("Result:");
    // show_matrix(mx,row,col);

    // local_max(mx,row,col);

    //min_maxCol(mx,row,col);

    //max_minCol(mx,row,col);

    // for(int i=0; i<row; i++) {
    //     for(int j=0; j<col; ++j) {
    //         mx[i][j] = rand() % (30 - -30 + 1) + -30;
    //     }
    // }
    // show_matrix(mx,row,col);
    // equal_positive_negative(mx,row,col);

    //equal_odd_even(mx,row,col);
    return 0;
}