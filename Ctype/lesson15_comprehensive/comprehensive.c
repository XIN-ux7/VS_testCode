#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 定义结构体
struct Person
{
    char name[50];
    int age;
};

// 回调函数类型
typedef void (*callback)(struct Person *);

// 导出函数：创建结构体并调用回调
__declspec(dllexport) void process_person(callback cb)
{
    struct Person *p = (struct Person *)malloc(sizeof(struct Person));
    strcpy(p->name, "Alice");
    p->age = 28;

    // C端输出
    printf("C:Person info->%s,%d\n", p->name, p->age);

    // 调用Python回调
    cb(p);

    // 释放内存
    free(p);
}