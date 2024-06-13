from stringcolor import cs
import time
import os
from commonFunctions import printc
from commonFunctions import clear_console
#-----------------------------restart and maintance-----------------------------  
def restart(act_One):
    printc("Restarting..", "white")
    time.sleep(1)
    printc("Restarting..", "yellow")
    time.sleep(1)
    printc("Restarting..", "green")
    time.sleep(1)
    printc("10%", "red")
    time.sleep(0.75)
    printc("25%", "red")
    time.sleep(1.5)
    printc("55%", "red")
    time.sleep(1.25)
    printc("80%", "red")
    time.sleep(1)
    printc("99%", "red")
    time.sleep(3)
    act_One()

def gameOver(act_One):
    time.sleep(1)
    printc("...was that the right decision?...", "grey")
    time.sleep(1)
    printc("You Died!", "red")
    time.sleep(2)
    printc("y | n", "blue")
    decision = input("Try again?: ")
    if decision.lower() == "y" or decision.lower() == "yes":
        clear_console()
        restart(act_One)
    elif decision.lower() == "n" or decision.lower() == "no":
        clear_console() 