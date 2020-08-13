from os import system, name
import sys
import time
from random import randint


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


print("__________         _________             ")
print("\______   \___.__./   _____/__.__. ______")
print(" |     ___<   |  |\_____  <   |  |/  ___/")
print(" |    |    \___  |/        \___  |\___ \ ")
print(" |____|    / ____/_______  / ____/____  >")
print("           \/            \/\/         \/ ")
time.sleep(0.5)
print("")
animation = ["Loading script 0%", "Loading script 4%", "Loading script 9%", "Loading script 25%", "Loading script 40%", "Loading script 70%", "Loading script 75%", "Loading script 95%", "Loading script 100%"]
for i in range(len(animation)):
    sys.stdout.write("\r" + animation[i % len(animation)])
    time.sleep(0.1)
    sys.stdout.flush()
clear()
print("__________         _________             ")
print("\______   \___.__./   _____/__.__. ______")
print(" |     ___<   |  |\_____  <   |  |/  ___/")
print(" |    |    \___  |/        \___  |\___ \ ")
print(" |____|    / ____/_______  / ____/____  >")
print("           \/            \/\/         \/ ")
print("")
print("Script loaded!")
time.sleep(2)
clear()
print("Welcome to PySys. An operating system made with python.")
print("Type 'cmd' to get started\n")

while True:
    cmd = input(">")
    if cmd == "cmd":
        print("List of available commands:")
        print("cmd, shutdown, clr, about, contact, randnr, artwork\n")
    elif cmd == "shutdown":
        conf = input("Type 'y' to confirm: ")
        if conf == "y":
            animation = ["Shutting down in 3", "Shutting down in 2", "Shutting down in 1"]
            for i in range(len(animation)):
                sys.stdout.write("\r" + animation[i % len(animation)])
                time.sleep(1)
                sys.stdout.flush()
            break
        else:
            print("System not shut down\n")
    elif cmd == "clr":
        clear()
        print("Welcome to PySys. An operating system made with python.")
        print("Type 'cmd' to get started\n")
    elif cmd == "about":
        print("You are using PySys 1.0 made by Are4\n")
    elif cmd == "contact":
        print("If you want to send the creator a message, you can do so on Discord to Are4#2139\n")
    elif cmd == "randnr":
        fromnr = input("Generate a random number from ")
        tonr = input("to ")
        print("")
        nrcheck = fromnr + tonr
        not_allowed_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for not_allowed_list_item in not_allowed_list:
            nrcheck = nrcheck.replace(not_allowed_list_item, "")
        if nrcheck == "":
            continuee = 1
        else:
            continuee = 0
        if continuee == 1:
            fromnrint = int(fromnr)
            tonrint = int(tonr)
            if fromnrint > tonrint:
                continuee1 = 0
            else:
                continuee1 = 1
            if continuee1 == 1:
                gen = randint(fromnrint, tonrint)
                print("The random number is", gen)
            if continuee1 == 0:
                print("Your from number value is higher than the to number value")
        if continuee == 0:
            print("Your values have at least a character other than a number.")
        print("")
    elif cmd == "artwork":
        print("__________         _________             ")
        print("\______   \___.__./   _____/__.__. ______")
        print(" |     ___<   |  |\_____  <   |  |/  ___/")
        print(" |    |    \___  |/        \___  |\___ \ ")
        print(" |____|    / ____/_______  / ____/____  >")
        print("           \/            \/\/         \/ ")
        print("")
    else:
        print("Command '", cmd, "' does not exist.\n", sep="")
