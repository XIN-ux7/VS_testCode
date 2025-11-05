from ctypes import CDLL,Structure,POINTER,c_int,c_double

# 定义与C 对应的结构体
class Person(Structure):
    _fields_ = [
        ("age",c_int),
        ("height",c_double)
    ]
    
# 加载DLL
dll = CDLL("./person_pointer.dll")

# 声明函数原型
dll.create_person.argtypes = [c_int,c_double]
dll.create_person.restype = POINTER(Person) # 返回结构体指针

dll.free_person.argtypes = [POINTER(Person)] 
dll.free_person.restype = None

# 调用C函数创建结构体
p = dll.create_person(30,180.5)
print("Python 侧读取 => age:",p.contents.age,",height:",p.contents.height)

# 调用释放函数
dll.free_person(p)
