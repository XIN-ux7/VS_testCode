#include <stdio.h>
#include <stdlib.h>

void change(int *a)
{
    *a = *a / 2;
}

int main()
{
    printf("请输入一个整数：");
    int i = 0;
    scanf("%d", &i);
    change(&i);
    printf("改变后的值是：%d\n", i);
    return 0;
}