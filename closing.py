import psutil,os


p = psutil.Process(36729)
p.terminate()
p.wait()