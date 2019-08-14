from data import *
import math
import random
import time
import subprocess
import platform
# import importlib


def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
    # return

clear()


def home():
    time.sleep(0.01)
    print(Green + 'Type a variable to check its value. Type "M" to return to the main menu:' + Color_Off)
    # return

home()


def input_loop():
    DataCheckerInput = input()
    if DataCheckerInput in ['G', 'g']:
        DataCheckerInputFinal = DataCheckerInput.upper()
    else:
        DataCheckerInputFinal = DataCheckerInput.lower()
    if DataCheckerInputFinal in ['M', 'm', 'MENU', 'menu']:
        import physics
        # return
    try:
        print(Cyan + str(eval(DataCheckerInputFinal)) + Color_Off)
        input_loop()
    except NameError:
        print(Red + 'ERROR: Variable not found' + Color_Off)
        input_loop()
    # return

input_loop()
