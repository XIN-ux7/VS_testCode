from ctypes import CDLL,Structure,c_int,c_double

# 定义 Python 侧的结构
class Person(Structure):
    _fields_ = [
        ("age",c_int),
        ("height",c_double)
    ]
    
# 加载DLL
dll = CDLL("./person.dll")

# 声明函数参数类型
dll.show_person.argtypes = [Person]
dll.show_person.restype = None

# 创建结构体变量并调用
p = Person(25,178.5)
dll.show_person(p)