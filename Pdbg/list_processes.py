from winappdbg.system import System

# 获取系统中的所有进程
system = System()
system.scan()

# 打印所有进程的 PID 和可用方法
# 打印所有进程的 PID 和名称
for process in system:
    print(f"PID: {process.get_pid()} - Name: {process.get_filename()}")