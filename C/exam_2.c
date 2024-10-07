#include <stdio.h>

void shiftRight(int *a, int *b, int *c) {
    int *temp;
    temp = c;
    c = b;
    b = a;
    a = temp;
    printf("Result: %d, %d, %d\n",a,b,c);
}

int main() {
    system("clear");
    int *n1, *n2, *n3;
    printf("Enter the first number: ");
    scanf("%d",&n1);
    printf("Enter the second number: ");
    scanf("%d",&n2);
    printf("Enter the third number: ");
    scanf("%d",&n3);
    printf("Result: %d, %d, %d\n",n1,n2,n3);
    shiftRight(n1,n2,n3);
}