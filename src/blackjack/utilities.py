import os

def clearCLI():
    if os.name == 'nt':
        os.system('CLS')
    elif os.name == 'posix':
        os.system('clear')
        pass
    else:
        print("**ERROR: (main.py) Unable to clear screen.**")
