#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i = 0, j = 1;
    while (scanf("%d"), &i)
    {
        if (i % 4 == 0 && i % 100 != 0 || i % 400 == 0)
        {
            printf("i is leap year\n");
        }
        else
        {
            printf("i is not leap year\n");
        }
    }
    i = !!j;
    printf("i=%d\n", i);
    return 0;
}