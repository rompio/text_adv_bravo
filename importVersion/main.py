from adv_functions import *
import pygame
from stringcolor import cs
import os
import time

tresure = 0
pirates = 100
#-----------------------------restart-----------------------------  
pygame.mixer.init()
pygame.mixer.music.load("./_music/pirates of the caribbean theme best.mp3")
pygame.mixer.music.set_volume(0.2)  # Set the volume to half
pygame.mixer.music.play(-1)

"""def actTwo():
    exec(open("text_adv_bravo_ac2.py").read())

    

def actTwo():
    exec(open("text_adv_bravo_ac2.py").read())
    
def actThree():
    exec(open("text_adv_bravo_act_3_copy.py").read())
    """
text = """


                                                                                                                                                               
                                                                                                                                                               
                                                                                                                                                               
                                                                                                                                                               
                                                                                                                                                               
                                                                                                 πππ                                                           
                                                                                                πππππ                                                          
                                        ππππππππππππ                                           πππππ                                                           
                                   πππππ          πππππ                                       πππππ                 πππ                                        
                                 πππππ             ππππππ                                    πππππ                 ππππ                                        
                                πππππ        π      πππππ ππ                                πππππ                 ππ π                                         
                                πππππ      ππ      ππππππππ                                πππππ ππ  πππππ       πππ                                           
                                 ππππ     ππ       ππππππππ                         πππππππππππ    πππ  ππ     πππππ                                           
                                   ππ   πππ       πππππππ          πππ      πππππππππππ  πππππ   πππ   ππ       ππππ                                           
                                       πππ      ππππππππππ ππππ  ππππππ   πππ    πππππ  πππππ   ππππππππ  ππππ  πππ                                            
                                     ππππππ πππππππππππππ  ππππππ    ππ ππππ    πππππ  πππππ   ππππ ππ  ππππ    πππ                                            
                                    ππππ πππππππππππππππ   ππππ   ππππ ππππ    πππππ  πππππ   πππππ    πππππ   ππππ                                            
                       ππ          ππππ    ππππ   πππππ   ππππ    πππ ππππ    πππππ  πππππ   ππππππ    πππππππππππ                                             
                     πππππ       πππππ           πππππ   ππππ        ππππ    πππππ  ππππππ  πππππππππππ πππππππππ                                              
                    πππππππ    ππππππ           πππππ   πππππ       πππππ   πππππππππππππππππππππππππ    ππππππ                                                
                    ππππππππππππππππ           πππππ   πππππ        πππππππππππππππ πππππππ   ππππ                                                             
                   πππππππππππππππ            πππππππππππππ         ππππππ   ππππ    ∞π                                                                        
                   ππππππππππππππ             πππππππ ππππ                          ∞πππ                                                                       
                    ππππππππππππ              πππππ  ππ                            ≈ππππ                                                                       
                     πππππππππ                                                    ≈ππππ                                                                        
                                                                            πππ  ≈ππππ                                                                         
                                                                         ππ  ≈π ∞ππππ                                                                          
                                                                       ππ     ππππππ    π                                                                      
                                                                     πππ    ππππππππ πππ                                                                       
                                                                    πππ    ≈πππππππππππ                                                                        
                                                                   ππππ    ≈ππππππ                                                                             
                                                                  ππππ     πππππ ≈π                                                                            
                                                                 πππππππππππππππ ππ                                                                            
                                                                 ≈ππππππππ≈ππππ  ππ                                                                            
                                                                  ≈πππππ  ππππ   ≈π                                                                            
                                                                         ππππ    π                                                                             
                                                                        ≈ππππ   √π                                                                  ππ         
                                                                        πππππ  ≈π                                                                  πππ         
                                                                       ≈ππππ  ∞π                    ππ√  π        √ππππ                           πππ          
                                                                       ≈ππππππππ                 π     π         πππ √π                          πππ           
                                                                       ≈ππππππ                ∞π     ππ         πππ √π                          πππ            
                                                                       ≈πππππ                ππ     ππ         πππ π                       πππ πππ             
                                                            πππ         ≈≈∞                  √ππ  ∞ππ     πππ ππππ        ππ πππ πππππ  ππ  ≈ππππ              
                                                           ππππ                                  πππ     ππ√ πππ   πππ≈ππππ  πππ  ∞πππ√ππ    πππ               
                               πππ                         πππ                                  πππ     ∞ππ πππ  √ππ   ππππ ∞ππ  ∞πππ∞ππ   √πππ                
          πππππππππππππππππ∞∞ ππ                          πππ                         π       ∞πππ   πππππ πππ  πππ   ππππ √ππ  ≈πππ∞ππππππππππ π              
        ∞πππ       πππ       ππ                     ∞π∞  πππ    πππ  πππ ππ≈ππππππππππππ     ππππ   ππ  πππππ  πππ   ππππ ππππ ∞ππππππππππ πππππ               
        πππ      ππππ      πππ                     ≈π√∞∞πππ   ππ  π  πππ    πππππππ∞√πππππππππππ  πππ  ≈ππππ  πππ   πππππππππ  πππππ∞πππ   ≈ππ                 
         √π     π πππ    ππππ        πππ π∞πππ     ππ  πππ  πππ  π  ∞ππ  πππ        πππππππππππ  ≈ππππππππππππππππππππππππππ   ≈ππ                             
              √π ≈πππ   ππππ  ππ ≈   πππ  ∞ππ     √ππ πππ  πππ∞≈   √ππ              ππππππππππ   ππππππππππππ ≈πππ                                             
             ππ  πππ    πππ ππ   π  √ππ  √πππππππ ≈πππππ  ππππ    ππππ               ππππππππ      ≈√∞                                                         
   ππ      πππ   πππ π πππ∞ππ   ππ ≈ππ  √ππππππ   πππππ  ππππππππ πππ                  ≈≈≈                                                                     
  ππππ   ππππ   πππππ ππππππ    πππππ  ππππ πππππππππππππ πππππ  πππ                                                                                           
 πππππππππππ    √ππ  ∞πππππππ ππ ππππ ππππππ∞πππππ ≈πππ                                                                                                        
 ππππππππππ      π   ≈πππππππππ  πππ   ≈∞∞                                                                                                                     
 ≈ππππππππ            ≈πππ≈√                                                                                                                                   
  π∞ππππ  






"""



