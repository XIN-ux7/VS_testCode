#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 导出函数
__declspec(dllexport) char *get_greeting()
{
    char *s = (char *)malloc(50); // 动态分配内存
    strcpy(s, "Hello from c!");
    return s;
}

// 释放函数
__declspec(dllexport) void free_string(char *s)
{
    free(s);
}