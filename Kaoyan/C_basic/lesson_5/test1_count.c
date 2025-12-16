#include <stdio.h>
int main()
{
    int a[6];
    int count = 0;
    printf("请输入5个整数：");
    int i = 0;
    for (i = 0; i < 5; i++)
    {
        scanf("%d", &a[i]);
        if (a[i] == 2)
        {
            count++;
        }
    }
    printf("数字2出现了%d次\n", count);
}