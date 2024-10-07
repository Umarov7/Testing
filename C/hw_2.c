#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

int random_num(int x, int y) {
    return rand() % (y - x + 1) + x;
}
void show_array(int a[], int b) {
    for(int i = 0; i < b; i++)
        printf("%d  ", a[i]);
    printf("\n");    
}

// 1-task
bool prime(int x) {
    for(int i=2; i*i <= x; i++) {
        if(x % i == 0)
            return false;
    }
    return true;
}
int is_prime(int a[], int b) {
    int count = 0;
    puts("Prime:");
    for(int i=0; i<b; i++) {
        if(prime(a[i])) {
            count++;
            printf("%d  ",a[i]);
        }
    }
    printf("\nThe number of prime numbers: %d\n",count);
}

// 2-task
void min_element(int a[], int b) {
    int min = a[0];
    for(int i=0; i < b; i++) {
        if(min > a[i]) {
            min = a[i];
        }
    }
    printf("Min: %d\n",min);
}

// 3-task
void positive_negative(int a[], int b) {
    for(int i=0; i < b; i++) {
        if(a[i] < 0)
            a[i] = 0;
        else
            a[i] = 1;    
    }
    show_array(a,b);
}

// 4-task
void even_elements(int a[], int b) {
    for(int i=0; i < b; i++) {
        if(a[i] % 2 == 0) {
            printf("%c ",43);
        } else {
            printf("%d ",a[i]);
        }
    }
    puts("");
}

// 5-task
void odd_elements(int a[], int b) {
    for(int i=0; i < b; i++) {
        if(a[i] % 2) {
            printf("  ");
        } else {
            printf("%d ",a[i]);
        }
    }
    puts("");    
}

// 6-task
void first_last(int a[], int b) {
    int first = a[0];
    for(int i=0; i < b; i++) {
        a[i] = a[i+1];
        if(i == b-1) {
            a[b-1] = first;
        }
        printf("%d  ",a[i]);
    }
    puts("");
}

int main() {
    system("clear");
    srand(time(NULL));
    int arr[50], n;
    printf("Enter a number of elements: "); scanf("%d",&n);
    // for(int i=0; i < n; i++) {
    //     arr[i] = random_num(1,90);
    // }
    // show_array(arr,n);

    //is_prime(arr,n);
    //min_element(arr,n);
    
    // for(int i=0; i < n; i++) {
    //     arr[i] = random_num(-12,26);
    // }
    // show_array(arr,n);
    // positive_negative(arr,n); 

    // for(int i=0; i < n; i++) {
    //     arr[i] = random_num(14,35);
    // }
    // show_array(arr,n);
    // even_elements(arr,n);

    // for(int i=0; i < n; i++) {
    //     arr[i] = random_num(-46,5);
    // }
    // show_array(arr,n);
    // odd_elements(arr,n);

    for(int i=0; i < n; i++) {
        arr[i] = random_num(-5,25);
    }
    show_array(arr,n);
    first_last(arr,n);
    return 0;
}