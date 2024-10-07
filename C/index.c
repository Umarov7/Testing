#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int max(int a, int b) {
    int c = a > b ? a : b;
    return c;
}
double divide(int a, int b) {
    return (double)a / b;
}
int num(char n){
    return n-48;
}
char atoA(char ch){
    if(ch >= 'A' && ch <= 'Z'){
        return ch;
    }
    return ch-32;
}
void pyramid(char letters){
    for(int i=1; i<=4; ++i) {
        for(int j=1; j<=i; j++) {
            printf("%c", letters);
        }
        letters++;
        printf("\n");
    }
}


int average(int a,int b,int c){
    int sum = a+b+c;
    return sum / 3;
}
void average2(int a, int b, int c){
    printf("%g\n", (float)(a+b+c)/3);
}
int ekub(int a, int b){
    int ekub;
    for(int i=1; i<=a; ++i){
        if(a % i == 0 && b % i == 0) {
            ekub = i;
        }
    }
    return ekub;
}
void sumOddEven(int a){
    int sumOdd = 0, sumEven = 0, i = 1;
    while(i < a) {
        if(i % 2) {
            sumOdd += i;
        } else {
            sumEven += i;
        }
        ++i;
    }
    printf("The sum of odds is %d\n", sumOdd);
    printf("The sum of evens is %i\n", sumEven);
}
void pos_neg(int a){
    if(a >= 0) {
        printf("Positive\n");
    } else {
        printf("Negative\n");
    }
}
void sum_square(){
    int sum = 0;
    do
    {
        int num;
        printf("Enter a number: "); scanf("%d", &num);
        if(num <= 0)
            break;
        sum += num * num;
    } while(1);
    printf("Result = %i\n", sum);
}
int ekuk(int a, int b){
    int ekub, i = 1;
    do {
        if(a % i == 0 && b % i == 0) {
            ekub = i;
        }
        ++i;
    } while(i <= b);
    return a * b / ekub;
}
int min(int a, int b){
    return (a < b) ? a : b;
}
int second_max(){
    int num, max = 0, max2 = 0;
    while(1) {
        printf("Enter a number: "); scanf("%d", &num);
        if(num <= 0) {
            break;
        }
        if(num > max) {
            max2 = max;
            max = num;
        } else if(num > max2 && num != max2) {
            max2 = num;
        }
    }
    return max2;
}
void second_min(){
    int num, min = INT_MAX, min2 = INT_MAX;
    for(;;) {
        printf("Enter a number: "); scanf("%d", &num);
        if(num <= 0) {
            break;
        }
        if(num < min) {
            min2 = min;
            min = num;
        } else if(num < min2 && num != min2) {
            min2 = num;
        }
    }
    printf("The 2nd min = %d\n", min2);
}

// int main() {
    // system("clear");
    // int x, y;
    // printf("Enter 2 number: ");
    // scanf("%d%d", &x, &y);
    //printf("Result is %g\n", divide(x, y));
    // char c;
    //printf("Enter a letter: "); scanf("%c", &n);
    // for(int i=1; i<=10; ++i) {
    //     scanf("%c", &c);
    //     printf("%c", atoA(c));
    // }
    // pyramid('a');


    // int n1,n2,n3;
    // printf("Enter 3 numbers: "); scanf("%d%d%d", &n1,&n2,&n3);
    // printf("%d\n", average(n1,n2,n3));
    // int n1, n2;
    // printf("Enter 2 numbers: "); scanf("%i%i", &n1, &n2);
    // printf("EKUB: %d\n", ekub(n1, n2));
    // int n;
    // printf("Enter a number: "); scanf("%i", &n);
    // sumOddEven(n);
    // pos_neg(n);
    // sum_square();
    // printf("EKUK = %i\n", ekuk(n1, n2));
    // printf("Min = %d\n", min(n1, n2));
    // printf("The 2nd max = %i\n", second_max());
//     second_min();
//     return 0;
// }


