import platform
import psutil
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[39m'
    BLINK = '\x1b[5m'

def greet():
  art = """
    _             _        __      _       _     
   / \   _ __ ___| |__    / _| ___| |_ ___| |__  
  / _ \ | '__/ __| '_ \  | |_ / _ \ __/ __| '_ \ 
 / ___ \| | | (__| | | | |  _|  __/ || (__| | | |
/_/   \_\_|  \___|_| |_| |_|  \___|\__\___|_| |_|
"""

  print(f"{bcolors.OKCYAN}{art}")

def sys_info():
    try:
        info = platform.freedesktop_os_release()
        return info
    except OSError:
        print("Error getting sys.info()")

def sys_platform():
    try:
        info = platform.uname()
        return info
    except OSError:
        print("Error getting sys.info()")

def display_info(sys_dict,sys_platform,sys_usage):
    print(f"{bcolors.HEADER}       System Details  ")
    print(f"{bcolors.OKCYAN}Distro: {bcolors.RESET}{sys_dict.get('NAME')}")
    print(f"{bcolors.OKCYAN}Site-URL: {bcolors.RESET}{sys_dict.get('HOME_URL')}")
    print(f"{bcolors.OKCYAN}Host: {bcolors.RESET}{sys_platform.node.capitalize()} {sys_platform.system} {sys_platform.machine} Release - {sys_platform.release}")
    load, mem, disk = sys_usage
    print(f"{bcolors.OKCYAN}Cpu load: {bcolors.RESET}{load[0]:.2f}   {load[1]:.2f}   {load[2]:.2f}")
    print(f"{bcolors.OKCYAN}Memory:  {bcolors.RESET}Total={mem.total}  Used={mem.total}")
    print(f"{bcolors.OKCYAN}Disk:  {bcolors.RESET}Total={disk.total}  Free={disk.free}")


def sys_usage():
    load = psutil.getloadavg()
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return load,mem,disk

def init():
    greet()
    display_info(sys_info(),sys_platform(),sys_usage())

init()
