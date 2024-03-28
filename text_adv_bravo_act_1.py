from stringcolor import cs
import time
import os

tresure = 0
pirates = 100

intro = "Introduction:"

def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

#-----------------------------Link to the other act's-----------------------------

def actTwo():
    exec(open("text_adv_bravo_ac2.py").read())
    
def actThree():
    exec(open("text_adv_bravo_act_3_copy.py").read())

#-----------------------------restart and maintance-----------------------------    

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

#-----------------------------First act-----------------------------

def actOne():
    printc(intro, "green")
    printc("You find yourself washed ashore on a mysterious island after a violent storm wreaks havoc on your ship. As you regain consciousness, you realize you're not alone. Pirate remnants litter the beach, and the distant sounds of waves crashing against the rocky cliffs echo ominously. Determined to survive, you venture deeper into the island's uncharted territory, unaware of the dangers lurking within.")
    time.sleep(4)
    printc("Act 1: The Encounter", "green")
    printc("As you explore the island, you stumble upon a ragtag group of pirates who have made this island their hideout. They greet you with suspicion, questioning your motives. With no means of escape, you strike a deal with the pirates: help them locate a legendary treasure rumored to be hidden somewhere on the island, and they'll assist you in returning home.")
    time.sleep(1)
    printc("fight | help | negotiate", "blue")
    decision = input("Choose: ")
    if decision.lower() == "fight":
        gameOver()
    
    elif decision.lower() == "help":
        printc("You are helping the pirates and agree to their conditions")
        time.sleep(3)
        actTwo()
    
    elif decision.lower() == "negotiate":
        printc("You tell the pirates that you will help them if they give you a part of the tresure")
        time.sleep(2)
        printc('"Pirate" How much do you want?')
        decision = int(input("Enter a percentage: "))
        if decision <= 33:
            tresure += 1
            actTwo()
        elif decision > 33:
            gameOver()

#-----------------------------Start the game-----------------------------
decision = input("You want to play? y/n: ")
if decision.lower() == "y" or decision.lower() == "yes":
        clear_console()
        actOne()
        
elif decision.lower() == "n" or decision.lower() == "no":
        clear_console()





    