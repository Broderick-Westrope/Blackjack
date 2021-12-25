import os
import subprocess


def clearCLI():
    if os.name == 'nt':
        os.system('CLS')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print("** ERROR: (main.py) Unable to clear screen. **")


def removeLine():
    if os.name == 'nt':
        print("\033[A                                                                                                                                                                                              \033[A\n")
    elif os.name == 'posix':
        tput = subprocess.Popen(['tput', 'cols'], stdout=subprocess.PIPE)
        cols = int(tput.communicate()[0].strip())
        print("\033[A{}\033[A".format(' '*cols) + "\n")
    else:
        print("** ERROR: (main.py) Unable to clear screen. **")
    
    # print()
