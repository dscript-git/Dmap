#!/usr/bin/env python3
import os
from Function import Choice
from Check import Root

root1 = Root()
print (root1.root_check())
function1 = Choice()

#colors
yellow = '\033[93m'
green = '\033[92m'
good = '\033[92m[+]\033[0m'
info = '\033[93m[!]\033[0m'

def menu():
    print (green," ===========> Dmap v1.0 by |dscript-git| <============")
    print ("")
    print (" [1] Scan a Single IP")
    print (" [2] Scan a Host")
    print (" [3] Scan a Range of Ip")
    print (" [4] Scan a Subnet")
    print (" [5] Scan a Single Port")
    print (" [6] Scan a Range of Ports")
    print (" [7] Scan Most Common Ports")
    print (" [8] Scan All 65,535 Ports")
    print (" [9] Scan using TCP Connect")
    print (" [10] Scan using TCP Syn Scan")
    print (" [11] Scan UDP Ports")
    print (" [12] Scan Common Ports - Ignore Discovery")
    print (" [13] Detect OS & Services")
    print (" [14] Standard Service Detection")
    print (" [15] More Agressive Service Detection")
    print (" [16] Banner Grabbing Detection")
    print (" [17] Heart Bleed Bug Detection")
    print (" [18] Find Online Info of IP Address")
    print (" [00] Exit")
    print ("")
    choice = input('\033[92m[+]\033[0m'" Enter Your Choice: "'\033[93m')

# Conditionals
    if choice == '00':
        try:
            print (info," Exiting ...")
            os.system('sleep 2')
            exit()
        except NameError:
            print (info," Wrong Input... Exiting...")
            os.system('sleep 2')
            exit()
        except KeyboardInterrupt:
            print (info," Keyboard Interrupt... Exiting...")
            os.system('sleep 2')
            exit()

    elif choice == '1':
        function1.choice1()

    elif choice == '2':
        function1.choice2()

    elif choice == '3':
        function1.choice3()

    elif choice == '4':
        function1.choice4()

    elif choice == '5':
        function1.choice5()

    elif choice == '6':
        function1.choice6()

    elif choice == '7':
        function1.choice7()

    elif choice == '8':
        function1.choice8()

    elif choice == '9':
        function1.choice9()

    elif choice == '10':
        function1.choice10()

    elif choice == '11':
        function1.choice11()

    elif choice == '12':
        function1.choice12()

    elif choice == '13':
        function1.choice13()

    elif choice == '14':
        function1.choice14()

    elif choice == '15':
        function1.choice15()

    elif choice == '16':
        function1.choice16()

    elif choice == '17':
        function1.choice17()

    elif choice == '18':
        function1.choice18()

    else:
        print (info,"Error... Exiting...")
        os.system('sleep 2')
        exit()

menu()
