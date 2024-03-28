
from adv_functions import *


#-----------------------------First act-----------------------------

def actOne():
    printc("Introduction:", "green")
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
        start_act2()
    
    elif decision.lower() == "negotiate":
        printc("You tell the pirates that you will help them if they give you a part of the tresure")
        time.sleep(2)
        printc('"Pirate" How much do you want?')
        decision = int(input("Enter a percentage: "))
        if decision <= 33:
            tresure += 1
            start_act2()
        elif decision > 33:
            gameOver()





    