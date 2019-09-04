import math
import random
import time
import platform

average_person_mass = 70
earth_gravity = 9.80665
earth_mass = 5.97e+24
earth_moon_distance = 3.844e+8
earth_radius = 6371000
earth_sun_distance = 1.496e+11
G = 6.67e-11
jupiter_mass = 1.898e+27
mars_mass = 6.39e+23
mars_sun_distance = 227.9e+6
mercury_mass = 3.285e+23
mercury_sun_distance = 57.91e+6
moon_mass = 7.34e+22
neptune_mass = 1.024e+26
saturn_mass = 5.683e+26
uranus_mass = 8.681e+25
venus_mass = 4.867e+24
venus_sun_distance = 108.2e+6

# INITIAL SCRIPT #
def initial():
    print('----G R A V I T A T I O N----')
    print('---- C A L C U L A T O R ---- ')
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
    time.sleep(1)


def home():
    print('Press "S" to start calculator or "E" to exit the program. Then press enter.')
    home.varinput = input()

    if home.varinput in ['S', 's', 'START', 'start']:

        # INPUT SCRIPT #
        print('Insert the bigger mass (kg): ')
        M = int(input())
        print('Insert the smaller mass (kg): ')
        m = int(input())
        print('Insert the distance of the objects or the radius of the orbit (m): ')
        R = int(input())

        # CALCULATIONS AND FORMULES #
        g = G * M / (R**2)
        a = G * m / (R**2)
        P = m * g
        P2 = M * a * (-1)
        v = math.sqrt(G * M / R)
        T = (2 * math.pi * R) / v
        w = v / R     # or (2 * math.pi) / T

        # DISPLAY SCRIPT #
        print(' ')
        print('INPUT')
        print('M = ' + str(M) + ' kg')
        print('m = ' + str(m) + ' kg')
        print('R = ' + str(R) + ' m')
        print(' ')
        print('OUTPUT')
        print('P (M on m) = ' + str(P) + ' N')
        print('P (m on M) = ' + str(P2) + ' N')
        print('g = ' + str(g) + ' m/s2')
        print('a = ' + str(a) + ' m/s2')
        print('T = ' + str(T) + ' s')
        print('v = ' + str(v) + ' m/s')
        print('w = ' + str(w) + ' rad/s')
        time.sleep(3)
        print(' ')
        home()

    elif home.varinput in ['H', 'h', 'HELP', 'help', 'INFO', 'info', 'I', 'i']:
        from physics import info

    elif home.varinput in ['E', 'e', 'EXIT', 'exit']:
        print('Leaving program')

    else:
        print('Error, type a valid input')
        home()

    return

initial()
home()
