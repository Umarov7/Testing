#include <stdio.h>
#include <stdbool.h> 
#include <string.h>
#define cls system("clear");
#include <limits.h> // INT_MAX and INT_MIN

// int main()
// {
//     system("clear");

    // int bSon = 23;
    // float kSon = 45.86;
    // char harf = 'H';
    // printf("%d, %.2f, %c\n", bSon, kSon, harf);

    // int bSon = 524;
    // float kSon = 85.56;
    // char harf = 'B';
    // printf("%d\n%.2f\n%c\n", bSon, kSon, harf);

    // float son = 45.78;
    // printf("%.1f\n", son);

    // int son = 25;
    // printf("%04d", son);

    // char word[10];
    // printf("Enter a word: ");
    // scanf("%s", word);
    // printf("\"%s\"", word);

    // float num, num2;
    // printf("Enter 2 numbers: ");
    // scanf("%f%f", &num, &num2);
    // printf("1-son: %d\n2-son: %d", (int)num, (int)num2);

    // char letter;
    // printf("Enter an uppercase latin letter: ");
    // scanf("%c", &letter);
    // printf("Uppercase:%c\nLowercase:%c\n", letter, letter + 32);



    // int x, a, b, c, d;
    // printf("Enter a number: ");
    // scanf("%d", &x);
    // a = x / 1000;
    // b = (x / 100) % 10;  
    // c = (x / 10) % 10;
    // d = x % 10;
    // printf("%d\n", a+b+c+d);

    // int x;
    // printf("Enter a number: ");
    // scanf("%d", &x);
    // printf("%d%d%d%d%d%d\n", x, x, x, x, x, x);
    // printf("%d    %d\n", x, x);
    // printf("%d    %d\n", x, x);
    // printf("%d%d%d%d%d%d\n", x, x, x, x, x, x);

    // int x;
    // printf("Enter a number: ");
    // scanf("%d", &x);
    // printf("%d\n%c\n", x, x);

//     return 0;
// }



// int main()
// {
//     system("clear");

//     int a, b;
//     printf("Enter 2 inequal numbers: ");
//     scanf("%d%d", &a, &b);
//     if (a > b) {
//         printf("%d<%d\n", b, a);
//     } else {
//         printf("%d<%d\n", a, b);
//     }

//     return 0;
// }

// int main()
// {
//     system("clear");

//     int uzb, ind;
//     printf("Hisobni kiriting: ");
//     scanf("%d:%d", &uzb, &ind);
//     if (uzb > ind) {
//         printf("1. Uzb-3\n2. Ind-0");
//     } else if (ind > uzb) {
//         printf("1. Ind-3\n2. Uzb-0");
//     } else {
//         printf("1. Uzb-1\n2. Ind-1");
//     }

//     return 0;
// }

// int main() 
// {
//     system("clear");

//     int a, b, c;
//     printf("Enter 3 numbers: ");
//     scanf("%d%d%d", &a, &b, &c);
//     int min = a < b && a < c ? a : b < a && b < c ? b : c;
//     printf("Result = %d\n", min);

//     return 0;
// }

// int main()
// {
//     system("clear");
//     int a, b, c;
//     printf("Enter 3 number: ");
//     scanf("%d%d%d", &a, &b, &c);
//     int max = a > b && a > c ? a : b > a && b > c ? b : c;
//     int min = a < b && a < c ? a : b < a && b < c ? b : c;
//     printf("Max(%d,%d,%d)=%d\nMin(%d,%d,%d)=%d\n", a, b, c, max, a, b, c, min);
//     return 0;
// }

// int main()
// {
//     system("clear");
//     char c[20];
//     printf("Enter a colour: ");
//     scanf("%s", c);
//     if(strcasecmp(c, "red") == 0) {
//         printf("Stop\n");
//     } else if(strcasecmp(c, "yellow") == 0) {
//         printf("Get ready\n");
//     } else if(strcasecmp(c, "green") == 0) {
//         printf("Go\n");
//     } else {
//         printf("Be careful\n");
//     }
//     return 0;
// }

// int main()
// {
//     system("clear");
//     int age;
//     printf("Enter your age: ");
//     scanf("%d", &age);
//     if(age <= 7) {
//         printf("Free\n");
//     } else if (age > 7 && age < 19) {
//         printf("15000\n");
//     } else {
//         printf("25000\n");
//     }
    
//     return 0;
// }

// int main()
// {
//     system("clear");
//     int t;
//     printf("Enter the time you're using it: ");
//     scanf("%d", &t);
//     if(t == 1) {
//         printf("10%%\n");
//     } else if(t == 2) {
//         printf("15%%\n");
//     } else if(t >= 3) {
//         printf("20%c\n", '%');
//     } else {
//         printf("Try again");
//     }
//     return 0;
// }

