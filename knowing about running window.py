import psutil
import os

# # gives all users in current operating system
# print( psutil.users() )

# # gives id of all running tasks
# print(psutil.pids())

# # gives pids, task name, username in which it is running
# for proc in psutil.process_iter(['pid', 'name', 'username']):
#     print(proc.info)

# Iterate over all running process
# for proc in psutil.process_iter():
#     try:
#         # Get process name & pid from process object.
#         processName = proc.name()
#         processID = proc.pid
#         print(processName , ' ::: ', processID)
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass


# def on_terminate(proc):
#     print("process {} terminated with exit code {}".format(proc, proc.returncode))

# procs = psutil.Process()
# for p in procs:
#     p.terminate()
# gone, alive = psutil.wait_procs(procs, timeout=3, callback=on_terminate)
# for p in alive:
#     p.kill()


p = psutil.Process(37146)
print(p.name())

print(p.connections())
