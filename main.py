from adv_functions import clear_console
from adv_actOne import actOne
from adv_actTwo import start_act2
from adv_actThree import actThree

tresure = 0
pirates = 100

#-----------------------------Start the game-----------------------------

decision = input("You want to play? y/n: ")
if decision.lower() == "y" or decision.lower() == "yes":
        clear_console()
        actOne()
        
elif decision.lower() == "n" or decision.lower() == "no":
        clear_console()