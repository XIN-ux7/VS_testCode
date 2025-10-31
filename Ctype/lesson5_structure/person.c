#include <stdio.h>
#include <windows.h>
// 定义C结构体
struct Person
{
    int age;
    double height;
};

// 导出函数（Windows下用__declspec(dllexport)）
__declspec(dllexport) void show_person(struct Person p)
{
    SetConsoleOutputCP(65001); // 设置为 UTF-8
    printf("C层输出:Age = %d,Height = %.2f\n", p.age, p.height);
}