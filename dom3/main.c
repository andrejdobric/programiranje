#include <stdio.h>
#include <stdlib.h>

void func(char *s1, char c)
{
    int i=0;
    int b=0;
    while(*(s1+i)!='\0'){
        if(*(s1+i)==c) b++;
        i++;
    }
    printf("%d",b);
}

int main()
{
    char s1[20];
    char c;
    printf("Unesite string:");
    scanf("%s",s1);
    printf("\nUnesite karakter:");
    scanf(" %c",&c);

    func(s1,c);

    return 0;
}
