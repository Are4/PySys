from os import system, name
import sys
import time
from random import randint
import os


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


if os.path.exists("logs"):
    os.remove("logs")
stoplog = 0
logdelete = 0
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
firststoplog = 0
line = 0
data = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
        "", "", "", ""]

while True:
    if line == 200:
        if firststoplog == 0:
            print("You have used more than 200 commands and the logs file won't save any more commands upon restarting the"
                    " script.\n")
            stoplog = 1
            firststoplog = 1
    DONTDELETE = 0
    cmd = input(">")
    if stoplog == 0:
        if cmd != "logclear":
            fl = open("logs", "w")
            data[line] = "User issued the command '" + cmd + "'\n"
            fl.writelines(data)
            line = line + 1
            fl.close()
    if cmd == "cmd":
        print("List of available commands:")
        print("cmd, sd, clr, about, contact, randnr, artwork, createhelp, readhelp, delhelp, logread\n")
    elif cmd == "sd":
        conf = input("Type 'y' to confirm: ")
        if conf == "y":
            if stoplog == 0:
                flc = open("logs", "w")
                data[line] = "    User issued the confirmation command '" + conf + "'\n"
                flc.writelines(data)
                line = line + 1
                flc.close()
            animation = ["Shutting down in 3", "Shutting down in 2", "Shutting down in 1"]
            for i in range(len(animation)):
                sys.stdout.write("\r" + animation[i % len(animation)])
                time.sleep(1)
                sys.stdout.flush()
            break
        else:
            if stoplog == 0:
                flc = open("logs", "w")
                data[line] = "    User issued the confirmation command '" + conf + "'\n"
                flc.writelines(data)
                line = line + 1
                flc.close()
            print("System not shut down\n")
    elif cmd == "clr":
        clear()
        print("Welcome to PySys. An operating system made with python.")
        print("Type 'cmd' to get started\n")
    elif cmd == "about":
        print("You are using PySys 1.1 made by Are4\n")
    elif cmd == "contact":
        print("If you want to send the creator a message, you can do so on Discord to Are4#2139\n")
    elif cmd == "randnr":
        fromnr = input("Generate a random number from ")
        if stoplog == 0:
            flnr = open("logs", "w")
            data[line] = "    User issued the number command '" + fromnr + "'\n"
            flnr.writelines(data)
            line = line + 1
            flnr.close()
        tonr = input("to ")
        if stoplog == 0:
            flnr = open("logs", "w")
            data[line] = "    User issued the number command '" + tonr + "'\n"
            flnr.writelines(data)
            line = line + 1
            flnr.close()
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
                if stoplog == 0:
                    fls = open("logs", "w")
                    data[line] = "    Script said the following '" + tonr + "'\n"
                    fls.writelines(data)
                    line = line + 1
                    fls.close()
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
    elif cmd == "createhelp":
        print("With this command you can create .txt files which you can read later!")
        print("Correct usage: first, type 'create'")
        print("When it says 'filename:', input the filename (one which you won't forget)")
        print("And on the second line after it says 'Write content:', write what you want to be stored.\n")
    elif cmd == "create":
        filename = input("Filename: ")
        if stoplog == 0:
            flf = open("logs", "w")
            data[line] = "    User gave the following filename '" + filename + "'\n"
            flf.writelines(data)
            line = line + 1
            flf.close()
        content = input("Write content: ")
        f = open(filename, "w")
        f.write(content)
        f.close()
        if stoplog == 0:
            fls = open("logs", "w")
            data[line] = "    Script created the file '" + filename + "'\n"
            fls.writelines(data)
            line = line + 1
            fls.close()
        print("Text file successfully created\n")
    elif cmd == "readhelp":
        print("With this command you can read a text file which you created with the 'create' command.")
        print("Correct usage: first, type 'read'")
        print("And then, after it says 'filename:', input the name of the text file\n")
    elif cmd == "read":
        filename = input("Filename: ")
        if stoplog == 0:
            flf = open("logs", "w")
            data[line] = "    User gave the following filename '" + filename + "'\n"
            flf.writelines(data)
            line = line + 1
            flf.close()
        if os.path.exists(filename):
            f = open(filename, "r")
            content = f.read()
            f.close()
            if stoplog == 0:
                fls = open("logs", "w")
                data[line] = "    Script read the file '" + filename + "'\n"
                fls.writelines(data)
                line = line + 1
                fls.close()
            print("The text file had the following message: ")
            print("'", content, "'", sep="")
        else:
            print("That file doesn't exist.")
        print("")
    elif cmd == "delhelp":
        print("With this command, you can delete text files which you created with the 'create' command.")
        print("Correct usage: first, type 'del'")
        print("After it says 'filename:', input the name of the file you wish to delete.")
        print("Then, confirm with a 'y' that you want to delete it and it will be deleted.\n")
    elif cmd == "del":
        filename = input("Filename: ")
        if stoplog == 0:
            flf = open("logs", "w")
            data[line] = "    User gave the following filename '" + filename + "'\n"
            flf.writelines(data)
            line = line + 1
            flf.close()
        if filename == "PySys.py" or filename == "pysys.py" or filename == "Pysys.py" or filename == "pySys.py"\
                or filename == "pYsys.py" or filename == "pysYs.py" or filename == "pysyS.py" or filename == "pysys.Py"\
                or filename == "pysys.pY" or filename == "PYsys.py" or filename == "PysYs.py" or filename == "PysyS.py"\
                or filename == "Pysys.Py" or filename == "Pysys.pY" or filename == "PYsys.py" or filename == "PYSys.py"\
                or filename == "PYsYs.py" or filename == "PYsyS.py" or filename == "PYsys.Py" or filename == "PYsys.pY"\
                or filename == "PYSys.py" or filename == "PYSYs.py" or filename == "PYSyS.py" or filename == "PYSys.Py"\
                or filename == "PYSys.pY" or filename == "PYSYS.py" or filename == "PYSYs.Py" or filename == "PYSYs.pY"\
                or filename == "PYSYS.Py" or filename == "PYSYS.pY" or filename == "PYSYS.PY":
            print("You can't delete this python script. Please don't try to.")
            if stoplog == 0:
                fle = open("logs", "w")
                data[line] = "    Script did not delete the file '" + filename + "'\n"
                fle.writelines(data)
                line = line + 1
                fle.close()
            DONTDELETE = 1
        if filename == "Run.bat" or filename == "run.bat" or filename == "rUn.bat" or filename == "ruN.bat"\
                or filename == "run.Bat" or filename == "run.bAt" or filename == "run.baT" or filename == "RUn.bat"\
                or filename == "RuN.bat" or filename == "Run.Bat" or filename == "Run.bAt" or filename == "Run.baT"\
                or filename == "RUN.bat" or filename == "RUn.Bat" or filename == "RUn.bAt" or filename == "RUn.baT"\
                or filename == "RUN.Bat" or filename == "RUN.bAt" or filename == "RUN.baT" or filename == "RUN.BAt"\
                or filename == "RUN.BaT" or filename == "RUN.BAT":
            print("You can't delete this file. Please don't try to.")
            if stoplog == 0:
                fle = open("logs", "w")
                data[line] = "    Script did not delete the file '" + filename + "'\n"
                fle.writelines(data)
                line = line + 1
                fle.close()
            DONTDELETE = 1
        if filename == "logs":
            print("You can't delete this file. Please don't try to.")
            if stoplog == 0:
                fle = open("logs", "w")
                data[line] = "    Script did not delete the file '" + filename + "'\n"
                fle.writelines(data)
                line = line + 1
                fle.close()
            DONTDELETE = 1
        if DONTDELETE == 0:
            if os.path.exists(filename):
                confirm = input("Type 'y' to confirm that action: ")
                if stoplog == 0:
                    flc = open("logs", "w")
                    data[line] = "    User issued the confirmation command '" + confirm + "'\n"
                    flc.writelines(data)
                    line = line + 1
                    flc.close()
                if confirm == "y":
                    os.remove(filename)
                    if stoplog == 0:
                        fls = open("logs", "w")
                        data[line] = "    Script deleted the file '" + filename + "'\n"
                        fls.writelines(data)
                        line = line + 1
                        fls.close()
                    print("File deleted.")
                else:
                    print("File not deleted")
            else:
                print("That file doesn't exist.")
                if stoplog == 0:
                    fls = open("logs", "w")
                    data[line] = "    Script said the file '" + filename + "' doesn't exist\n"
                    fls.writelines(data)
                    line = line + 1
                    fls.close()
        print("")
    elif cmd == "logread":
        logread = open("logs", "r")
        logs = logread.read()
        logread.close()
        print("")
        print(logs)
        print("")
    else:
        print("Command '", cmd, "' does not exist.\n", sep="")
