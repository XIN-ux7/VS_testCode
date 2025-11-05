#include <stdio.h>

// 导出函数：返回错误码
__declspec(dllexport) int divide(int a, int b, int *result)
{
    if (b == 0)
    {
        return -1; // 错误码：除以零
    }
    *result = a / b;
    return 0; // 成功
}