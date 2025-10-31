from ctypes import cdll, c_int,byref,POINTER

# 1. 加载DLL
dll = cdll.LoadLibrary("./pointer_demo.dll")

# 2. 声明函数参数类型（重要）
dll.change_value.argtypes = [POINTER(c_int)] # 接收int指针
dll.change_value.restype = None # void 返回类型

# 3. 创建一个C 整型变量
num = c_int(10)
print("调用前 num =",num.value)

# 4. 传指针给C 函数
dll.change_value(byref(num))
print("调用后 num =", num.value)