// int main()
// {
//     system("clear");
//     char m[10];
//     printf("Enter a model: ");
//     scanf("%s", m);
//     if(strcasecmp(m, "Damas") == 0)
//     {
//         printf("100 mln.\n");
//     } else if (strcasecmp(m, "Spark") == 0)
//     {
//         printf("90 mln.\n");
//     } else if (strcasecmp(m, "Kaptiva") == 0)
//     {
//         printf("300 mln.\n");
//     } else if (strcasecmp(m, "Nexia") == 0)
//     {
//         printf("125 mln.\n");
//     } else if (strcasecmp(m, "Malibu") == 0)
//     {
//         printf("400 mln.\n");
//     } else
//     {
//         printf("Try again\n");
//     }
//     return 0;
// }

// int main()
// {
//     system("clear");
//     int a, b, c;
//     printf("Enter 3 numbers: ");
//     scanf("%d%d%d", &a, &b, &c);
//     int max = (a > b)?((a > c) ? a : c):((b > c) ? b : c);
//     printf("Max(%d, %d, %d)=%d\n", a, b, c, max);
//     return 0;
// }

// int main()
// {
//     system("clear");
//     int season;
//     printf("1. Winter\n2. Spring\n3. Summer\n4. Autumn\n");
//     printf("Choose the one: ");
//     scanf("%d", &season);
//     switch (season)
//     {
//     case 1: printf("1. December\n2. January\n3. February\n");
//         break;
//     case 2: printf("1. March\n2. April\n3. May\n");
//         break;
//     case 3: printf("1. June\n2. July\n3. August\n");
//         break;
//     case 4: printf("1. September\n2. October\n3. November\n");
//         break;        
//     default: printf("Try again\n");
//         break;
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     double value; char distance;
//     printf("m = millimetr\ns = santimetr\nd = detsimetr\nM = metr\nk = kilometr\n");
//     printf("Enter the distance: "); scanf("%lf%c", &value, &distance);
//     switch (distance)
//     {
//     case 'm':
//         printf("%.2lf millimetr = %.2lf metr\n", value, value/1000);
//         break;
//     case 's':
//         printf("%.2lf santimetr = %.2lf metr\n", value, value/100);
//         break;
//     case 'd':
//         printf("%.2lf detsimetr = %.2lf metr\n", value, value/10);
//         break;    
//     default:
//         printf("Try again\n");
//         break;
//     case 'M':
//         printf("%.2lf metr = %.2lf metr\n", value, value);
//         break;
//     case 'k':
//         printf("%.2lf kilometr = %.2lf metr\n", value, value*1000);
//         break;        
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     int date;
//     printf("Enter a date: "); scanf("%d", &date);
//     switch (date % 7)
//     {
//     case 1:
//         printf("Monday\n");
//         break;
//     case 2:
//         printf("Tuesday\n");
//         break;
//     case 3:
//         printf("Wednesday\n");
//         break;
//     case 4:
//         printf("Thursday\n");
//         break;
//     case 5:
//         printf("Friday\n");
//         break;
//     case 6:
//         printf("Saturday\n");
//         break;
//     case 0:
//         printf("Sunday\n");
//         break;                    
//     default:
//         printf("Try again\n");
//         break;
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     int mark; Home:
//     printf("Enter a mark: "); scanf("%d", &mark);
//     switch (mark)
//     {
//     case 10:
//     case 9:
//         printf("A\n");
//         break;
//     case 8:
//         printf("B\n");
//         break;
//     case 7:
//         printf("C\n");
//         break;
//     case 6:
//         printf("D\n");
//         break;
//     case 0 ... 5:
//         printf("F\n");
//         break;            
//     default:
//         printf("Try again\n");
//         break;
//     }
//     goto Home;
//     return 0;
// }

