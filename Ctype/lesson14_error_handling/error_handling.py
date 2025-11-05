from ctypes import CDLL,c_int,byref,POINTER

#加载DLL
dll = CDLL("./error_handling.dll")

# 声明函数参数和返回类型
dll.divide.argtypes = [c_int,c_int,POINTER(c_int)]
dll.divide.restype = c_int

# 调用函数并处理错误
def safe_divide(a,b):
    result = c_int()
    ret = dll.divide(a,b,byref(result))
    if ret != 0:
        raise ValueError("C函数返回错误:除数不能为0")
    return result.value

# 测试
print("10 / 2 =", safe_divide(10,2))
try:
    print("10 / 0 = ",safe_divide(10,0))
except ValueError as e:
    print("捕获到异常:", e)