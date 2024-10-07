#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// 1-task
typedef struct {
    char name[20];
    int age;
    int stipend;
    int marks[5];
}student;

void print_student(student s) {
    printf("Name:    %s\n",s.name);
    printf("Age:     %d\n",s.age);
    printf("Stipend: %d$\n",s.stipend);
    printf("Marks:   ");
    for(int i=0; i<5; i++) {
        printf("%d ",s.marks[i]);
    }
    printf("\n\n");
}
void mark_4(student s[], int a) {
    int sum;
    for(int i=0; i < a; i++) {
        sum = 0;
        for(int j=0; j<5; j++) {
            sum += s[i].marks[j];
        }
        if(sum / 5 == 4) {
            print_student(s[i]);
        }
    }
}



typedef struct {
    char name[20];
    int stipend, year;
}students;

void show_student(students s) {
    printf("Name:    %s\n",s.name);
    printf("Year:    %d\n",s.year);
    printf("Stipend: %d$\n",s.stipend);
    printf("\n\n");
}
// 2-task
void stipend_sum(students s[], int a) {
    int sum = 0;
    for(int i=0; i<a; i++) {
        if(s[i].year == 2) {
            sum += s[i].stipend;
            show_student(s[i]);
        }
    }
    printf("The total amount of stipend paid for the second year students is %d$\n",sum);
}
// 3-task
void short_name(students s[], int a) {
    for(int i=0; i<a; i++) {
        if(strlen(s[i].name) < 5) {
            puts(s[i].name);
        }
    }
}

int main() {
    system("clear");

    // student sts[4] = {{"Ali",18,150,{5,4,5,5,5}},
    //                          {"Aziz",19,100,{5,2,3,4,4}},
    //                          {"Akbar",18,125,{5,4,5,4,5}},
    //                          {"Komil",20,200,{5,5,5,5,5}}};
    // mark_4(sts,4);

    students Sts[10] = {{"Tom",150,1},
                        {"Alex",100,1},
                        {"Mark",200,2},
                        {"Sam",300,2},
                        {"Frank",250,2},
                        {"Robert",350,2},
                        {"Ron",400,3},
                        {"Will",350,3},
                        {"Xavier",400,4},
                        {"James",500,4}};

    // stipend_sum(Sts,10);

    // short_name(Sts,10);
    return 0;
}