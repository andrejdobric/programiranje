#include <stdio.h>
#include <stdlib.h>

int jednaki(char *s1, char *s2)
{
    int i = 0, b = 0;
    while(*(s1 + i) != '\0' && *(s2 + i) != '\0'){
        if(*(s1 + i) != *(s2 + i)){
            b = 1;
            break;
        }
        i++;
    }
    if(b == 0 && *(s1 + i) == '\0' && *(s2 + i) == '\0')
        return 1;
    else
        return 0;
}

int main()
{
    char s1[20];
    char s2[20];
    printf("Unesite prvi string:");
    scanf("%s",s1);
    printf("\nUnesite drugi string:");
    scanf("%s",s2);

    int jdk=jednaki(s1,s2);

    if(jdk == 1){
        printf("\nJednaki su.");
    } else printf("\nNisu jednaki.");


    return 0;
}
