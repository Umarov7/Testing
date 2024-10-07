#include <stdio.h>
#include <ctype.h>
#include <string.h>

// 1-task
void min_length(char a[]) {
    char min[15] = "";
    int length = 0;
    char * word = strtok(a," \t\n.,!?:;");
    while(word != NULL) {
        if(strlen(word) < length || length == 0) {
            strcpy(min,word);
            length = strlen(word);
        }
        word = strtok(NULL," \t\n.,!?:;");
    }
    printf("The shortest word: %s\n",min);
}

// 2-task
void max_length(char a[]) {
    char max[20] = "";
    int length = 0;
    char * word = strtok(a," \t\n.,!?:;");
    do {
        if(strlen(word) > length || length == 0) {
            strcpy(max,word);
            length = strlen(word);
        }
        word = strtok(NULL," \t\n.,!?:;");
    } while(word != NULL);
    printf("The longest word: %s\n",max);
}

// 3-task
void length_number(char a[], int n) {
    char arr[50] = "";
    char * word = strtok(a," \t\n.,!?:;");
    while(word != NULL) {
        if(strlen(word) > n) {
            if(strcmp(arr,"") == 0) {
                strcpy(arr,word);
            } else {
                strcat(arr,", ");
                strcat(arr,word);
            }
        }
        word = strtok(NULL," \t\n.,!?:;");
    }
    if(strcmp(arr,"") == 0) {
        puts("Not found");
        return ;
    }
    printf("Words: %s\n",arr);
}

// 4-task
void sort_words(char a[]) {
    char arr[50][50], temp[50], * word = strtok(a," \t\n.,!?:;");
    int index = 0;
    while(word != NULL) {
        strcpy(arr[index++],word);
        word = strtok(NULL," \t\n.,!?:;");
    }
    for(int i = 0; i < index - 1; i++) {
        for(int j = i + 1; j < index; ++j) {
            if(strlen(arr[i]) > strlen(arr[j])) {
                strcpy(temp,arr[i]);
                strcpy(arr[i],arr[j]);
                strcpy(arr[j],temp);
            }
        }
    }
    for(int i=0; i < index; i++) {
        printf("%d. %s\n",i+1,arr[i]);
    }
}

// 5-task
void even_length(char a[]) {
    char arr[25][25], * word = strtok(a," \t\n.,!?:;");
    int index = 0;
    while(word != NULL) {
        strcpy(arr[index++],word);
        word = strtok(NULL," \t\n.,!?:;");
    }
    for(int i=0; i < index; ++i) {
        if(strlen(arr[i]) % 2 == 0) {
            for(int j = strlen(arr[i]); j >= 0; j--) {
                printf("%c",(arr[i])[j]);
            }
        } else {
            printf("%s",arr[i]);
        }
        printf(" ");
    }
    puts("");
}

// 6-task
void odd_length(char a[]) {
    char arr[25][25], * word = strtok(a," \t\n.,!?:;");
    int index = 0;
    while(word != NULL) {
        strcpy(arr[index++],word);
        word = strtok(NULL," \t\n.,!?:;");
    }
    for(int i=0; i < index; ++i) {
        if(strlen(arr[i]) % 2) {
            strcpy(arr[i],"String");
            printf("%s ",arr[i]);
        } else {
            printf("%s ",arr[i]);
        }
    }
    puts("");  
}

// 7-task
void solve(char a[]) {
    char numbers[25][25], operators[25];
    int index_n = 0, index_o = 0;
    for(int i=0; a[i] != '\0'; i++) {
        if(a[i] == '+' || a[i] == '-') {
            operators[index_o++] = a[i];
        }
    }
    char * num = strtok(a,"+-");
    while(num != NULL) {
        strcpy(numbers[index_n++],num);
        num = strtok(NULL,"+-");
    }
    int result = atoi(numbers[0]);
    for(int i=0; i < index_o; i++) {
            if(operators[i] == '+') {
                result += atoi(numbers[i+1]);
            } else if(operators[i] == '-') {
                result -= atoi(numbers[i+1]);
            }
    }
    printf("Result: %d\n",result);
}

int main() {
    system("clear");
    char str[50];
    printf("Enter a string: ");
    fgets(str,sizeof(str),stdin);
    str[strlen(str) - 1] = '\0';
    //min_length(str);
    //max_length(str);

    // int num;
    // printf("Enter a number: "); scanf("%d",&num);
    // length_number(str,num);

    //sort_words(str);
    //even_length(str);
    //odd_length(str);
    solve(str);
    return 0;
}