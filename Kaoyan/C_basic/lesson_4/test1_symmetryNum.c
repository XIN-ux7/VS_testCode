#include <stdio.h>
int main()
{
    printf("请输入一个整形数：");
    int num1, num2;
    int count = 0;
    int tempt = 0;
    // 12321
    scanf("%d", &num1);
    num2 = num1;
    while (num1)
    {
        tempt = num1 % 10;
        // 1
        count = count * 10 + tempt;
        // 1232
        num1 = num1 / 10;
    }
    printf("该数的反转数为：%d\n", count);
    if (count == num2)
    {
        printf("该数是对称数\n");
    }
    else
    {
        printf("该数不是对称数\n");
    }
    return 0;
}