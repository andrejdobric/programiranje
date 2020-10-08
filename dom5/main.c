#include <stdio.h>
#include <stdlib.h>

int main()
{
    int niz[100];
    int n;
    int b;

    printf("Unesite velicinu niza:");
    scanf("%d",&n);

    printf("\nUnesite niz:");
    for(int i=0;i<n;i++){
        scanf("%d",(niz+i));
    }
    for(int i=0; i<n; i++){
        if((*(niz+i)%3)==0){
            printf("\n%d",*(niz+i));
        }
    }
}
