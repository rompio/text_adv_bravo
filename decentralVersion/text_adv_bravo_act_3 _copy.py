import pygame
from stringcolor import cs
import time
from text_adv_bravo_act_1 import gameOver 

pygame.mixer.init()
pygame.mixer.music.load("./_music/pirates of the caribbean theme best.mp3")
pygame.mixer.music.set_volume(0.2)  # Set the volume to half
pygame.mixer.music.play(-1)

def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

printc("Act 3: The Guardian", "gold")
printc('At last, you reach the heart of the island, where the legendary treasure is said to lie. But guarding it is a fearsome creature, a monstrous guardian awakened by your intrusion. "What do thy want?" it roars from the caves opening')
printc('shout: "Give me your treasure or we will kill you!" | whine: "please do not be disturbed - we will go our separate ways"| offer: "We bring a present for your majesty!"', "blue")

decision = input("What do you do?: ")

if decision.lower() == "shout":
    printc("The ugly monster gets furious and sets the whole area on fire with it's burning breath!.", "red")
    time.sleep(3)
    printc("YOU AND THE GUYS ARE TOAST!", "yellow")
    time.sleep(2)
    printc("YOU ARE DEAD!", "black")
    gameOver()

    # restart?
    restart = input("Do you want to try again? ")
    if restart.lower() == "yes":
        exec(open("./text_adv_bravo_act_3.py").read())
    elif restart.lower() == "no":
        time.sleep(2)
        printc("YOU ARE DEAD!")
    else :
        printc("You have to choose one of the options!")
        time.sleep(2)
        exec(open("./text_adv_bravo_act_3.py").read())
elif decision.lower() == "whine":
    # printc("The ugly monster cracks itself so hard that the earth starts cracking too! YOU AND THE GUYS FALL INTO AN ENDLESS HOLE! YOU ARE DEAD!")
    printc("The ugly monster cracks itself so hard...", "red")
    time.sleep(3)
    printc("... that the earth starts cracking too!", "yellow")
    time.sleep(2)
    printc("YOU AND THE GUYS FALL INTO AN ENDLESS HOLE!", "red")
    time.sleep(3)
    printc("YOU ARE DEAD!", "black")
    gameOver()
    """
    restart = input("Do you want to try again? ")
    if restart.lower() == "yes":
        exec(open("./text_adv_bravo_act_3.py").read())
    elif restart.lower() == "no":
        time.sleep(2)
        printc("YOU ARE DEAD!")
    else :
        printc("You have to choose one of the options!")
        time.sleep(2)
        exec(open("./text_adv_bravo_act_3.py").read())
    """
elif decision.lower() == "offer":
    printc("The monster seems to be courious and comes closer to you.", "green")
    time.sleep(2)
    printc("You give it the present and it opens it.", "yellow")
    time.sleep(2)
    printc("It's a mirror. The monster sees itself and starts crying. It's so ugly that it can't stand itself. It runs away and you can take the treasure.", "blue")
    time.sleep(6)
    printc("Instead of leaving the Island, you decide to become the pirates leader and party with them all day every day on the beach, with whiskey sours till the end of all days!", "red")
    time.sleep(7)
    printc("YOU WIN!", "gold")
    time.sleep(2)
    #next print + new input + new if elif
else :
    printc("You have to choose one of the options!")
    time.sleep(2)
    exec(open("./text_adv_bravo_act_3.py").read())
    # act3()



    