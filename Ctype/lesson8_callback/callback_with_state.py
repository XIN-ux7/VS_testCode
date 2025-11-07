from ctypes import CDLL,c_int,CFUNCTYPE,c_void_p

#定义回调函数类型
CALLBACK_TYPE = CFUNCTYPE(None,c_int,c_void_p)

#加载 DLL
dll = CDLL("./callback_with_state.dll")

# 定义一个带有状态的Python类
class Person:
    def __init__(self,name):
        self.name = name
        
    def callback(self,n,obj):
        print(f"Python 回调函数被调用，接收到参数：{n},{self.name}")
        
# 创建 Python类实例
person = Person("Alice")
# 将类的实例方法作为回调函数传递给c
callback_func = CALLBACK_TYPE(person.callback)

# 调用C函数并传递回调函数及类实例
dll.call_python_callback_with_state(callback_func,c_void_p(id(person)))