// int main()
// {
//     cls
//     int a, b; char op;
//     printf("Enter 2 numbers and an operator: ");
//     scanf("%d%c%d", &a, &op, &b);
//     switch (op)
//     {
//     case '+':
//         printf("%d + %d = %d\n", a, b, a + b);
//         break;
//     case '-':
//         printf("%d - %d = %d\n", a, b, a - b);
//         break;
//     case '*':
//         printf("%d x %d = %d\n", a, b, a * b);
//         break;  
//     case ':':
//         printf("%d : %d = %d\n", a, b, a / b);
//         break;
//     case '%':
//         printf("%d %% %d = %d\n", a, b, a % b);
//         break;          
//     default:
//         printf("Try again\n");
//         break;
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     int x;
//     printf("Enter a number: "); scanf("%d", &x);
//     switch (x)
//     {
//     case 1:
//         printf("Open calculator\n");
//         break;
//     case 2:
//         printf("Open calendar\n");
//         break;
//     case 3:
//         printf("Stop the programme\n");
//         break;    
//     default:
//         printf("Try again\n");
//         break;
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     int month;
//     printf("Enter a number: "); scanf("%d", &month);
//     switch (month)
//     {
//         case 1:
//             printf("January\n");
//             break;
//         case 2:
//             printf("February\n");
//             break;
//         case 3:
//             printf("March\n");
//             break;
//         case 4:
//             printf("April\n");
//             break;
//         case 5:
//             printf("May\n");
//             break;
//         case 6:
//             printf("June\n");
//             break;
//         case 7:
//             printf("July\n");
//             break;
//         case 8:
//             printf("August\n");
//             break;
//         case 9:
//             printf("September\n");
//             break;
//         case 10:
//             printf("October\n");
//             break;
//         case 11:
//             printf("November\n");
//             break;
//         case 12:
//             printf("December\n");
//             break;                                            
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     int month;
//     printf("Enter a month_number: "); scanf("%d", &month);
//     switch (month)
//     {
//         case 1:
//             printf("January-31\n");
//             break;
//         case 2:
//             printf("February-28/29\n");
//             break;
//         case 3:
//             printf("March-31\n");
//             break;
//         case 4:
//             printf("April-30\n");
//             break;
//         case 5:
//             printf("May-31\n");
//             break;
//         case 6:
//             printf("June-30\n");
//             break;
//         case 7:
//             printf("July-31\n");
//             break;
//         case 8:
//             printf("August-31\n");
//             break;
//         case 9:
//             printf("September-30\n");
//             break;
//         case 10:
//             printf("October-31\n");
//             break;
//         case 11:
//             printf("November-30\n");
//             break;
//         case 12:
//             printf("December-31\n");
//             break;  
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     char l;
//     printf("Enter a letter: "); scanf("%c", &l);
//     switch (l)
//     {
//         case 'a':
//         case 'o':
//         case 'i':
//         case 'u':
//         case 'e':
//             printf("Vowel\n");
//             break;
//         default:
//             printf("Consonant\n");
//             break;    
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     int month;
//     printf("Enter a month_number: "); scanf("%d", &month);
//     switch (month)
//     {
//         case 1:
//         case 2:
//         case 12:
//             printf("Winter\n");
//             break;
//         case 3 ... 5:
//             printf("Spring\n");
//             break;
//         case 6 ... 8:
//             printf("Summer\n");
//             break;
//         case 9 ... 11:
//             printf("Autumn\n");
//             break;
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     char word;
//     printf("Enter a word: "); scanf("%c", &word);
//     switch (word)
//     {
//         case 'b':
//         case 'B':
//             printf("book-kitob\n");
//             break;
//         case 'p':
//         case 'P':
//             printf("pen-ruchka\n");
//             break;
//         case 'h':
//         case 'H':
//             printf("home-uy\n");
//             break;
//         case 's':
//         case 'S':
//             printf("school-maktab\n");
//             break;
//         default:
//             printf("Try another word\n");
//             break;              
//     }
//     return 0;
// }

