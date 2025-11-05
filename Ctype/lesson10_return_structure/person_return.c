#include <stdio.h>

struct Person
{
    int age;
    double height;
};

// 导出函数：返回一个结构体
__declspec(dllexport) struct Person create_person(int age, double height)
{
    struct Person p;
    p.age = age;
    p.height = height;
    printf("c层创建Person:Age = %d,Height=%.2f\n", p.age, p.height);
    return p;
}