// void show_array(int a[], int count);
// int count_even;
// int main() {
//     system("clear");
//     // int arr[] = {1,2,3,4,5,6,7,8,9,10};
//     // for(int i = 0; i < sizeof(arr)/sizeof(int); i++) {
//     //     printf("%d = %d\n", arr[i], arr[i] * arr[i]);
//     // }
//     int arr[15], count;
//     printf("Enter a number of the elements: "); scanf("%d", &count);
//     for(int i = 0; i < count; ++i) {
//         scanf("%d", &arr[i]);
//         if(arr[i] % 2 == 0)
//             count_even++; 
//     }
//     show_array(arr, count);
// }
// void show_array(int a[], int count) {
//     printf("Elements: ");
//     for(int i=0; i<count; ++i) 
//         printf("%i, ", a[i]);
//         printf("Evens = %i\n", count_even);
// }
void show_array(float a[], int c) {
    for(int i = 0; i < c; i++)
        printf("%g : ", a[i]);
    printf("\n");    
}
// int main() {
//     system("clear");
//     int n, odd = 1, arr[15];
//     printf("Enter a number of elements: "); scanf("%d", &n);
//     for(int i = 0; i < n; i++) {
//         arr[i] = odd;
//         odd += 2;
//     }
//     show_array(arr, n);    
//     return 0;
// }
int random_num(int x, int y) {
    return rand() % (y - x + 1) + x;
}
float random_f(int a, int b) {
    return random_num(a,b) * 0.23 + b * 1.0 / a;
}
// int main() {
//     system("clear");
//     float arr[15]; int n;
//     printf("Enter a number of elements: "); scanf("%d", &n);
//     for(int i=0; i<n; ++i) {
//         arr[i] = random_f(10,49);
//     }
//     show_array(arr,n);
//     return 0;
// }
// int main() {
//     system("clear");
//     srand(time(NULL));
//     int n, arr[20];
//     printf("Enter a number of elements: "); scanf("%d",&n);
//     for(int i=0; i<n; i++) {
//         arr[i] = random_num(-50,50);
//         printf("%d ", arr[i]);
//     }
//     int j=0, count=0;
//     do {
//         if(arr[j] > 0)
//             count++;
//         j += 2;
//     } while(j < n);
//     printf("\nResult = %d\n", count);
//     return 0;
// }

// void elements_odd_even(int a[], int b, bool c) {
//     if(c == 0) {
//         for(int i = c; i < b; i += 2) 
//             printf("%d : ", a[i]);
//     } else {
//         for(int j = b-1; j >= 0; j -= 2) 
//             printf("%d | ", a[j]);
//     }
// }
// int main() {
//     system("clear");
//     srand(time(NULL));
//     int n, arr[20];
//     printf("Enter a number of elements: "); scanf("%d",&n);
//     for(int i=0; i<n; i++) {
//         arr[i] = random_num(10,30);
//         printf("%d ", arr[i]);
//     }
//     printf("\nResult:\n");
//     elements_odd_even(arr,n,false);
//     printf("\n");
//     elements_odd_even(arr,n,true);
//     printf("\n");
//     return 0;
// }
int second_max_element(int a[], int b) {
    int max1 = 0, max2 = 0;
    for(int i = 0; i < b; i++) {
        if(max1 < a[i]) {
            max1 = a[i];
        }
        if(max2 < a[i] && a[i] != max1) {
            max2 = a[i];
        }
    }
    return max2;
}
// int main() {
//     system("clear");
//     srand(time(0));
//     int n, arr[20];
//     printf("Enter a number of elements: "); scanf("%d",&n);
//     for(int i=0; i<n; ++i) {
//         arr[i] = random_num(10,99);
//         printf("%d ", arr[i]);
//     }
//     //printf("\nThe 2nd max = %i\n", second_max_element(arr,n));
//     int index = -1, el;
//     for(int i = 1; i < n-1; i++) {
//         if(arr[i] > arr[0] && arr[i] < arr[n-1] && arr[i] % 2 == 0) {
//             index = i;
//             el = arr[i];
//             break;
//         }
//     }
//     if(index >= 0) 
//         printf("\nThe first even number = %d\nIndex = %d\n", el, index);
//     else 
//         printf("\nIt's not found\n");    
//     return 0;
// }


// int main() {
//     system("clear");
    // int arr[] = {70,63,27,53,25,47,28,16,61,99,57,87,16,25,34};
    // int l_min, count = 0;
    // for(int i = 1; i < sizeof(arr)/sizeof(int); ++i) {
    //     if(arr[i] < arr[i-1] && arr[i] < arr[i+1]) {
    //         printf("%d\n", arr[i]);
    //         count++;
    //     }
    // }
    // printf("The number of local_mins is %i\n", count);
