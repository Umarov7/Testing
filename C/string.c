#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool latin_letter(char c) {
    return c > 64 && c < 91 || c > 96 && c < 123 ? true : false;
}
int length(char s[]) {
    int count = 0;
    for(int i=0; s[i] != '\0' && s[i] != '\n'; i++) {
        count++;
    }
    return count;
}
int count_latin(char s[]) {
    int count = 0;
    for(int i=0; i < length(s); i++) {
        if(latin_letter(s[i]) == true)
            count++;
    }
    return count;
}
// sum_digit()
void first_digit(char * s) {
    int index_digit = -1;
    for(int i=0; i < length(s); ++i) {
        if(s[i] >= '0' && s[i] <= '9') {
            index_digit = i;
            break;
        }
    }
    if(index_digit < 0) {
        printf("Try again\n");
        return ;
    }
    s[index_digit+1] = '\0';
    puts(s);
}

void string_join(char s[], char c[]) {
    int i=0;
    while(s[i] != '\0')
        i++;
    s[i++] = ' ';
    int j=0;
    while(c[j] != '\0')
        s[i++] = c[j++];
    s[i] = '\0';
    puts(s);        
}

/*int binary_decimal(char s[]) {
    char * reverse; int index = 0;
    for(int i = s; i >= 0; --i) {
        reverse[index++] = s[i];
    }
    for(int i=0; i<sizeof(reverse) / sizeof(char); i++) {
        printf("%c",reverse[i]);
    }
}*/

// void odd_even(int a[]) {
//     int sum = 0, product = 1;
//     for(int i = 0; a[i] != '\n' && a[i] != '\0'; i++) {
//         if(isdigit(a[i])) {
//             if((a[i] - '0') % 2) {
//                 product *= (a[i] - '0');
//             }
//             else if ((a[i] - '0') % 2 == 0){
//                 sum += (a[i] - '0'); 
//             }   
//         }
//     }
//     printf("Product of odds = %d\nSum of evens = %d\n",product,sum);
// }

void copy_str(char a[], char b[]) {
    int i=0;
    while(b[i] != '\0') {
        a[i] = b[i];
        i++;
    }
    a[i] = '\0';
}

void str_contains_word(char a[]) {
    int count_letter = 0, count_word = 0;
    char temp[15], words[50];
    for(int i=0; a[i] != '\0'; i++) {
        if(isalnum(a[i]))
            temp[count_letter++] = a[i];
        else {
            temp[count_letter] = '\0';
            copy_str(words[count_word++],temp);
            temp[0] = '\0';
            count_letter = 0;
        }
    }
    for(int j=0; j<count_word; j++) {
        printf("%d. %s\n",j+1,words);
    }
}

/*void reverse(char a[]) {
    char b[50];
    for(int i = length(a); i >= 0; i--) {
        copy_str(b,a);
    }
}*/

/*void surname_name_lastName(char a[]) {
    char s[15], n[2], l[2], index = 0;
    for(int i=0; a[i] != '\0'; i++) {
        if(isalpha(a[i])) {
            strcpy(s,a[i]);
            n[index++] = a[i];
            l[index++] = a[i];
        } else {
            s[index++] = '\0';
        }
    }
    for(int i=0; i < strlen(s); ++i) {
        printf("%c. %c. %c",n,l,s[i]);
    }
}*/

void count_letters(char a[]) {
    int count = 0;
    for(int i=0; a[i] != '\0'; i++) {
            count++;
            if(strchr(a,a[i])) {
                count++;
            }
            printf("'%c' - %d\n",a[i],count);
            count = 0;
    }
}

int main() {
    system("clear");
    char str[50], str2[50];
    printf("Enter a string: ");
    //scanf("%s",str);
    fgets(str,sizeof(str),stdin);
    str[strlen(str) - 1] = '\0';
    //printf("Latin letters: %d\n",count_latin(str));
    //first_digit(str);
    // printf("Enter a string: "); scanf("%s",str2);
    // string_join(str,str2);
    //binary_decimal(str);

    /*odd_even(str);*/
    //char word[15];
    //printf("Enter a word: "); scanf("%s",word);
    /*str_contains_word(str);
    reverse(str);
    printf("%s",str);*/

    //surname_name_lastName(str);
    
    count_letters(str);
    return 0;
}