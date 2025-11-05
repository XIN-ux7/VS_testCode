#include <stdio.h>
#include <stdlib.h>

// 定义结构体
struct Person
{
    int age;
    double height;
};

// 导出函数（返回指针）
__declspec(dllexport) struct Person *create_person(int age, double height)
{
    struct Person *p = (struct Person *)malloc(sizeof(struct Person));
    p->age = age;
    p->height = height;
    return p; // 返回结构体指针
}

// 释放内存
__declspec(dllexport) void free_person(struct Person *p)
{
    free(p);
}