/*int main()
{
    cls
    int n;
    printf("Enter a number: "); scanf("%d", &n);
    if(n > 9999) {
        printf("Try another number\n");
        goto error;
    }
    switch (n / 1000)
    {
        case 1: printf("Bir ming ");break;
        case 2: printf("Ikki ming ");break;
        case 3: printf("Uch ming ");break;
        case 4: printf("To'rt ming ");break;
        case 5: printf("Besh ming ");break;
        case 6: printf("Olti ming ");break;
        case 7: printf("Yetti ming ");break;
        case 8: printf("Sakkiz ming ");break;
        case 9: printf("To'qqiz ming ");break;
    }
    switch ((n / 100) % 10)
    {
        case 1: printf("bir yuz ");break;
        case 2: printf("ikki yuz ");break;
        case 3: printf("uch yuz ");break;
        case 4: printf("to'rt yuz ");break;
        case 5: printf("besh yuz ");break;
        case 6: printf("olti yuz ");break;
        case 7: printf("yetti yuz ");break;
        case 8: printf("sakkiz yuz ");break;
        case 9: printf("to'qqiz yuz ");break;
    }
    switch ((n / 10) % 10)
    {
        case 1: printf("o'n ");break;
        case 2: printf("yigirma ");break;
        case 3: printf("o'ttiz ");break;
        case 4: printf("qirq ");break;
        case 5: printf("ellik ");break;
        case 6: printf("oltmish ");break;
        case 7: printf("yetmish ");break;
        case 8: printf("sakson ");break;
        case 9: printf("to'qson ");break;
    }
    switch (n % 10)
    {
        case 1: printf("bir\n");break;
        case 2: printf("ikki\n");break;
        case 3: printf("uch\n");break;
        case 4: printf("to'rt\n");break;
        case 5: printf("besh\n");break;
        case 6: printf("olti\n");break;
        case 7: printf("yetti\n");break;
        case 8: printf("sakkiz\n");break;
        case 9: printf("to'qqiz\n");break;
    }
    error:    
    return 0;
}


int main()
{
    cls
    double value; char currency;
    printf("s = so'm\nf = funt\nt = tenge\nd = dollar\nr = rubl\n");
    printf("Enter a value and a currency: "); scanf("%lf_%c", &value, &currency);
    switch (currency)
    {
        case 's': printf("%.2lf so'm = %.2lf so'm\n", value, value);break;
        case 'f': printf("%.2lf funt = %.2lf so'm\n", value, value * 14832.92);break;
        case 't': printf("%.2lf tenge = %.2lf so'm\n", value, value * 25.55);break;
        case 'd': printf("%.2lf dollar = %.2lf so'm\n", value, value * 12198.13);break;
        case 'r': printf("%.2lf rubl = %.2lf so'm\n", value, value * 121.39);break;
    }
    return 0;
}

int main()
{
    cls
    double value; char units;
    printf("b = bit\nB = byte\nk = kilobyte\nm = megabyte\ng = gigabyte\n");
    printf("Enter a value and a unit of information: "); scanf("%lf_%c", &value, &units);
    switch (units)
    {
        case 'B': printf("%.2lf bytes = %.2lf bytes\n", value, value);break;
        case 'b': printf("%.2lf bits = %.2lf bytes\n", value, value * 0.13);break;
        case 'k': printf("%.2lf kilobytes = %.2lf bytes\n", value, value * 1024);break;
        case 'm': printf("%.2lf megabytes = %.2lf bytes\n", value, value * 1048576);break;
        case 'g': printf("%.2lf gigabytes = %.2lf bytes\n", value, value * 1073741824);break;
    }
    return 0;
}

int main()
{
    cls
    int year;
    printf("Enter a year: "); scanf("%d",&year);
    int colour = (year % 10) / 2;
    int animal = year % 12;
    switch (colour)
    {
        case 0: printf("Green ");break;
        case 1: printf("Red ");break;
        case 2: printf("Yellow ");break;
        case 3: printf("White ");break;
        case 4: printf("Black ");break;
    }
    switch (animal)
    {
        case 0: printf("monkey\n");break;
        case 1: printf("rooster\n");break;
        case 2: printf("dog\n");break;
        case 3: printf("pig\n");break;
        case 4: printf("rat\n");break;
        case 5: printf("bull\n");break;
        case 6: printf("tiger\n");break;
        case 7: printf("rabbit\n");break;
        case 8: printf("dragon\n");break;
        case 9: printf("snake\n");break;
        case 10: printf("horse\n");break;
        case 11: printf("sheep\n");break;
    }
    return 0;
}

int main()
{
    cls
    int day, month;
    printf("Enter a birth date: "); scanf("%d-%d",&day,&month);
    switch (month)
    {
        case 1:
            if(day < 20)
                printf("Capricorn\n");
            else
                printf("Aquarius\n");break;
        case 2:
            if(day < 19)
                printf("Aquarius\n");
            else
                printf("Pisces\n");break;
        case 3:
            if(day < 21)
                printf("Pisces\n");
            else
                printf("Aries\n");break;
        case 4:
            if(day < 20)
                printf("Aries\n");
            else
                printf("Taurus\n");break;
        case 5:
            if(day < 21)
                printf("Taurus\n");
            else
                printf("Gemini\n");break;
        case 6:
            if(day < 21)
                printf("Gemini\n");
            else
                printf("Cancer\n");break;
        case 7:
            if(day < 23)
                printf("Cancer\n");
            else
                printf("Leo\n");break;
        case 8:
            if(day < 23)
                printf("Leo\n");
            else
                printf("Virgo\n");break;
        case 9:
            if(day < 23)
                printf("Virgo\n");
            else
                printf("Libra\n");break;
        case 10:
            if(day < 23)
                printf("Libra\n");
            else
                printf("Scorpio\n");break;
        case 11:
            if(day < 23)
                printf("Scorpio\n");
            else
                printf("Sagittarius\n");break;
        case 12:
            if(day < 22)
                printf("Sagittarius\n");
            else
                printf("Capricorn\n");break;                                                                                            
    }
    return 0;
}*/