//     int arr[20], n;
//     printf("Enter a number of elements: "); scanf("%d",&n);
//     printf("Enter the elements\n");
//     for(int i = 0; i < n; ++i) 
//         scanf("%i",&arr[i]);
//     int intruder; bool order = false;
//     if(arr[0] < 0) {
//         for(int i=1; i<n; i++) {
//             if(arr[i] >= 0 && i % 2) {
//                 continue;
//             } else {
//                 order = true;
//                 intruder = arr[i];
//                 break;
//             }
//         }
//     } else {
//         for(int i=1; i<n; i++) {
//             if(arr[i] < 0 && i % 2) {
//                 continue;
//             } else {
//                 order = true;
//                 intruder = arr[i];
//                 break;
//             }
//         }
//     }
//     if(order == true)
//         printf("Intruder = %d\n", intruder);
//     else
//         printf("True\n");        
//     return 0;
// }


// void array_exercises(int a[], int b) {
    // for(int i=0; i<b; i++) {
    //     a[i] = random_num(1,100);
    //     printf("%d ", a[i]);
    // } printf("\n");
    // for(int i=3; i<8; ++i) {
    //     printf("%i ", a[i]);
    // } printf("\n");
    
    // for(int i=0; i<b; i++) {
    //     a[i] = random_num(10,80);
    //     printf("%d ", a[i]);
    // } printf("\n");
    // int swap = a[0]; a[0] = a[b-1]; a[b-1] = swap;
    // for(int i=0; i<b; i++) {
    //     printf("%d ", a[i]);
    // } printf("\n");

    // for(int i=0; i<b; i++) {
    //     a[i] = random_num(10,80);
    //     printf("%d ", a[i]);
    // } printf("\n");
    // int swap = a[5]; a[5] = a[9]; a[9] = swap;
    // for(int i=0; i<b; i++) {
    //     printf("%d ", a[i]);
    // } printf("\n");

    // for(int i=0; i<b; i++) {
    //     a[i] = random_num(10,90);
    //     printf("%d ", a[i]);
    // } printf("\n");
    // int odd[20], even[20], odd_count = 0, even_count = 0;
    // for(int i=0; i<b; i++) {
    //     if(a[i] % 2) {
    //         odd[odd_count] = a[i];
    //         odd_count++;
    //     } else {
    //         even[even_count] = a[i];
    //         ++even_count;
    //     }
    // }
    //  for(int i = 0; i < odd_count; i++) {
    //     printf("%d ", odd[i]);
    // } printf("\n");
    //  for(int i = 0; i < even_count; i++) {
    //     printf("%i ", even[i]);
    // } printf("\n");

    // for(int i=0; i<b; i++) {
    //     a[i] = random_num(-10,20);
    //     printf("%d ", a[i]);
    // } printf("\n");
    // int pos[20], neg[20], pos_count = 0, neg_count = 0;
    // for(int i=0; i<b; i++) {
    //     if(a[i] >= 0) {
    //         pos[pos_count] = a[i];
    //         pos_count++;
    //     } else {
    //         neg[neg_count] = a[i];
    //         ++neg_count;
    //     }
    // }
    // int swap_p = pos[0]; pos[0] = pos[pos_count-1]; pos[pos_count-1] = swap_p;
    // int swap_n = neg[0]; neg[0] = neg[neg_count-1]; neg[neg_count-1] = swap_n;
    // for(int i = 0; i < pos_count; i++)
    //     printf("%i ", pos[i]);
    // printf("\n");
    // for(int i = 0; i < neg_count; i++)
    //     printf("%d ", neg[i]);
    // printf("\n");
