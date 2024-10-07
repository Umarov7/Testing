#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

int random_num(int x, int y) {
    return rand() % (y - x + 1) + x;
}
int max(int a[], int b) {
    int max = INT_MIN, index = -1;
    for(int i=0; i < b; i++) {
        if(a[i] > max) {
            max = a[i];
            index = i;
        }
    }
    return index;
}
int min(int a[], int b) {
    int min = INT_MAX, index = -1;
    for(int i=0; i < b; i++) {
        if(a[i] < min) {
            min = a[i];
            index = i;
        }
    }
    return index;
}

int main() {
    srand(time(0));
    int n, arr[50];
    printf("Enter a number: "); scanf("%d",&n);
    printf("Elements: ");
    for(int i = 0; i < n; i++) {
        arr[i] = random_num(-50,50);
        printf("%4d",arr[i]);
    }
    printf("\n");
    int max_el = max(arr,n);
    int min_el = min(arr,n);
    int count = 0;
    if(min_el < max_el) {
        for(int j = (min_el + 1); j < max_el; j++) {
            count++;
        }
    } else if(max_el < min_el) {
        for(int k = (max_el + 1); k < min_el; k++) {
            count++;
        }
    }
    printf("The numbers between max and min: %d\n",count);
}