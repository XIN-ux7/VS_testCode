#include <stdio.h>
#include <windows.h>

struct Person
{
    int age;
    double height;
};

// 修改数组中每个元素
__declspec(dllexport) void update_person_array(struct Person *p_array, int count)
{
    SetConsoleOutputCP(65001);
    for (int i = 0; i < count; i++)
    {
        p_array[i].age += 1;
        p_array[i].height += 2.0;
        printf("C层第%d个: Age  = %d, Height = %.2f\n", i, p_array[i].age, p_array[i].height);
    }
}