// }
// void array_sorting_ex(int a[], int b) {
    // for(int i=0; i<b; i++) {
    //     a[i] = random_num(1,100);
    //     printf("%d ", a[i]);
    // } printf("\n");
    // int odd[50], even[50], odd_count = 0, even_count = 0;
    // for(int i=0; i<b; i++) {
    //     if(a[i] % 2) {
    //         odd[odd_count] = a[i];
    //         odd_count++;
    //     } else {
    //         even[even_count] = a[i];
    //         ++even_count;
    //     }
    // }
    // int swap;
    // for(int i = 0; i < odd_count; i++) {
    //     for(int j = 0; j < odd_count-1; j++) {
    //         if(odd[j] > odd[j+1]) {
    //             swap = odd[j];
    //             odd[j] = odd[j+1];
    //             odd[j+1] = swap;
    //         }
    //     }
    // }
    // for(int i = 0; i < even_count; i++) {
    //     for(int j = 0; j < even_count-1; j++) {
    //         if(even[j] > even[j+1]) {
    //             swap = even[j];
    //             even[j] = even[j+1];
    //             even[j+1] = swap;
    //         }
    //     }
    // }
    //  for(int i = 0; i < odd_count; i++) {
    //     printf("%d ", odd[i]);
    // } printf("\n");
    //  for(int i = 0; i < even_count; i++) {
    //     printf("%i ", even[i]);
    // } printf("\n");
    
    // for(int i=0; i<b; i++) {
    //     a[i] = random_num(1,100);
    //     printf("%d ", a[i]);
    // } printf("\n");
    // int swap;
    // for(int i=0; i<b; i++) {
    //     for(int j=0; j<b-1; ++j) {
    //         if(a[j] > a[j+1]) {
    //             swap = a[j];
    //             a[j] = a[j+1];
    //             a[j+1] = swap;
    //         }
    //     }
    // }
    // for(int i=0; i<b; i++) {
    //     printf("%d ", a[i]);
    // } printf("\n");
    
    // for(int i=0; i<b; i++) {
    //     a[i] = random_num(-30,30);
    //     printf("%d ", a[i]);
    // } printf("\n");
    // int pos[30], neg[30], pos_count = 0, neg_count = 0;
    // for(int i=0; i<b; i++) {
    //     if(a[i] >= 0) {
    //         pos[pos_count] = a[i];
    //         pos_count++;
    //     } else {
    //         neg[neg_count] = a[i];
    //         ++neg_count;
    //     }
    // }
    // int swap;
    // for(int i = 0; i < pos_count; i++) {
    //     for(int j = 0; j < pos_count-1; j++) {
    //         if(pos[j] > pos[j+1]) {
    //             swap = pos[j];
    //             pos[j] = pos[j+1];
    //             pos[j+1] = swap;
    //         }
    //     }
    // }
    // for(int i = 0; i < neg_count; i++) {
    //     for(int j = 0; j < neg_count-1; j++) {
    //         if(neg[j] > neg[j+1]) {
    //             swap = neg[j];
    //             neg[j] = neg[j+1];
    //             neg[j+1] = swap;
    //         }
    //     }
    // }
    //  for(int i = 0; i < pos_count; i++) {
    //     printf("%d ", pos[i]);
    // } printf("\n");
    //  for(int i = 0; i < neg_count; i++) {
    //     printf("%i ", neg[i]);
    // } printf("\n");
    
    // for(int i=0; i<b; i++) {
    //     a[i] = random_num(-30,30);
    //     printf("%d ", a[i]);
    // } printf("\n");
    // int pos[30], neg[30], pos_count = 0, neg_count = 0;
    // for(int i=0; i<b; i++) {
    //     if(a[i] >= 0 && a[i] % 2) {
    //         pos[pos_count] = a[i];
    //         pos_count++;
    //     } else if(a[i] < 0 && a[i] % 2 == 0) {
    //         neg[neg_count] = a[i];
    //         ++neg_count;
    //     }
    // }
    // int swap;
    // for(int i = 0; i < pos_count; i++) {
    //     for(int j = 0; j < pos_count-1; j++) {
    //         if(pos[j] > pos[j+1]) {
    //             swap = pos[j];
    //             pos[j] = pos[j+1];
    //             pos[j+1] = swap;
    //         }
    //     }
    // }
    // for(int i = 0; i < neg_count; i++) {
    //     for(int j = 0; j < neg_count-1; j++) {
    //         if(neg[j] > neg[j+1]) {
    //             swap = neg[j];
    //             neg[j] = neg[j+1];
    //             neg[j+1] = swap;
    //         }
    //     }
    // }
    //  for(int i = 0; i < pos_count; i++) {
    //     printf("%d ", pos[i]);
    // } printf("\n");
    //  for(int i = 0; i < neg_count; i++) {
    //     printf("%i ", neg[i]);
    // } printf("\n");
    
