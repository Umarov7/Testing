#include <stdio.h>

// 1-task
void factorial_two(int a[], int b) {
    int res = 2;
    for(int i=0; i < b; i++) {
        a[i] = res * res * i;
        printf("%d  ", a[i]);
    }
    puts("");
}

// 2-task
void arithmetic_progression(int a[], int b, int c) {
    for(int i=0; i < b; i++) {
        a[i] = a[i-1] + c;
        printf("%d  ", a[i]);
    }
    puts("");    
}

// 3-task
void geometric_progression(int a[], int b, int c) {
    for(int i=0; i < b; i++) {
        a[i] = a[i-1] * c;
        printf("%d  ", a[i]);
    }
    puts("");     
}

// 4-task
void fibonacci(int a[], int b) {
    int f1 = 0, f2 = 1, f3;
    for(int i=0; i < b; i++) {
        f3 = f1+f2;
        f1 = f2;
        f2 = f3;
        a[i] = f3;
        printf("%d  ", a[i]);
    }
    puts("");
}

// 5-task
void sum_prequel(int a[], int b, int c, int d) {
    int sum = 0;
    a[0] = c;
    a[1] = d;
    for(int i=2; i < b; i++) {
        if(i == 2) {
            sum += a[i-2];
        }
        sum += a[i-1];
        a[i] = sum;
    }
    for(int i=0; i < b; i++) {
        printf("%d  ", a[i]);
    }
    puts("");     
}

// 6-task
void reverse(int a[], int b) {
    int el = 0;
    for(int i=0; i < b; i++)
        a[i] = ++el;
    for(int i=b-1; i >= 0; i--) {
        printf("%d  ",a[i]);
    }
    puts("");
}

// 7-task
void odd_elements(int a[], int b) {
    int count = 0;
    for(int i=0; i < b; i++) {
        printf("Enter an element: "); scanf("%d",&a[i]);
    }
    printf("Odds: ");
    for(int i=0; i<b; ++i) {
        if(a[i] % 2) {
            count++;
            printf("%d | ",a[i]);
        }
    }
    printf("\nThe odd elements' count: %d\n",count);
}

// 8-task
void even_elements(int a[], int b) {
    int count = 0;
    for(int i=0; i < b; i++) {
        printf("Enter an element: "); scanf("%d",&a[i]);
    }
    printf("Evens: ");
    for(int i = b-1; i >= 0; --i) {
        if(a[i] % 2 == 0) {
            count++;
            printf("%d | ",a[i]);
        }
    }
    printf("\nThe even elements' count: %d\n",count);    
}

// 9-task
void even_odd_elements(int a[], int b) {
    for(int i=0; i < b; i++) {
        printf("Enter an element: "); scanf("%d",&a[i]);
    }
    for(int i=0; i<b; i++) {
        if(a[i] % 2 == 0) {
            printf("%d | ",a[i]);
        }
    }
    for(int i = b-1; i >= 0; --i) {
        if(a[i] % 2) {
            printf("%d | ",a[i]);
        }
    }
    puts("");
}

int main() {
    system("clear");
    srand(time(NULL));
    int arr[50], n, diff, num1, num2;
    printf("Enter a number: "); scanf("%d",&n);

    //factorial_two(arr,n);
    
    // printf("Enter a common difference: "); scanf("%d",&diff);
    // arithmetic_progression(arr,n,diff);
    // geometric_progression(arr,n,diff);

    //fibonacci(arr,n);

    // printf("Enter 2 numbers: "); scanf("%d%d",&num1,&num2);
    // sum_prequel(arr,n,num1,num2);
    
    //reverse(arr,n);
    //odd_elements(arr,n);
    //even_elements(arr,n);
    even_odd_elements(arr,n);
    return 0;
}