def blink_text(txt):
    for char in text:
        if char == "π" or "∞" or "≈" or "√" or "≠" or "∏"or "∑"or "∆"or "∫"or "√"or "∞"or "∂":
            print("\033[31m" + char, end="", flush=True)  # Blinking red text
        else:
            print("\033[0m" + char, end="", flush=True)  # Steady black text
        time.sleep(0.0001)  # Pause for 0.5 seconds
    print("\033[0m")  # Reset text color to default

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


#-------------------------------------actThree---------------------------

def actThree():
    print("")
    printc("Act 3: The Guardian", "gold")
    print("")
    printc('At last, you reach the heart of the island, where the legendary treasure is said to lie. But guarding it is a fearsome creature, a monstrous guardian awakened by your intrusion. "What do thy want?" it roars from the caves opening')
    printc('shout: "Give me your treasure or we will kill you!" | whine: "please do not be disturbed - we will go our separate ways"| offer: "We bring a present for your majesty!"', "blue")
    print("")
    decision = input("What do you do?: ")

    if decision.lower() == "shout":
        print("")
        printc("The ugly monster gets furious and sets the whole area on fire with it's burning breath!.", "red")
        time.sleep(3)
        print("")
        printc("YOU AND THE GUYS ARE TOAST!", "yellow")
        time.sleep(2)
        print("")
        printc("YOU ARE DEAD!", "black")
        gameOver()

        # restart?
        restart = input("Do you want to try again? ")
        if restart.lower() == "yes":
            actThree()
        elif restart.lower() == "no":
            time.sleep(2)
            print("")
            printc("YOU ARE DEAD!")
        else :
            print("")
            printc("You have to choose one of the options!")
            time.sleep(2)
            actThree()
    elif decision.lower() == "whine":
        # printc("The ugly monster cracks itself so hard that the earth starts cracking too! YOU AND THE GUYS FALL INTO AN ENDLESS HOLE! YOU ARE DEAD!")
        print("")
        printc("The ugly monster cracks itself so hard...", "red")
        time.sleep(3)
        print("")
        printc("... that the earth starts cracking too!", "yellow")
        time.sleep(2)
        print("")
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
        print("")
        printc("The monster seems to be courious and comes closer to you.", "green")
        time.sleep(2)
        print("")
        printc("You give it the present and it opens it.", "yellow")
        time.sleep(2)
        print("")
        printc("It's a mirror. The monster sees itself and starts crying. It's so ugly that it can't stand itself. It runs away and you can take the treasure.", "blue")
        time.sleep(6)
        print("")
        printc("Instead of leaving the Island, you decide to become the pirates leader and party with them all day every day on the beach, with whiskey sours till the end of all days!", "red")
        time.sleep(7)
        print("")
        printc("YOU WIN!", "gold")
        time.sleep(2)
        #next print + new input + new if elif
    else :
        print("")
        printc("You have to choose one of the options!")
        time.sleep(2)
        actThree()
