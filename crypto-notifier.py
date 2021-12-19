import psutil
from urllib import request, parse

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.cmdline():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

if not checkIfProcessRunning('book_wait.py'):
    data = parse.urlencode({'key': 'YiGJdc', 'title': 'okex', 'msg': 'okex bot die', 'event': 'event'}).encode()
    req = request.Request("https://api.simplepush.io/send", data=data)
    request.urlopen(req)

if not checkIfProcessRunning('ftx-strategy.py'):
    data = parse.urlencode({'key': 'YiGJdc', 'title': 'ftx', 'msg': 'ftx bot die', 'event': 'event'}).encode()
    req = request.Request("https://api.simplepush.io/send", data=data)
    request.urlopen(req)
