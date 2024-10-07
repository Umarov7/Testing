#include <stdio.h>
#include <stdbool.h>

bool latin(char x) {
    return x > 64 && x < 91 || x > 96 && x < 123 ? true : false;
}
// 1-task
void the_longest_word(char a[]) {
    int start = 0, count = 0, start_max = 0, count_max = 0;
    for(int i=0; a[i] != '\0'; i++) {
        if(a[i] == ' ' || a[i] == '\n') {
            if(count > count_max) {
                count_max = count;
                start_max = start; 
            }
            count = 0;
            start = i+1;  
        } else {
            count++;
        }
    }
    char longest[count_max + 1]; int index = 0;
    for(int i=start_max; i < start_max + count_max; i++) {
        longest[index++] = a[i];
    }
    longest[count_max] = '\0';
    printf("The longest word: %s\n",longest);
}

// 2-task
void words(char a[]) {
    int start = 0, count = 0;
    for(int i=0; a[i] != '\0'; i++) {
        if(latin(a[i]) == false) {
            for(int i=start; i < start + count; ++i) {
                printf("%c",a[i]);
            }
            printf("\n");
            count = 0; start = i+1;
        } else {
            count++;
        }
    }
}

// 3-task
void symbols(char a[]) {
    int count = 0;
    for(int i=0; a[i] != '\0'; i++) {
        if(latin(a[i]) == true || a[i] > 47 && a[i] < 58 || a[i] == '\n') {
            continue;
        } else {
            count++;
        }
    }
    printf("The symbols: %d\n",count);
}

// 4-task
void missing_letters(char a[]) {
    char found_letters[26] = "", letters[26] = "qwertyuiopasdfghjklzxcvbnm";
    for(int i=0; a[i] != '\n' && a[i] != '\0'; i++) {
        if(a[i] > 96 && a[i] < 123) {
            bool check_exist = false;
            for(int j=0; j<26; j++) {
                if(a[i] == found_letters[j]) {
                    check_exist = true;
                    break;
                }
            }
            if(!check_exist) {
                found_letters[i] = a[i];
            }
        }
    }
    printf("Missing letters: ");
    for(int k=0; k < 26; k++) {
        bool check = false;
        for(int l=0; l < 26; l++) {
            if(letters[k] == found_letters[l]) {
                check = true;
                break;
            }
        }
        if(!check) {
            printf("%c ",letters[k]);
        }
    }
}

// 5-task
void uppercase_letters(char a[]) {
    int count = 0;
    for(int i = 0; a[i] != '\n' && a[i] != '\0'; i++) {
        if(a[i] > 64 && a[i] < 91) {
            count++;
        }
    }
    printf("Uppercase letters: %d\n",count);
}

// 6-task
void lowercase_letters(char a[]) {
    int count = 0;
    for(int i = 0; a[i] != '\n' && a[i] != '\0'; i++) {
        if(a[i] > 96 && a[i] < 123) {
            count++;
        }
    }
    printf("Lowercase letters: %d\n",count);    
}

// 7-task
bool is_vowel(char x) {
    if(x == 65 || x == 69 || x == 73 || x == 79 || x == 85)
        return true;
    else if(x == 97 || x == 101 || x == 105 || x == 111 || x == 117)
        return true;
    else
        return false;    
}
void vowels(char a[]) {
    int count = 0;
    for(int i=0; a[i] != '\n' && a[i] != '\0'; ++i) {
        if(is_vowel(a[i]) == true)
            count++;
    }
    printf("Vowels: %d\n",count);
}

// 8-task
bool is_consonant(char x) {
    if(latin(x) == true) {
        if(is_vowel(x) == false) {
            return true;
        }
    }
    return false;
}
int greatest_common_factor(int a, int b) {
    int gcf;
    for(int i=1; i<=a; ++i) {
        if(a % i == 0 && b % i == 0)
            gcf = i;
    }
    return gcf;
}
void ratio(char a[]) {
    int cons = 0, vow = 0;
    for(int i=0; a[i] != '\n' && a[i] != '\0'; i++) {
        if(is_vowel(a[i]) ==  true)
            vow++;
        else if(is_consonant(a[i]) == true)
            cons++;
        else
            continue;
    }
    int ekub = greatest_common_factor(cons,vow);
    printf("Result: %d : %d\n",cons / ekub, vow / ekub);
}

int main() {
    system("clear");
    char str[50];
    printf("Enter a string: "); fgets(str,sizeof(str),stdin);
    
    //the_longest_word(str);
    
    //words(str);

    // char sentence[20];
    // printf("Enter: "); scanf("%[^\n]",sentence);
    // symbols(sentence);

    //missing_letters(str);

    //uppercase_letters(str);

    //lowercase_letters(str);

    //vowels(str);
    
    ratio(str);
    return 0;
}