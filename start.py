from datafiles.data import *
import math
import random
import time
import subprocess
import platform

# Pogram Menu Executer (Execute this Script in Python 3)

def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)

def info():
    clear()
    time.sleep(0.01)
    print(UCyan + 'What is YuCode Physics Calculator?' + Color_Off)
    print('This project contains some physics calculators like inclined-plane or gravitation. In them, some input (like a mass) is introduced and some output (weight, friction force, orbital velocity...) is expected.' + Color_Off)
    print(UCyan + 'Data variables' + Color_Off)
    print('Some data like Earth\'s mass or the radius of Mass\' orbit is stored in this program. You can use them by typing the exact variable name, instead of writting the decimal value. Here are the available variables so far:')
    print('- average_person_mass')
    print('- earth_gravity')
    print('- earth_mass')
    print('- earth_moon_distance')
    print('- earth_radius')
    print('- earth_sun_distance')
    print('- G (gravitational constant)')
    print('- jupiter_mass')
    print('- mars_mass')
    print('- mars_sun_distance')
    print('- mercury_mass')
    print('- mercury_sun_distance')
    print('- moon_mass')
    print('- neptune_mass')
    print('- saturn_mass')
    print('- sun_mass')
    print('- uranus_mass')
    print('- venus_mass')
    print('- venus_sun_distance')
    input(Green + "Press any key to continue..." + Color_Off)
    clear()
    time.sleep(0.01)
    program_start()


def input_loop():
    ProgramRun = input()

    if ProgramRun in ['E', 'e', 'EXIT', 'exit']:
        print(Red + 'Leaving program' + Color_Off)

    elif ProgramRun in ['D', 'd', 'DATA', 'data']:
        from datafiles import datachecker
    elif ProgramRun == str(0):
        info()

    elif ProgramRun == str(1):
        from programs import inclinedplane

    elif ProgramRun == str(2):
        from programs import gravitation

    else:
        print(Red + 'ERROR: Unexpected input! Please try again:' + Color_Off)
        input_loop()


def program_start():
    print(' ')
    print(Yellow + 'Which program would you like to start? You should read the INFO before starting the program for the first time.')
    print(' ' + Color_Off)
    print(Red + '[E] EXIT' + Color_Off)
    print(Green + '[D] Data checker' + Color_Off)
    print(Green + '[0] INFO' + Color_Off)
    print(Yellow + '[1] Inclined plane' + Color_Off)
    print(Yellow + '[2] Gravitation' + Color_Off)
    print(' ')
    input_loop()

# time.sleep(1)
clear()
time.sleep(0.01)
print(Yellow + 'WELCOME TO YUCODE PHYSICS CALCULATOR!')
time.sleep(1)

program_start()
