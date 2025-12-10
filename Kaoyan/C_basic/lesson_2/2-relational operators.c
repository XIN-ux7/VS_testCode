#include <stdio.h>
int main()
{
    int a;
    while (scanf("%d", &a))
    {
        if (3 < a < 10)
        {
            printf("a is between 3 and 10\n");
        }
        else
        {
            printf("a is not between 3 and 10\n");
        }
    }
}