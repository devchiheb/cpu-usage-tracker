import time
import psutil
import os


cpu = psutil.cpu_percent()
ram=psutil.virtual_memory().percent
def dispusage (cpu,ram,bars=50):
    cpu_percent=cpu/100
    cpu_bar="◼"*int(cpu_percent*bars)+'-'*(bars-int(cpu_percent*bars))
    mem_percent=ram/100

    mem_bar="◼"*int(mem_percent*bars)+'-'*(bars-int(mem_percent*bars))

    print(f"\r cpu usage |{cpu_bar}|{cpu:.2f}%   ",end="")
    print(f"ram usage |{mem_bar}|{ram:.2f}%   ",end="\r")


while True:
    try:    
        time.sleep(0.5)
        dispusage(cpu,ram,30)
    except:

        break


