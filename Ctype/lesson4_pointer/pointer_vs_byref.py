from ctypes import c_int,pointer,byref

# 准备一个整数
num = c_int(10)

# 创建指针的两种方式
p1 = byref(num) # 方式1：通过byref获取地址（轻量）
p2 = pointer(num) # 方式2：创建真正的指针对象（完整指针）

print("p1 = ",p1) # byref对象
print("p2 = ",p2) # LP_c_int 对象（真正的指针）
print("p2.contents =",p2.contents)# 指针指向的内容
print("p2.contents.value=",p2.contents.value)
