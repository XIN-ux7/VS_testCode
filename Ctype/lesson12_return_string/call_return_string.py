from ctypes import CDLL,c_char_p

# 加载DLL
dll = CDLL("./return_string.dll")

# 声明返回类型
dll.get_greeting.restype = c_char_p
dll.free_string.argtypes = [c_char_p]
dll.free_string.restype = None

# 调用C函数
s = dll.get_greeting()
print("Python 接收到字符串:", s.decode('utf-8'))

# 释放C 端内存
dll.free_string(s)