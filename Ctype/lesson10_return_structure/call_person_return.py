from ctypes import CDLL,Structure,c_int,c_double

# 定义结构体
class Person(Structure):
    _fields_ = [
        ("age",c_int),
        ("height",c_double)
    ]
    
# 加载 DLL
dll = CDLL("./person_return.dll")
    
# 声明返回类型
dll.create_person.restype = Person
dll.create_person.argtypes = [c_int,c_double]

# 调用函数并接受结构体返回值
p = dll.create_person(30,182.3)

print("python接收到结构体:")
print(f"Age = {p.age},Height = {p.height}")