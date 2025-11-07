from winappdbg.process import Process
from winappdbg.textio import HexDump

def print_threads_and_modules(pid):
    """
    打印指定 PID 的线程和模块信息。
    注意：附加到某些系统/受保护进程可能需要管理员权限。
    """
    try:
        process = Process(pid)
    except Exception as e:
        print(f"无法创建 Process({pid})：{e}")
        return

    try:
        bits = process.get_bits()          # 从 Process 获取位宽（32/64）
        print(f"Process {process.get_pid()} ({bits}-bit)")

        # 列出线程
        print("Threads:")
        for thread in process.iter_threads():
            try:
                print(f"\tTID {thread.get_tid()}")
            except Exception as e:
                print(f"\t[线程枚举错误] {e}")

        # 列出模块
        print("Modules:")
        for module in process.iter_modules():
            try:
                base = module.get_base()
                size = module.get_size() if hasattr(module, "get_size") else "?"
                filename = module.get_filename() or "<unknown>"
                # 使用 HexDump.address 格式化地址，传入进程位宽
                addr = HexDump.address(base, bits)
                print(f"\t{addr}\t{size}\t{filename}")
            except Exception as e:
                print(f"\t[模块枚举错误] {e}")

    finally:
        # Process 对象没有显式 close 方法，但如果后来需要清理可在此处处理
        pass

# 示例：把要查看的 PID 替换为真实 PID，例如 1234
print_threads_and_modules(11152)
