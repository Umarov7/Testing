#include <stdio.h>

void sort_digits(int n) {
    if(n > 0) {
        sort_digits(n/10);
        int x = n % 10;
        printf("%d ",x);
    }
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    sort_digits(n);
    puts("");
}