// int main()
// {
//     cls
//     int a = 100;
//     while (a >= 1) 
//     {
//         printf("%d, ", a);
//         a -= 2;
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     int n, odds = 0, sum = 0;
//     while (1)
//     {
//         printf("Enter a number: ");
//         scanf("%d", &n);
//         if(n == 0)
//             break;
//         if(n % 2) {
//             odds++;
//             sum += n; 
//         } 
//     }
//     printf("%d - %d\n", odds, sum);
//     return 0;
// }

// int main()
// {
//     cls
//     char a, b;
//     printf("Enter 2 signs: "); scanf("%c_%c", &a, &b);
//     do
//     {
//         if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u') {
//             printf("%c ", a);
//         }
//         if (a == 'A' || a == 'E' || a == 'I' || a == 'O' || a == 'U') {
//             printf("%c ", a);
//         }
//         a++;
//     } while (a <= b);
//     return 0;
// }

// int main()
// {
//     cls
//     int a, b, sum = 0;
//     printf("Enter 2 numbers: "); scanf("%d%d",&a,&b);
//     do
//     {
//         if (a % 7 == 0) {
//             sum += a;
//         }
//         a++;
//     } while (a <= b);
//     printf("Result is %d\n", sum);
//     return 0;
// }

// int main()
// {
//     cls
//     float a, b, sum = 0, count = 0;
//     printf("Enter 2 numbers: "); scanf("%f%f",&a,&b);
//     do
//     {
//         sum += a;
//         count++;
//         ++a;
//     } while (a <= b);
//     printf("Result = %.3f\n", sum / count);
//     return 0;
// }

// int main()
// {
//     cls
//     int n, a, b, x, count = 0;
//     printf("Enter a number of numbers you'd like to enter: "); scanf("%d",&n);
//     printf("Enter a and b: "); scanf("%d%d",&a,&b);
//     do
//     {
//         printf("Enter a number: "); scanf("%d",&x);
//         if(x > a && x < b) {
//             count++;
//         }
//         --n;
//     } while(n > 0);
//     printf("The result is %d\n", count);
//     return 0;
// }



/*int main()
{
    cls
    int n, res = 1;
    printf("Enter a number: "); scanf("%d",&n);
    while (n >= 1) {
        res *= n;
        --n;
    }
    printf("%d\n",res);
    return 0;
}

int main()
{
    cls
    int k,n,sum = 0;
    printf("Enter 2 numbers: "); scanf("%d%d",&k,&n);
    k++;
    while(k < n)
    {
        if(k % 3 == 0 && k % 5) {
            sum += k;
        }
        ++k;
    }
    printf("%d\n",sum);
    return 0;
}

int main()
{
    cls
    int a,b;
    printf("Enter 2 numbers: "); scanf("%d%d",&a,&b);
    int n = a > b ? a : b;
    while(1)
    {
        if(n % a == 0 && n % b == 0) {
            printf("%d\n",n);
            break;
        }
        ++n;
    }
    return 0;
}

int main()
{
    cls
    int x = 15, y, tries = 0;
    while(1)
    {
        printf("Enter a number: "); scanf("%d",&y);
        if(x == y) {
            printf("It's taken %d tries to find the number\n",tries);
            break;
        } else {
            tries++;
        }
    }
    return 0;
}

int main()
{
    cls
    int n, min;
    printf("Enter a number of numbers you'd like to enter: "); scanf("%d",&n);
    printf("Enter a number: "); scanf("%d",&min);
    while(n > 1) {
        int num;
        printf("Enter a number: "); scanf("%d",&num);
        if(min > num) {
            min = num;
        }
        --n;
    }
    printf("The minimum number entered is: %d\n",min);
    return 0;
}

int main()
{
    cls
    int n, res = 1;
    while(1)
    {
        printf("Enter a number: "); scanf("%d",&n);
        if(n < 0) {
            res *= n;
        } else if(n == 0) {
            break;
        }
    }
    printf("The result is %d\n",res);
    return 0;
}*/

// int main()
// {
//     cls
//     int n = 1, sum = 0;
//     while(n <= 100) {
//         sum += n;
//         if(sum >= 100) {
//             printf("%d\n",n);
//             break;
//         }
//         n++;
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     int n = 5, num, max = 0;
//     while(n >= 1)
//     {
//         printf("Enter a number: "); scanf("%d",&num);
//         if(num > max) {
//             max = num;
//         }
//         --n;
//     }
//     printf("Max is %d\n",max);
//     return 0;
// }

