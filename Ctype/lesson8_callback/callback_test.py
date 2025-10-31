from ctypes import CDLL,c_int,CFUNCTYPE
# 实现C->Python的回调
# 定义 Python 回调函数的类型
CALLBACK_TYPE = CFUNCTYPE(None,c_int)

# 加载 DLL
dll = CDLL("./callback_test.dll")

# 定义 Python回调函数
def python_callback(n):
    print("Python 回调函数接收到:", n)
    
# 将 Python 回调函数转换为c可调用的函数指针
callback_func = CALLBACK_TYPE(python_callback)

# 调用C函数并传递回调函数
dll.call_python_callback(callback_func)
