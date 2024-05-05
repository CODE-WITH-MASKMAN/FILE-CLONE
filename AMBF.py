import os
import platform
import sys
import time
import ctypes
os.system('xdg-open https://example.com') 

try:
    import requests
except ImportError:
    os.system("pip uninstall requests -y; pip install requests")
    import requests

print('CHECKING FOR UPDATE...')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]

if bit == '64bit':
    print('WELCOME 64BIT USER')
    crack_lib = ctypes.CDLL('./Data/script/crack.so')

elif bit == '32bit':
    print('WELCOME 32BIT USER')
    crack_lib = ctypes.CDLL('./Data/script/crack.so')

