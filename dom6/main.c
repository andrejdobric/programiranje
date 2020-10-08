#include <stdio.h>
#include <stdlib.h>

void upis(int n, int m, int niz[n][m])
{
    int i, j;

    for (i=0; i<n; i++)
    {
        for (j=0; j<m; j++)
        {
            printf ("Red %d kolona %d: ", i+1, j+1);
            scanf  ("%d", (*(niz + i) + j));
        }
    }
}

void sabiranje(int n, int m,int niz1[n][m],int niz2[n][m])
{
    int i, j;

    for( i=0; i<n; i++)
    {
        for(j=0; j<m; j++)
        {
            *(*(niz1 +i) + j)+=*(*(niz2 +i) + j);
        }
    }
}

void ispis(int n, int m, int niz[n][m])
{
    int i, j;

    for(i=0; i<n; i++)
    {
        for(j=0; j<m; j++)
        {
            printf("%d ", *(*(niz + i) + j));
        }
        printf("\n");
    }
}



int main()
{
    int niz1[20][20], niz2[20][20], n, m;
    scanf("%d", &n);
    scanf("%d", &m);

    upis(n,m,niz1);
    upis(n,m,niz2);

    sabiranje(n,m,niz1,niz2);
    ispis(n,m,niz1);


}
