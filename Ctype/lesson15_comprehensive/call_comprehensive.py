from ctypes import CDLL,Structure,c_char,c_int,CFUNCTYPE,POINTER

# 定义结构体
class Person(Structure):
    _fields_=[
        ("name",c_char * 50),
        ("age",c_int)
    ]
    
# 定义回调函数类型
CALLBACK = CFUNCTYPE(None, POINTER(Person))

# Python回调函数
def python_callback(p):
    print("Python 回调收到Person:",p.contents.name.decode("utf-8"),p.contents.age)
    
# 加载DLL
dll = CDLL("./comprehensive.dll")

# 设置参数类型
dll.process_person.argtypes = [CALLBACK]
dll.process_person.restype = None

# 调用DLL，并传递回调
dll.process_person(CALLBACK(python_callback))
