from data import *
import math
import random
import time
import subprocess
import platform

def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)

clear()

def home():
    time.sleep(0.01)
    print(Green + 'Type a variable to check its value. Type "M" to return to the main menu' + Color_Off)

home()

def input_loop():
    DataCheckerInput = input()
    if DataCheckerInput in ['M', 'm', 'MENU', 'menu']:
        import physics
        return
    try:
        print(Cyan + str(eval(DataCheckerInput)) + Color_Off)
        if NameError:
            input_loop()
        else:
            home()
    except NameError:
        print(Red + 'ERROR: Variable not found' + Color_Off)
        input_loop()

input_loop()
