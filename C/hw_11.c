#include <stdio.h>

// 1-task
void print_alphabet(char a) {
    if(a <= 'z') {
        printf("%c ",a);
    } else {
        return ;
    }
    print_alphabet(a+1);
}

// 2-task
int remaining_num(int a, int b) {
    static int res;
    if(a >= b) {
        res = a-b;
        return remaining_num(a-b,b);
    } else {
        return res;
    }
}

// 3-task
int multiplication(int a, int b) {
    static int res;
    if(b > 0) {
        res += a;
        return multiplication(a,b-1);
    } else {
        return res;
    }
}

// 4-task
int factorial(int a) {
    if(a == 1) {
        return 1;
    } else {
        return a * factorial(a-1);
    }
}

// 5-task
void fill_arr(int a[], int b) {
    static int i = 0;
    if(i < b) {
        printf("Enter an element: ");
        scanf("%d",&a[i]);
        i++;
        fill_arr(a,b);
    } else {
        return ;
    }
}
void print_arr(int a[], int b) {
    static int i = 0;
    if(i < b) {
        printf("%d  ",a[i++]);
        print_arr(a,b);
    } else {
        puts("");
        return ;
    }
}

// 6-task
void printCalendar(int day) {
    printf("Sun\tMon\tTue\tWed\tThu\tFri\tSat\n");
    printf("%d\t%d\t%d\t%d\t%d\t%d\t%d\n", day, day + 1, day + 2, day + 3, day + 4, day + 5, day + 6);
}
void calendar(int a) {
    static int i = 1;
    if(a >= 1 && a <= 31 && i < 8) {
        i++;
        printCalendar(a);
        calendar(a+7);
    } else {
        return ;
    }
}

int main() {
    system("clear");
    // char letter;
    // printf("Enter a letter: "); scanf("%c",&letter);
    // print_alphabet(letter);

    // int n1, n2;
    // printf("Enter 2 numbers: "); scanf("%d%d",&n1,&n2);
    // printf("The remaining number = %d\n",remaining_num(n1,n2));
    // printf("The multiplication result = %d\n",multiplication(n1,n2));

    int n, arr[50];
    printf("Enter a number: "); scanf("%d",&n);
    //printf("Result: %d\n",factorial(n));
    // fill_arr(arr,n);
    // print_arr(arr,n);
    calendar(n);
    return 0;
}