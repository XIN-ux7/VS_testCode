#include <stdio.h>

// 求n的阶乘
int f(int n)
{
    if (1 == n)
    {
        return 1;
    }
    return n * f(n - 1);
}

// 走楼梯
int step(int n)
{
    if (1 == n)
    {
        return 1;
    }
    if (2 == n)
    {
        return 2;
    }
    return step(n - 1) + step(n - 2);
}

int main()
{
    int n;
    int ret;
    scanf("%d", &n);
    ret = f(n);
    printf("%d\n", ret);
    scanf("%d", &n);
    ret = step(n);
    printf("%d\n", ret);
    return 0;
}