#include <stdio.h>
int main()
{
    int currency = 100;
    int num = 40;
    int count = 0;
    int i = 10, j = 5, k = 2, l = 1;
    for (i = 1; i <= 10; i++)
    {
        for (j = 1; j <= 20; j++)
        {
            for (k = 1; k <= 50; k++)
            {
                for (l = 1; l <= 100; l++)
                {
                    if ((i * 10 + j * 5 + k * 2 + l * 1) == currency && (i + j + k + l) == num)
                    {
                        count++;
                        printf("10元的有%d张，5元的有%d张，2元的有%d张，1元的有%d张\n", i, j, k, l);
                    }
                }
            }
        }
    }
    printf("共有%d种组合方式\n", count);
}