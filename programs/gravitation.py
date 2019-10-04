from datafiles.data import *
import math
import random
import time
import subprocess
import platform

# Gravitation Calculator Script (Execute This Script in Python 3)


def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)


# INITIAL SCRIPT #
def initial():
    clear()
    print(Cyan + ' ')
    print('* * * * * * * * * * * * * * * * * * * * * * * *')
    print('* G R A V I T A T I O N   C A L C U L A T O R *')
    print('* * * * * * * * * * * * * * * * * * * * * * * *')
    time.sleep(1)
    print(' ')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print('                 *            *       *        ')
    time.sleep(0.1)
    print('           *         *    *       *            ')
    time.sleep(0.1)
    print('       *          * *                   *      ')
    time.sleep(0.1)
    print('             *         *     *       *      *  ')
    time.sleep(0.1)
    print('           *         *   *              *      ')
    time.sleep(0.1)
    print('                                               ')
    time.sleep(0.1)
    print('                                               ')
    time.sleep(0.1)
    print('                     ****                      ')
    time.sleep(0.1)
    print('                   ********                    ')
    time.sleep(0.1)
    print('                  **********                   ')
    time.sleep(0.1)
    print('      (________  ************  _________)      ')
    time.sleep(0.1)
    print('      (________  ************  _________)      ')
    time.sleep(0.1)
    print('                  **********                   ')
    time.sleep(0.1)
    print('                   ********                    ')
    time.sleep(0.1)
    print('                     ****                      ')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print(' ' + Color_Off)
    time.sleep(1)


def home():
    print(Cyan + 'Press "S" to start calculator, "H" for help or information, "M" to return to the main menu or "E" to exit the program. Then press enter.' + Color_Off)
    home.varinput = input()

    if home.varinput in ['S', 's', 'START', 'start']:

        # INPUT SCRIPT #
        print(Cyan + 'Insert the bigger mass (kg): ' + Color_Off)
        M = eval(input())
        print(Cyan + 'Insert the smaller mass (kg): ' + Color_Off)
        m = eval(input())
        print(Cyan + 'Insert the distance of the objects or the radius of the orbit (m): ' + Color_Off)
        R = eval(input())

        # CALCULATIONS AND FORMULES #
        g = G * M / (R**2)
        a = G * m / (R**2)
        P = m * g
        P2 = M * a * (-1)
        v = math.sqrt(G * M / R)
        T = (2 * math.pi * R) / v
        ω = v / R     # or (2 * math.pi) / T

        # DISPLAY SCRIPT #
        print(' ')
        print(Cyan + 'INPUT' + Color_Off)
        print('M = ' + str(M) + ' kg')
        print('m = ' + str(m) + ' kg')
        print('R = ' + str(R) + ' m')
        print(' ')
        print(Cyan + 'OUTPUT' + Color_Off)
        print('P (M on m) = ' + str(P) + ' N')
        print('P (m on M) = ' + str(P2) + ' N')
        print('g = ' + str(g) + ' m/s2')
        print('a = ' + str(a) + ' m/s2')
        print('T = ' + str(T) + ' s')
        print('v = ' + str(v) + ' m/s')
        print('ω = ' + str(ω) + ' rad/s')
        time.sleep(3)
        print(' ')
        print(' ')
        home()

    elif home.varinput in ['H', 'h', 'HELP', 'help', 'INFO', 'info', 'I', 'i']:
        from start import info

    elif home.varinput in ['E', 'e', 'EXIT', 'exit']:
        print('Leaving program')

    elif home.varinput in ['M', 'm', 'MENU', 'menu']:
        import start
        # from start import *

    else:
        print(Red + 'Error, type a valid input' + Color_Off)
        home()


initial()
home()
