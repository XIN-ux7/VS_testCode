from ctypes import cdll,c_char_p,c_int

# 加载 C标准库
libc = cdll.msvcrt if hasattr(cdll,"msvcrt") else cdll.LoadLibary("libc.so.6")

# 声明函数参数类型和返回类型
libc.strlen.argtypes = [c_char_p] # 参数是char*
libc.strlen.restype = c_int # 返回 int

# 调用 strlen
length = libc.strlen(b"Hello ctypes")
print("字符串长度=",length)