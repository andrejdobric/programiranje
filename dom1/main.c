#include <stdio.h>
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

void trnsp(int n, int m, int niz[n][m], int niz1[m][n])
{
    int i, j;

    for(i=0; i<n; i++)
    {
        for(j=0; j<m; j++)
        {
            *(*(niz1 + i) + j) = *(*(niz + j) + i);
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

int main() {
    int niz[10][10], niz1[10][10], n, m;

    scanf("%d", &n);
    scanf("%d", &m);

    upis(n,m,niz);

    trnsp(n,m,niz,niz1);

    ispis(m,n,niz1);


    return 0;
}
