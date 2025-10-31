from ctypes import *

# 创建 C 类型变量
a = c_int(10)
b = c_double(3.14)
c = c_char(b'Z')
d = c_bool(True)


print("a = ",a.value)
print("b = ",b.value)
print("c = ",c.value)
print("d = ",d.value)

# 修改值
a.value= 90
print("修改后 a=",a.value)

