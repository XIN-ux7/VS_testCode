#include <stdio.h>
#include <windows.h>

//  定义回调函数类型（C 端）
typedef void (*callback_with_state)(int, void *);

// C函数，调用回调函数，并传递附加状态数据（Python对象）
__declspec(dllexport) void call_python_callback_with_state(callback_with_state cb, void *obj)
{
    SetConsoleOutputCP(65001); // 设置控制台输出为UTF-8
    printf("C层调用回调函数:\n");
    cb(42, obj); // 传递参数给回调函数，并附带Python对象的引用
}
