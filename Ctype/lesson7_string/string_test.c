#include <stdio.h>
#include <string.h>
#include <windows.h>

// 修改字符串内容
__declspec(dllexport) void modify_string(char *s)
{
    SetConsoleOutputCP(65001); // utf-8输出
    strcat(s, "World!");       // 在字符串后追加内容
    printf("C层输出:%s\n", s);
}
