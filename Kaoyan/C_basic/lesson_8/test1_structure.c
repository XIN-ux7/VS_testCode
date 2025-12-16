#include <stdio.h>

struct Student
{
    int num;
    char name[20];
    char gender;
};

int main()
{
    struct Student stu2;
    printf("请输入学号、姓名、性别（M/F）：");
    scanf("%d %s %c", &stu2.num, stu2.name, &stu2.gender);
    printf("学号：%d\n姓名：%s\n性别：%c\n", stu2.num, stu2.name, stu2.gender);
    return 0;
}