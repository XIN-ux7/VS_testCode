from ctypes import CDLL,Structure,c_int,c_double,POINTER,byref

# 定义 Pthon 侧结构体
class Person(Structure):
    _fields_=[
        ("age",c_int),
        ("height",c_double)
    ]
    
# 加载DLL
dll = CDLL("./update_person.dll")
dll.update_person.argtypes = [POINTER(Person)]
dll.update_person.restype = None

# 创捷结构体变量
p = Person(25,178.5)
print("调用前Python",p.age,p.height)

# 调用C函数修改结构体
dll.update_person(byref(p))
print("调用后 python:",p.age,p.height)