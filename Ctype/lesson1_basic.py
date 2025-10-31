from ctypes import cdll

# 加载系统C运行时库

libc = cdll.msvcrt if hasattr(cdll,"msvcrt") else cdll.LoadLibrary("libc.so.6")

# 调用C的printf函数
libc.printf(b"Hello from C! Number = %d\n",123)