// int main()
// {
//     cls
//     int n = 5, num, min;
//     while(n >= 1)
//     {
//         printf("Enter a number: "); scanf("%d",&num);
//         if(num < min) {
//             min = num;
//         }
//         --n;
//     }
//     printf("Min is %d\n",min);
//     return 0;
// }

// int main()
// {
//     cls
//     int n, i = 1, d;
//     printf("Enter a number: "); scanf("%d",&n);
//     while(i <= 99)
//     {
//         if(n % i == 0) {
//             printf("%d\n",i);
//         }
//         i++;
//     }
//     return 0;
// }

// int main()
// {
//     cls
//     int n, c = 0, sum = 0;
//     while(1)
//     {
//         printf("Enter a number: "); scanf("%d",&n);
//         if(n <= 0) {
//             break;
//         }
//         c++;
//         sum += n;
//     }
//     printf("Sum:%d\nAverage:%d\nNumber:%d\n",sum,sum / c, c);
//     return 0;
// }

/*int main()
{
    cls
    int n, res = 1;
    printf("Enter a number: "); scanf("%d",&n);
    do
    {
        res *= n;
        --n;
    } while (n >= 1);
    printf("%d\n",res);
    return 0;    
}

int main()
{
    cls
    int k,n,sum = 0;
    printf("Enter 2 numbers: "); scanf("%d%d",&k,&n);
    k++;
    do
    {
        if(k % 3 == 0 && k % 5) {
            sum += k;
        }
        ++k;
    } while(k < n);
    printf("%d\n",sum);
    return 0;    
}

int main()
{
    cls
    int a,b;
    printf("Enter 2 numbers: "); scanf("%d%d",&a,&b);
    int n = a > b ? a : b;
    do
    {
        if(n % a == 0 && n % b == 0) {
            printf("%d\n",n);
            break;
        }
        ++n;
    } while(1);
    return 0;    
}

int main()
{
    cls
    int x = 15, y, tries = 0;
    do
    {
        printf("Enter a number: "); scanf("%d",&y);
        if(x == y) {
            printf("It's taken %d tries to find the number\n",tries);
            break;
        } else {
            tries++;
        }
    } while(1);
    return 0;    
}

int main()
{
    cls
    int n, min;
    printf("Enter a number of numbers you'd like to enter: "); scanf("%d",&n);
    printf("Enter a number: "); scanf("%d",&min);
    do 
    {
        int num;
        printf("Enter a number: "); scanf("%d",&num);
        if(min > num) {
            min = num;
        }
        --n;
    } while(n > 1);
    printf("The minimum number entered is: %d\n",min);
    return 0;    
}

int main()
{
    cls
    int n, res = 1;
    do
    {
        printf("Enter a number: "); scanf("%d",&n);
        if(n < 0) {
            res *= n;
        } else if(n == 0) {
            break;
        }
    } while(1);
    printf("The result is %d\n",res);
    return 0;    
}*/

// int main()
// {
//     cls
//     int a, b, sum = 0, mult = 1;
//     printf("Enter 2 numbers: "); scanf("%d%d",&a,&b);
//     for (int i = a; i <= b; i++)
//     {
//         if (i % 2 != 0) {
//             mult *= i;
//         } else {
//             sum += i;
//         }
//     }
//     printf("Sum:%d\nMultiplied result:%d\n",sum,mult);
//     return 0;
// }

// int main()
// {
//     cls
//     int n, num, e = -1;
//     printf("Enter a number of numbers you'd like to enter: "); scanf("%d",&n);
//     for (int i = n; i >= 1; i--)
//     {
//         printf("Enter a number: "); scanf("%d",&num);
//         if (num % 2 == 0 && e == -1) {
//             e = num;
//         }
//     }
//     printf("Result:%d\n",e);
//     return 0;
// }

// int main()
// {
//     cls
//     int n, res = 1;
//     printf("Enter a number: "); scanf("%d",&n);
//     for (int i = n; i >= 1; --i)
//     {
//         res *= i;
//     }
//     printf("Result:%d\n",res);
//     return 0;
// }

