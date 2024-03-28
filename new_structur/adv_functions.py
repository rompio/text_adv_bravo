from stringcolor import cs
import time
import os
from main import *
#-----------------------------restart and maintance-----------------------------  
"""def actTwo():
    exec(open("text_adv_bravo_ac2.py").read())
    
def actTwo():
    exec(open("text_adv_bravo_ac2.py").read())
    
def actThree():
    exec(open("text_adv_bravo_act_3_copy.py").read())
    """

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
    printc("80%", "red")
    time.sleep(1)
    printc("99%", "red")
    time.sleep(3)
    actOne()

def gameOver():
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