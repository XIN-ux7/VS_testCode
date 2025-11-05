from ctypes import CDLL,c_char_p,create_string_buffer

# 加载DLL
dll = CDLL('./modify_string.dll')

# 声明参数类型
dll.append_world.argtypes = [c_char_p]
dll.append_world.restype = None

# 创建可修改字符串缓冲区
s = create_string_buffer(b"Hello, ", 50)  # 预留足够空间

# 调用C函数
dll.append_world(s)

#Python 端读取修改后的字符串
print("Python 读取字符串：",s.value.decode('utf-8'))