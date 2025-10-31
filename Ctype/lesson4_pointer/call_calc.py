from ctypes import *

# 加载 DLL
dll = CDLL("./calc.dll")

# 设置函数参数类型
dll.add_sub.argtypes = [c_int,c_int,POINTER(c_int),POINTER(c_int)]
dll.add_sub.restype = None

# 准备输出函数
sum_result = c_int()
diff_result = c_int()

# 调用
dll.add_sub(20,8,byref(sum_result),byref(diff_result))

# 查看结果
print("加法结果 sum = ", sum_result.value)
print("减法结果 diff =",diff_result.value)