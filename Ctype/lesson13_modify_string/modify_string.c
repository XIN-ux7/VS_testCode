#include <stdio.h>
#include <string.h>

// 导出函数：修改字符串
__declspec(dllexport) void append_world(char *s)
{
    strcat(s, "World!");
    printf("C层修改后的字符串:%s\n", s);
}