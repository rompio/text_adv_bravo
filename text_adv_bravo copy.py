from stringcolor import cs
import time

def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))


intro= "Introduction:"
printc(intro, "green")
printc("You find yourself washed ashore on a mysterious island after a violent storm wreaks havoc on your ship. As you regain consciousness, you realize you're not alone. Pirate remnants litter the beach, and the distant sounds of waves crashing against the rocky cliffs echo ominously. Determined to survive, you venture deeper into the island's uncharted territory, unaware of the dangers lurking within.")
time.sleep(5)
printc("Act 1: The Encounter", "green")
printc("As you explore the island, you stumble upon a ragtag group of pirates who have made this island their hideout. They greet you with suspicion, questioning your motives. With no means of escape, you strike a deal with the pirates: help them locate a legendary treasure rumored to be hidden somewhere on the island, and they'll assist you in returning home.")
printc("fight | help | negotiate", "blue")
decision = input("Choose: ")
if decision.lower() == "fight":
    printc("YOU ARE DEAD")
    #restart?
elif decision.lower() == "help":
    printc("You are helping the pirates and agree to their conditions")
    act2()
    #next print + new input + new if elif
    if decision.lower() == "fight":
        printc("YOU ARE DEAD")
        gameOver()
        #restart?
    elif decision.lower() == "help":
        printc("You are helping the pirates and agree to their conditions")
        #next print + new input + new if elif
    elif decision.lower() == "negotiate":
            printc("You tell the pirates that you will help them if they give you a part of the tresure")
            #next print + new input + new if elif

elif decision.lower() == "negotiate":
    printc("You tell the pirates that you will help them if they give you a part of the tresure")
    #next print + new input + new if elif

# def gameOver()

# def act2()

# def act3()



    