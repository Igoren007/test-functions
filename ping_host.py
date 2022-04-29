import platform
import subprocess

def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', parameter, '1', host]
    resp = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if resp == 0:
        print('ping OK')
    else:
        print('ping BAD')
    return resp
        
print(myping("www.google.com"))
print(myping("172.16.1.254"))
