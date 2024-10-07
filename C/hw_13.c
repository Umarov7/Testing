#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#include <string.h>

// 1-task
int second_max_element(int a[], int b) {
    int max1 = 0, max2 = 0;
    for(int i = 0; i < b; i++) {
        if(max1 < a[i]) {
            max1 = a[i];
        }
    }
    for(int j = 0; j < b; j++) {
        if(max1 > a[j] && max2 < a[j]) {
            max2 = a[j];
        }
    }
    return max2;
}
void max_second_removal(int *a, int b) {
    printf("Enter the elements: ");
    for(int i=0; i<b; i++) {
        scanf("%d",&*(a+i));
    }
    int index = -1, max2 = second_max_element(a,b);
    for(int j = 0; j < b; j++) {
        if(a[j] == max2)
            index = j;
    }
    printf("Max2 = %d\n",max2);
    printf("Max2 index = %d\n",index);
    for(int k = index; k < b; k++)
        a[k] = a[k+1];
    a[b-1] = '\0';
    for(int i=0; i<b; i++)
        printf("%4d",a[i]);
    puts("");    
}

// 2-task
int second_min_element(int a[], int b) {
    int min1 = INT_MAX, min2 = INT_MAX;
    for(int i = 0; i < b; i++) {
        if(min1 > a[i]) {
            min1 = a[i];
        }
    }
    for(int j = 0; j < b; j++) {
        if(min1 < a[j] && min2 > a[j]) {
            min2 = a[j];
        }
    }
    return min2;
}
void min_second_removal(int *a, int b) {
    printf("Enter the elements: ");
    for(int i=0; i<b; i++) {
        scanf("%d",&*(a+i));
    }
    int index = -1, min2 = second_min_element(a,b);
    for(int j = 0; j < b; j++) {
        if(a[j] == min2)
            index = j;
    }
    printf("Min2 = %d\n",min2);
    printf("Min2 index = %d\n",index);
    for(int k = index; k < b; k++)
        a[k] = a[k+1];
    a[b-1] = '\0';
    for(int i=0; i<b; i++)
        printf("%4d",a[i]);
    puts("");    
}

// 3-task
void remove_target(int a[], int b, int c) {
    printf("Enter the elements: ");
    for(int i=0; i<b; i++) {
        scanf("%d",&*(a+i));
    }
    int target = b-c;
    for(int i = target; i < b; i++) {
        a[i] = '\0';
        if(i != b) {
            continue;
        }
    }
    for(int i=0; i<b; i++)
        printf("%4d",a[i]);
    puts(""); 
}

// 4-task
void info(char a[]) {
    char mx[25][25], * part = strtok(a," \t\n");
    int index = 0;
    while(part != NULL) {
        strcpy(mx[index++],part);
        part = strtok(NULL," \t\n");
    }
    for(int i=0; i<index; i++) {
        printf("%s\n",mx[i]);
    }
}

int main() {
    system("clear");
    int n, *arr;
    printf("Enter a number: "); scanf("%d",&n);
    arr = (int *) calloc(n,sizeof(int));
    
    // max_second_removal(arr,n);
    // min_second_removal(arr,n);
    
    int target;
    printf("Enter a target: "); scanf("%d",&target);
    remove_target(arr,n,target);

    free(arr);

    // char str[50];
    // printf("Enter a string: "); fgets(str,sizeof(str),stdin);
    // info(str);

    return 0;
}