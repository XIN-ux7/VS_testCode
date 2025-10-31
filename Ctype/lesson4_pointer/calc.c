#include <stdio.h>

// 同时返回加法和减法的结果
void add_sub(int a, int b, int *sum, int *diff)
{
    *sum = a + b;
    *diff = a - b;
}