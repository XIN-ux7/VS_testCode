#include <stdio.h>
#include <windows.h>

struct Person
{
    int age;
    double height;
};

// 函数接收结构体指针，并修改成员
__declspec(dllexport) void update_person(struct Person *p)
{
    SetConsoleOutputCP(65001);
    p->age += 5;
    p->height += 10.0;
    printf("C层修改后:Age = %d,Height = %.2f\n", p->age, p->height);
}