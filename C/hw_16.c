#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
// 1-task
void second_word(FILE * a, char * b) {
    int n = strlen(b);
    fwrite(b,sizeof(char),n, a);
    fseek(a,-n*sizeof(char),SEEK_END);
    char res[50];
    int index = 0, space_index;
    fread(b, sizeof(char), n, a);
    for(int i=0; i < strlen(b); i++) {
        if(b[i] == ' ') {
            space_index = i+1;
            break;
        }
    }
    int word_index = space_index;
    while(b[space_index++] != ' ') {
        res[index++] = b[word_index++];
    }
    res[index] = '\0';
    puts(res);
    puts(res);
}

// 2-task
struct country
{
    char name[50];
    char continent[50];
    double population;
    float area; 
    int gdp;
};
typedef struct country Country;
bool check_population(Country c) {
    return c.population > 100;
}

// 3-task
void even_elements(FILE * a, int b) {
    int num;
    for(int i=0; i < b; i++) {
        num = rand() % 100;
        fwrite(&num,sizeof(int),1,a);
        printf("%d ",num);
    }
    fseek(a,-4*b,SEEK_END);
    printf("\nEven numbers: ");
    while(fread(&num,sizeof(num),1,a) != 0) {
        if(num % 2 == 0) {
            printf("%d | ",num);
        }
    }
    puts("");
}

// 4-task
void odd_elements(FILE * a, int b) {
    int num;
    for(int i=0; i < b; i++) {
        num = rand() % 100;
        fwrite(&num,sizeof(int),1,a);
        printf("%d ",num);
    }
    fseek(a,0,SEEK_SET);
    printf("\nOdd numbers: ");
    while(fread(&num,sizeof(num),1,a) != 0) {
        if(num % 2) {
            printf("%d | ",num);
        }
    }
    puts("");
}

// 5-task
void sort_inc(int a[], int b) {
    int temp;
    for(int i=0; i < b-1; i++) {
        for(int j=i; j < b; j++) {
            if(a[i] > a[j]) {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
}
void sort_dec(int a[], int b) {
    int temp;
    for(int i=0; i < b-1; i++) {
        for(int j=i; j < b; j++) {
            if(a[i] < a[j]) {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
}
void numbers(FILE * a, int b) {
    int num;
    for(int i=0; i < b; i++) {
        num = rand() % (51 - -50 + 1) + -50;
        fwrite(&num,sizeof(int),1,a);
        printf("%d ",num);
    }
    rewind(a);
    int odds[50], evens[50], pos_s[50], neg_s[50], o = 0, e = 0, p = 0, n = 0;
    while(fread(&num,sizeof(num),1,a) != 0) {
        if(num % 2) {
            odds[o++] = num;
        } else {
            evens[e++] = num;
        }
        if(num < 0) {
            neg_s[n++] = num;
        } else {
            pos_s[p++] = num;
        }
    }
    sort_inc(evens,e);
    sort_inc(neg_s,n);
    sort_dec(odds,o);
    sort_dec(pos_s,p);
    FILE * odd = fopen("Toq.bin","wb");
    FILE * even = fopen("Juft.bin","wb");
    FILE * pos = fopen("Musbat.bin","wb");
    FILE * neg = fopen("Manfiy.bin","wb");
    for(int i=0; i < e; i++) {
        fwrite(&evens[i],sizeof(int),1,even);
    }
    for(int i=0; i < o; i++) {
        fwrite(&odds[i],sizeof(int),1,odd);
    }
    for(int i=0; i < p; i++) {
        fwrite(&pos_s[i],sizeof(int),1,pos);
    }
    for(int i=0; i < n; i++) {
        fwrite(&neg_s[i],sizeof(int),1,neg);
    }
    fclose(odd);
    fclose(even);
    fclose(pos);
    fclose(neg);
}

// 6-task
void fill_show_array(int a[], int b) {
    for(int i=0; i < b; i++) {
        a[i] = rand() % 100;
        printf("%d  ",a[i]);
    }
    puts("");
}
void local_min(int a[], int b) {
    int count = 0;
    printf("Result:");
    for(int i=0; i < b; i++) {
        if(i > 0 && i < b-1) {
            if(a[i] < a[i-1] && a[i] < a[i+1]) {
                printf("%4d",a[i]);
                count++;
            }
        }
    }
    printf("\nThe number of local minimums: %d\n",count);
}

int main() {
    system("clear");
    chdir("/home/ibrohim/Binary_files");
    /*
    FILE * bf = fopen("task1.bin","wb+");
    if(bf == NULL) {
        puts("Error occured");
        return 0;
    }
    char info[50];
    printf("Enter the input information: "); fgets(info,sizeof(info),stdin);
    second_word(bf,info);
    fclose(bf);
    */

    /*
    FILE * bf = fopen("task2.bin","wb+");
    if(bf == NULL) {
        puts("Error occured");
        return 0;
    }
    Country countries[] = {{"Australia","Australia", 26.8, 7.692, 1.719},
                           {"Brazil","South America", 203.06, 8.515, 4.101},
                           {"Japan","Asia", 125.416, 377.975, 6.495},
                           {"Pakistan","Asia", 241.499, 881.913, 1.568},
                           {"United Kingdom","Europe", 66.971, 242.495, 3.872}};
    fwrite(countries,sizeof(Country),sizeof(countries)/sizeof(Country),bf);
    fseek(bf,0,SEEK_SET);
    FILE * new_f = fopen("Country.html","wb");  
    if(new_f == NULL) {
        puts("Error occured");
        return 0;
    }
    Country con;
    while(fread(&con,sizeof(Country),1,bf) != 0) {
        if(check_population(con)) {
            fwrite(&con.name,sizeof(Country),1,new_f);
        }
    }
    fclose(bf);
    fclose(new_f);
    */

    /*
    srand(time(NULL));
    FILE * bf = fopen("task3.bin","wb+");
    if(bf == NULL) {
        puts("Error occured");
        return 0;
    }
    int n;
    printf("Enter a number: "); scanf("%d",&n);
    even_elements(bf,n);
    fclose(bf);
    */

    /*
    srand(time(NULL));
    FILE * bf = fopen("task4.bin","wb+");
    if(bf == NULL) {
        puts("Error occured");
        return 0;
    }
    int n;
    printf("Enter a number: "); scanf("%d",&n);
    odd_elements(bf,n);
    fclose(bf);
    */

    /*
    FILE * bf = fopen("task5.bin","wb+");
    if(bf == NULL) {
        puts("Error occured");
        return 0;
    }
    int n;
    printf("Enter a number: "); scanf("%d",&n);
    numbers(bf,n);
    fclose(bf);
    */

    srand(time(NULL));
    FILE * bf = fopen("task6.bin","wb+");
    if(bf == NULL) {
        puts("Error occured");
        return 0;
    }
    int n, numbers[50];
    printf("Enter a number: "); scanf("%d",&n);
    fill_show_array(numbers,n);
    local_min(numbers,n);
    fclose(bf);
    return 0;
}