//     for(int i=0; i<b; i++) {
//         a[i] = random_num(10,90);
//         printf("%d ", a[i]);
//     } printf("\n");
//     int max = INT_MIN, min = INT_MAX, maxINDEX = 0, minINDEX = 0;
//     for(int i=0; i<b; ++i) {
//         if(a[i] > max) {
//             max = a[i];
//             maxINDEX = i;
//         }
//         if(a[i] < min) {
//             min = a[i]; 
//             minINDEX = i;
//         } 
//     }
//     int swap = a[maxINDEX]; a[maxINDEX] = a[minINDEX]; a[minINDEX] = swap;
//     for(int i=0; i<b; ++i) {
//         printf("%i ", a[i]);
//     } printf("\n");
// }
// int main() {
//     system("clear");
//     srand(time(NULL));
//     int n, arr[50];
//     printf("Enter a number of elements: "); scanf("%d",&n);
//     //array_exercises(arr, n);
//     array_sorting_ex(arr, n);
//     return 0;
// }


// float random_float() {
//     return (rand() % 90 + 10) / 12.0 * 0.36;
// }
// int main() {
//     system("clear");
//     srand(time(NULL));
//     float arr_f[50]; int n;
//     printf("Enter a number: "); scanf("%d",&n);
//     for(int i=0; i<n; i++) {
//         arr_f[i] = random_float();
//         printf("%.2f ", arr_f[i]);
//     }
//     float * sum = arr_f;
//     for(int i=1; i<n; ++i) {
//         * sum = arr_f[i];
//     }
//     printf("\nSum = %.3f\n", * sum);
//     return 0;
// }


/*bool prime(int a) {
    int count = 0;
    for(int i=1; i<=a; i++) {
        if(a % i == 0)
            count++;
    }
    if(count <= 2)
        return true;
    else 
        return false;    
}
int find_prime(int a[], int b, int *c) {}*/

// double price(double a, double b) {
//     return a * b;
// }
// double square_triangle(double a, double b) {
//     return a * b / 2;
// }
// int main() {
//     system("clear");
//     double n1, n2;
//     printf("Enter 2 number: "); scanf("%lf%lf", &n1, &n2);
//     double (*functions_double) (double, double) = price;
//     printf("The price of the house: %lf\n", functions_double(n1,n2));
//     functions_double = square_triangle;
//     printf("The square of triangle: %lf\n", functions_double(n1,n2));
//     return 0;
// }


void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
void swap_max_min(int a[], int b) {
    int * max = a, * min = a;
    for(int i=0; i<b; i++) {
        if(*max < a[i])
            max = &a[i];
        if(*min > a[i])
            min = &a[i];    
    }
    swap(max, min);
    for(int i=0; i<b; ++i) {
        printf("%d ",a[i]);
    }
}
int sum_odds(int a) {
    int sum = 0;
    for(int i=0; i<a; i++) {
        if(i % 2)
            sum += i;
    }
    return sum;
}
// int main() {
//     system("clear");
//     srand(time(NULL));
    // 1_ex.
    // int n = 15; int * p_num = &n;
    // printf("%p\n", p_num);
    // printf("%d\n", *p_num);
    // printf("%p\n", &n);
    
    // 2_ex.
    // int n;
    // printf("Enter a number: "); scanf("%d", &n);
    // int * num = &n;
    // *num *= 2;
    // printf("%d\n",n);
    // printf("%d\n",*num);

    // 3_ex.
    // int n1, n2;
    // printf("Enter 2 numbers: "); scanf("%d%d",&n1,&n2);
    // swap(&n1,&n2);
    // printf("A = %d\nB = %d\n",n1,n2);

    // 4_ex.
    // int n = 10, arr[30];
    // int * el = arr;
    // for(int i=0; i<n; i++) {
    //     *el = random_num(10,80);
    //     printf("%d ", *el);
    // } printf("\n");

    // 5_ex.
    // int arr[10];
    // int * el = arr;
    // for(int i=0; i<10; i++) {
    //     *el = random_num(5,50);
    // }
    // printf("%d ", (*el+0));
    // printf("%d ", (*el+1));
    // printf("%d ", (*el+2));
    // printf("%d ", (*el+3));
    // printf("%d ", (*el+4));
    // printf("%d ", (*el+5));
    // printf("%d ", (*el+6));
    // printf("%d ", (*el+7));
    // printf("%d ", (*el+8));
    // printf("%d ", (*el+9));
    
    // 6_ex.
    // int n = 20, arr[20];
    // for(int i=0; i<n; i++) {
    //     arr[i] = random_num(1,100);
    //     printf("%d ",arr[i]);
    // }
    // int * max = arr;
    // for(int i=0; i<n; ++i) {
    //     if(arr[i] > *max)
    //         *max = arr[i];
    // }
    // printf("\nMax: %d\n", *max);

    // 7_ex.
    // int n;
    // printf("Enter a number: "); scanf("%d",&n);
    // int * n_new = n % 10 * 10 + n /10;
    // printf("%d\n", n_new);

    // 8_ex.
    // int n = 20, arr[20];
    // for(int i=0; i<n; i++) {
    //     arr[i] = random_num(10,90);
    //     printf("%d ",arr[i]);
    // } printf("\n");
    // swap_max_min(arr, n);

    // 9_ex.
