// pointer_demo.c
#include <stdio.h>

// 这个函数接受一个int指针，把它的值改成100
void change_value(int *x)
{

    *x = 100;
}

// gcc -shared -o pointer.dll pointer_demo.c