#-------------------------actTwo-----------------
# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def start_act2():
    act2 = """
Act 2: The Hunt

Together with the pirates, you embark on a perilous journey through dense jungles, treacherous cliffs, and hidden caves, all while evading the island's dangers and discovering its secrets. Along the way, you forge uneasy alliances, navigate deadly traps, and face off against wild beasts.

Suddenly, a piercing screech echoes through the jungle, causing your group to freeze in their tracks. A group of strange, bird-like creatures swoops down...
"""
    act2_decisions = "(Try to fight them with the pirates/ Try to scare them away/ Attempt to communicate with the birds.)"

    printc(act2, "yellow")
    time.sleep(3)
    printc(act2_decisions, "cyan")
    time.sleep(0.5)
    print("")
    decision = input("CHOOSE: ") 
    if "fight" in decision.lower():
        print("")
        printc("With a grim determination, you draw your weapon and prepare to defend yourself against the mysterious birds. The pirates beside you follow suit, their expressions hardened with resolve as they brace for battle.", "yellow")
        time.sleep(1)
        print("")
        printc("Despite your best efforts, the birds prove to be formidable opponents, their swift movements and coordinated attacks making it difficult to gain the upper hand. With each passing moment, your group finds themselves pushed further and further back, forced to retreat under the relentless assault of the avian assailants.", "orange")
        time.sleep(1)
        print("")
        printc("In the end, you are victorious, but at a great cost. The pirates lie wounded and exhausted, their numbers decimated by the fierce battle. As you survey the aftermath of the conflict, you realize that the jungle holds many more dangers than you could have ever imagined, and that your journey is far from over.", "yellow")
        time.sleep(2)
        actThree()
    elif "scare" in decision.lower():
        print("")
        printc("You try to scare the birds away by shouting and waving your arms, but they only seem to grow more agitated and aggressive in response.", "yellow")
        time.sleep(1)
        print("")
        printc("The largest of the birds swoops down from the treetops, its talons extended as it dives towards you with deadly intent. In a desperate bid to defend yourself, you raise your weapon and prepare to face the creature head-on.", "orange")
        time.sleep(2)
        print("")
        printc("You are dead.","red")
        time.sleep(1)
        print("")
        try_again = input("Do you want to try again? (y/n): ")
        if try_again.lower() == "y":
            start_act2()
        else:
            printc("Thank you for playing. Goodbye!", "yellow")
            time.sleep(1)
            exit()
    elif "communicate" in decision.lower():
        print("")
        printc("You raise your hands in a non-threatening gesture and try to mimic the birds' calls, hoping to establish some form of communication.", "yellow")
        time.sleep(1)
        print("")
        printc("To your surprise, the largest of the birds descends from the treetops, its wings outstretched as it lands gracefully before you. Its bright eyes regard you with a mixture of curiosity and intelligence, and you sense a faint understanding passing between you.", "yellow")
        time.sleep(1)
        print("")
        printc("With a soft cooing sound, the bird begins to communicate in a series of intricate melodies and gestures, its meaning clear even if its language is not. It seems to be warning you of danger ahead, urging caution in your journey through the jungle.", "yellow")
        time.sleep(1)
        print("")
        printc("Thanks to your decision to communicate with the birds, you've gained valuable insight into the dangers lurking within the jungle, and perhaps even made some unexpected allies along the way. But remember, the path ahead is still fraught with peril, and every choice you make could have far-reaching consequences.", "green")
        time.sleep(1)
        actThree()
    else:
        print("")
        printc("Invalid decision. Please choose one of the available options.", "red")
        printc(act2_decisions, "cyan")
        print("")
        decision = input("CHOOSE: ")
#-----------------------------First act-----------------------------


def actOne():
    tresure = 0
    print("")
    printc("Introduction:", "green")
    print("")
    printc("You find yourself washed ashore on a mysterious island after a violent storm wreaks havoc on your ship. As you regain consciousness, you realize you're not alone. Pirate remnants litter the beach, and the distant sounds of waves crashing against the rocky cliffs echo ominously. Determined to survive, you venture deeper into the island's uncharted territory, unaware of the dangers lurking within.")
    time.sleep(4)
    print("")
    printc("Act 1: The Encounter", "green")
    print("")
    printc("As you explore the island, you stumble upon a ragtag group of pirates who have made this island their hideout. They greet you with suspicion, questioning your motives. With no means of escape, you strike a deal with the pirates: help them locate a legendary treasure rumored to be hidden somewhere on the island, and they'll assist you in returning home.")
    time.sleep(1)
    print("")
    printc("fight | help | negotiate", "blue")
    print("")
    decision = input("Choose: ")
    if decision.lower() == "fight":
        gameOver()
    
    elif decision.lower() == "help":
        print("")
        printc("You are helping the pirates and agree to their conditions")
        time.sleep(3)
        start_act2()
    
    elif decision.lower() == "negotiate":
        print("")
        printc("You tell the pirates that you will help them if they give you a part of the tresure")
        time.sleep(2)
        print("")
        printc('"Pirate" How much do you want?')
        print("")
        decision = int(input("Enter a percentage: "))
        if decision <= 33:
            tresure += 1
            start_act2()
        elif decision > 33:
            gameOver()
#-----------------------------Start the game-----------------------------
clear_console()
blink_text(text)

print("")
decision = input("You want to play? y/n: ")
if decision.lower() == "y" or decision.lower() == "yes":
        clear_console()
        actOne()
        
elif decision.lower() == "n" or decision.lower() == "no":
        clear_console()