#include <stdio.h>
int main()
{
    int num = 0;
    int i = 0;
    int result = 1;
    printf("请输入一个正整数：");
    scanf("%d", &num);
    // 5
    for (i = 1; i <= num; i++)
    {
        result = result * i;
    }
    printf("%d的阶乘是：%d\n", num, result);
    return 0;
}