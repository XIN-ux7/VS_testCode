import sys
from winappdbg.system import System

# Instance a System object
system = System()

# Get the target application
# command_line = system.argv_to_cmdline(sys.argv[1:])
command_line = "notepad.exe" # calc.exe cmd.exe
# Start a new process
process = system.start_process(command_line) # see the docs for more options

# Show info on the new process
print("Started process %d (%d bits)" % (process.get_pid(),process.get_bits()))