/*int main()
{
    cls
    int n;
    printf("Enter a number: "); scanf("%d",&n);
    for (int i = n; i >= 0; i--)
    {
        if (i % 2 == 0)
        {
            printf("%d\n",i);
        }
        
    }
    return 0;
}
int main()
{
    cls
    int n;
    printf("Enter a number: "); scanf("%d",&n);
    for (int i = n; i >= 0; --i)
    {
        if (i % 2) {
            printf("%d\n",i);
        }
    }
    return 0;
}
int main()
{
    cls
    int n, count = 0;
    printf("Enter a number: "); scanf("%d",&n);
    for (int i = 1; i <= n; ++i)
    {
        if (n % i == 0)
        {
            count++;
        }
    }
    if (count > 2)
    {
        printf("%d - complex\n",n);
    } else if (n / 1 && n / n)
    {
        printf("%d - prime\n",n);
    }
    return 0;
}
int main()
{
    cls
    int a,b,c;
    for (int i = 100; i < 1000; ++i)
    {
        a = i / 100;
        b = (i / 10) % 10;
        c = i % 10;
        if (a == b || a == c || b == a || b == c || c == a || c == b)
        {
            printf("%i: ",i);
        }
    }
    return 0;
}
int main()
{
    cls
    int n,c,r = 0;
    printf("Enter a number: "); scanf("%d",&n);
    c = n;
    for(;n>0;n/=10) {
        r = r * 10 + n % 10;
    }
    while (r)
    {
        printf("%d ", r%10);
        r /= 10;
    }
    for(;;c/=10)
    {
        if(c % 10 != 0)
            break;
        printf("%d ",c%10);    
    }
    return 0;
}
int main()
{
    cls
    int a,b,c;
    printf("Enter 3 numbers: "); scanf("%d%d%d",&a,&b,&c);
    for(int i=2;i<=a;i++) {
        if(a%i==0 && b%i==0 && c%i==0) {
            printf("Result:%d\n",i);
            break;
        }
    }
    return 0;
}
int main()
{
    cls
    int n, f1 = 0, f2 = 1, f3;
    printf("Enter a number: "); scanf("%d",&n);
    for(; f1+f2 < n;) {
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
        printf("%d\n",f3);
    }
    return 0;
}*/


// int main()
// {
//     cls
//     int n, i = 1, sum = 0;
//     printf("Enter a number: "); scanf("%d",&n);
//     do
//     {
//         if (n % i == 0)
//         {
//             sum += i;
//         }
//         ++i;
//     } while (i < n);
//     if (n == sum)
//     {
//         printf("%d - mukammal son\n",n);
//     } else
//     {
//         printf("%d - mukammal son emas\n",n);
//     }
//     return 0;
// }
// int main()
// {
//     cls
//     int n,m1,m2;
//     while(1) {
//         printf("Enter a number: "); scanf("%d",&n);
//         if(n < 0) {
//             break;
//         }
//         if(n > m1) {
//             m2 = m1;
//             m1 = n;
//         } else if(n > m2 && n < m1) {
//             m2 = n;
//         }
//     }
//     printf("The 2nd max=%d\n",m2);
//     return 0;
// }



// int main()
// {
//     cls
//     char l = 65;
//     while(l < 70) {
//         for(int c=1; c<=7; ++c) {
//             printf("%c ",l);
//         }
//         ++l;
//         printf("\n");
//     }
//     return 0;
// }
// int main()
// {
//     cls
//     char l; int n;
//     printf("Enter a number: "); scanf("%d",&n);
//     for(int i=65; i<65+n; ++i) {
//         l = 'A';
//         while(l <= i) {
//             printf("%c ",l);
//             ++l;
//         }
//         printf("\n");
//     }
//     return 0;
// }
// int main()
// {
//     cls
//     int d;
//     printf("Enter a distance: "); scanf("%d",&d);
//     d = (d + 2) / 3;
//     printf("%d\n",d);
//     return 0;
// }
// int main()
// {
//     cls
//     int n;
//     printf("Enter a number: "); scanf("%d",&n);
//     for(int i=1; i<=n; i++) {
//         for(int j=1; j<=n; ++j) {
//             if(i==1 || j==1 || i==n || j==n) 
//                 printf("* ");
//             else if(i<=j && i+j <= n+1)
//                 printf("* ");    
//             else 
//                 printf("  ");    
//         }
//         printf("\n");
//     }
//     return 0;
// }



// int main()
// {
//     cls
//     int a,b,c,d;
//     printf("Enter 4 numbers: "); scanf("%d%d%d%d",&a,&b,&c,&d);
//     if(a == b)
//         printf("%d-%d\n",c,d);
//     else if(a == c)
//         printf("%d-%d\n",b,d);
//     else if(a == d)
//         printf("%d-%d\n",b,c);
//     else if(b == c)
//         printf("%d-%d\n",a,d);
//     else if(b == d)
//         printf("%d-%d\n",a,c);
//     else
//         printf("%d-%d\n",a,b);            
//     return 0;
// }
// int main()
// {
//     cls
//     int x,h,m;
//     printf("Enter the current time: "); scanf("%d:%d",&h,&m);
//     printf("Enter the minutes: "); scanf("%d",&x);
//     m += x;
//     if(m >= 60) {
//         m -= 60;
//         h++;
//     }
//     if(h == 24) {
//         h -= 24;
//     }
//     printf("After %d minutes: %02d:%02d\n",x,h,m);
//     return 0;
// }

