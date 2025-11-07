from winappdbg.system import System

# Create a system snapshot
system = System()

# Now we can enumerate the running processes
for process in system:
    print(
        "%d:\t%s\t%s\t%s"
        %(
            process.get_pid(),
            process.get_arch(),
            process.get_bits(),
            process.get_filename(),
        )
    )
    