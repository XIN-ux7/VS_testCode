from ctypes import CDLL,c_char_p,create_string_buffer

# 加载 DLL
dll = CDLL("./string_test.dll")
dll.modify_string.argtypes = [c_char_p]
dll.modify_string.restype = None

# 创建可修改的字符串缓冲区
s = create_string_buffer(b"Hello",50) # 50字节空间
dll.modify_string(s)

# Python 端查看修改
print("Python 输出：",s.value.decode("utf-8"))