from ctypes import cdll,c_char_p,c_int

libc = cdll.msvcrt if hasattr(cdll,"msvcrt") else cdll.LoadLibrary("libc.so.6")

libc.strncmp.argtypes = [c_char_p,c_char_p,c_int]
libc.strncmp.restype = c_int

# 调用 strncmp 比较字符串
# 第三个参数 n 决定最多比较多少个字符
result = libc.strncmp(b"hello",b"hello",5)
print("比较结果1 = ",result)

result = libc.strncmp(b"hello",b"world",5)
print("比较结果2 = ",result)