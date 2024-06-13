from stringcolor import cs
import time
import os
#-----------------------------restart and maintance-----------------------------  

def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def restart():
    printc("Restarting..", "white")
    time.sleep(1)
    printc("Restarting..", "yellow")
    time.sleep(1)
    printc("Restarting..", "green")
    time.sleep(1)
    printc("10%", "red")
    time.sleep(1)
    printc("40%", "red")
    time.sleep(1)
    printc("80%", "red")
    time.sleep(1)
    printc("99%", "red")
    time.sleep(3)
    #Pass here actOne() as a parameter

def gameOver():#Pass here actOne() as a parameter
    time.sleep(1)
    printc("...was that the right decision?...", "grey")
    time.sleep(1)
    printc("You Died!", "red")
    time.sleep(2)
    printc("y | n", "blue")
    decision = input("Try again?: ")
    if decision.lower() == "y" or decision.lower() == "yes":
        clear_console()
        restart()
    elif decision.lower() == "n" or decision.lower() == "no":
        clear_console()    