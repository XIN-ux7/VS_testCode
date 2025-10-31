from ctypes import CDLL,Structure,c_int,c_double,POINTER,byref

# 定义结构体
class Person(Structure):
    _fields_ = [
        ("age",c_int),
        ("height",c_double)
    ]
    
# 加载 DLL
dll = CDLL("./person_array.dll")
dll.update_person_array.argtypes=[POINTER(Person),c_int]
dll.update_person_array.restype = None

# 创建结构体数组
PersonArray= Person * 3
arr = PersonArray(Person(20,170.0),Person(25,175.5),Person(30,180.2))

# 调用 C 函数
dll.update_person_array(arr,3)

# Python 端查看修改结果
for i,p in enumerate(arr):
    print(f"Python 第{i}个: Age {p.age},Height = {p.height}")