/*int main()
{
    cls
    char dir; int order;
    printf("Enter the current direction: "); scanf("%c",&dir);
    printf("Enter the order: "); scanf("%d",&order);
    switch(dir)
    {
        case 'N':
        switch (order)
        {
        case 1: printf("Robot has turned to east\n"); break;
        case 2: printf("Robot has turned to west\n"); break;
        case 3: printf("Robot has turned to south\n"); break;
        case 4: printf("Robot has remained at north\n"); break;
        default: break;
        }
        break;

        case 'S':
        switch (order)
        {
        case 1: printf("Robot has turned to west\n"); break;
        case 2: printf("Robot has turned to east\n"); break;
        case 3: printf("Robot has turned to north\n"); break;
        case 4: printf("Robot has remained at south\n"); break;
        default: break;
        }
        break;
        
        case 'E':
        switch (order)
        {
        case 1: printf("Robot has turned to south\n"); break;
        case 2: printf("Robot has turned to north\n"); break;
        case 3: printf("Robot has turned to west\n"); break;
        case 4: printf("Robot has remained at east\n"); break;
        default: break;
        }
        break;

        case 'W':
        switch (order)
        {
        case 1: printf("Robot has turned to north\n"); break;
        case 2: printf("Robot has turned to south\n"); break;
        case 3: printf("Robot has turned to east\n"); break;
        case 4: printf("Robot has remained at west\n"); break;
        default: break;
        }
        break;
    }
    return 0;
}*/
// int main()
// {
//     cls
//     int p,c;
//     printf("Enter a pin: "); scanf("%d",&p);
//     for(int i = 0; i <= 9; i++) {
//         for(int j=0; j<=9; j++) {
//             for(int k = 0; k <= 9; ++k) {
//                 for(int l=0; l<=9; ++l) {
//                     ++c;
//                     if(i == p/1000 && j == (p/100)%10 && k == (p/10)%10 && l == p%10)
//                         printf("The pin has been found in %d takes\n",c);
//                 }
//             }
//         }
//     }
//     return 0;
// }

/*int main()
{
    cls
    int n;
    printf("Enter a number: "); scanf("%d",&n);
    for(int i = n/2+1; i <= n; i++) {
        for(int j=1; j<=n; ++j) {
            if(i + j == n + 1 || i == j) 
                printf("* ");
            else
                printf("  ");        
        }
        printf("\n");
    }
    for(int i=1; i<=n; ++i) {
        for(int j = 1; j <= n; j++) {
            if(i==1 || j==1 || i==n || j==n) 
                printf("* ");
            else if(i==j || i+j == n+1)
                printf("* ");    
            else
                printf("  ");    
        }
        printf("\n");
    }
    return 0;
}

int main()
{
    cls
    int pen = 50,pencil = 10,rubber = 1;
    for(int i = 1; i <= 8; i++) {
        for(int j = 1; j <= 48; ++j) {
            for(int k=1; k<=98; ++k) {
                if(i+j+k == 100 && pen*i + pencil*j + rubber*k ==  500) {
                    printf("Pens: %d\nPencils: %d\nRubbers: %d\n",i,j,k);
                    return 0;
                }
            }
        }
    }
}
int main()
{
    cls
    int a,b,c;
    printf("Enter 2 numbers: "); scanf("%d%d",&a,&b);
    while(a <= b) {
        c = 0;
        for(int i=1; i<=a; ++i) {
            if(a % i == 0) {
                c++;
            }
        }
        if(c <= 2 && (a/1 && a/a)) {
            printf("%d ",a);
        }
        ++a;
    }    
    return 0;
}
int main()
{
    cls
    int n, num=1, sum;
    printf("Enter a number: "); scanf("%i",&n);
    do {
        sum=0;
        for(int i=1; i<num; ++i) {
            if(num % i == 0) {
                sum += i;
            }
        }
        if(num == sum) {
            printf("%d ",num);
        }
        num++;
    } while(num <= n);
    return 0;
}
int main()
{
    cls
    for(int i=1; i<10; i++) {
        for(int j = 1; j <= 10; ++j) {
            printf("%dx%d=%i\n",i,j,i*j);
        }
    }
    return 0;
}*/
