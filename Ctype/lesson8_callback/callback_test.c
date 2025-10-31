#include <stdio.h>
#include <windows.h>

// 定义一个回调函数类型（c端）
typedef void (*callback)(int);

// C 函数，调用回调函数
__declspec(dllexport) void call_python_callback(callback cb)
{
    SetConsoleOutputCP(65001); // 设置控制台输出为 UTF-8 编码
    printf("C层调用回调函数:\n");
    cb(42); // 调用回调函数，传递一个整数参数
}