//     int n;
//     printf("Enter a number: "); scanf("%d",&n);
//     printf("Sum of odds: %d\n", sum_odds(n));
//     return 0;
// }


void show_matrix(int a[][10], int b, int c) {
    for(int i=0; i<b; i++) {
        for(int j=0; j<c; j++) {
            printf("%d  ",a[i][j]);
        }
        printf("\n");
    }
}
/*int main() {
    system("clear");
    srand(time(NULL));
    // int arr[10][10], row, col, res;
    // printf("Enter 2 numbers: "); scanf("%d%d",&row,&col);
    // for(int i=0; i<row; i++) {
    //     for(int j=0; j<col; j++) {
    //         try_again:
    //         res = rand() % 100;
    //         if(res % 2 == 0) {
    //             arr[i][j] = res;
    //         } else {
    //             goto try_again;
    //         }
    //     }
    // }

    // int arr[10][10], n, res;
    // printf("Enter a number: "); scanf("%d",&n);
    // for(int i=0; i<n; i++) {
    //     for(int j=0; j<n; ++j) {
    //         if(i == j || i+j == n-1) {
    //             try:
    //             res = rand() % 100;
    //             if(res % 2)
    //                 arr[i][j] = res;
    //             else
    //                 goto try;    
    //         } else {
    //             try_again:
    //             res = rand() % 100;
    //             if(res % 2 == 0)
    //                 arr[i][j] = res;
    //             else
    //                 goto try_again;
    //         }
    //     }
    // }
    // for(int i=0; i<n; i++) {
    //     for(int j=0; j<n; j++) {
    //         printf("%d ",arr[i][j]);
    //     }
    //     printf("\n");
    // }

    int arr[10][10],row,col;
    printf("Enter 2 numbers: "); scanf("%d%d",&row,&col);
    int el = 0;
    for(int i=0; i<row; i++) {
        for(int j=0; j<col; ++j) {
            arr[i][j] = ++el;
            printf("%4d",arr[i][j]);
        }
        printf("\n");
    }
    printf("After:\n");
    for(int i=0; i<row; i++) {}
    return 0;
}
*/


void swap_max_min_matrix(int a[][10], int b, int c) {
    int max = INT_MIN, min = INT_MAX;
    for(int i=0; i<b; i++) {
        for(int j=0; j<c; ++j) {
            if(a[i][j] > max)
                max = i;
            if(a[i][j] < min)
                min = i;    
        }
    }
    if(a[max] == a[min]) {
        puts("Max and Min are in the same row");
    }
    puts("Result:");
    int temp;
    for(int i=0; i<b; i++) {
        for(int j=0; j<c; ++j) {
            temp = a[max][j];
            a[max][j] = a[min][j];
            a[min][j] = temp;
        }
    }
}

void max_min_matrix(int a[][10], int b, int c) {
    int max = a[0][0], min = a[0][0];
    for(int i=0; i<b; i++) {
        for(int j=0; j<c; ++j) {
            if(i==j || i+j == b-1) {
                if(a[i][j] > max)
                    max = a[i][j];
                if(a[i][j] < min)
                    min = a[i][j];    
            }
        }
    }
    printf("Max = %d\nMin = %d\n",max,min);
}

int main() {
    system("clear");
    srand(time(0));
    int mx[10][10],row,col;
    printf("Enter 2 numbers: "); scanf("%d%d",&row,&col);
    for(int i=0; i<row; i++) {
        for(int j=0; j<col; ++j) {
            mx[i][j] = random_num(10,99);
        }
    }
    //show_matrix(mx,row,col);
    //swap_max_min_matrix(mx,row,col);
    show_matrix(mx,row,col);
    max_min_matrix(mx,row,col);
    return 0;
}