from stringcolor import cs
import time
from text_adv_bravo_act_1 import gameOver
from text_adv_bravo_act_1 import actThree

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
    decision = input("CHOOSE: ") 
    if "fight" in decision.lower():
        printc("With a grim determination, you draw your weapon and prepare to defend yourself against the mysterious birds. The pirates beside you follow suit, their expressions hardened with resolve as they brace for battle.", "yellow")
        time.sleep(1)
        printc("Despite your best efforts, the birds prove to be formidable opponents, their swift movements and coordinated attacks making it difficult to gain the upper hand. With each passing moment, your group finds themselves pushed further and further back, forced to retreat under the relentless assault of the avian assailants.", "orange")
        time.sleep(1)
        printc("In the end, you are victorious, but at a great cost. The pirates lie wounded and exhausted, their numbers decimated by the fierce battle. As you survey the aftermath of the conflict, you realize that the jungle holds many more dangers than you could have ever imagined, and that your journey is far from over.", "yellow")
        time.sleep(2)
        actThree()
    elif "scare" in decision.lower():
        printc("You try to scare the birds away by shouting and waving your arms, but they only seem to grow more agitated and aggressive in response.", "yellow")
        time.sleep(1)
        printc("The largest of the birds swoops down from the treetops, its talons extended as it dives towards you with deadly intent. In a desperate bid to defend yourself, you raise your weapon and prepare to face the creature head-on.", "orange")
        time.sleep(2)
        printc("You are dead.","red")
        time.sleep(1)
        try_again = input("Do you want to try again? (y/n): ")
        if try_again.lower() == "y":
            start_act2()
        else:
            printc("Thank you for playing. Goodbye!", "yellow")
            time.sleep(1)
            exit()
    elif "communicate" in decision.lower():
        printc("You raise your hands in a non-threatening gesture and try to mimic the birds' calls, hoping to establish some form of communication.", "yellow")
        time.sleep(1)
        printc("To your surprise, the largest of the birds descends from the treetops, its wings outstretched as it lands gracefully before you. Its bright eyes regard you with a mixture of curiosity and intelligence, and you sense a faint understanding passing between you.", "yellow")
        time.sleep(1)
        printc("With a soft cooing sound, the bird begins to communicate in a series of intricate melodies and gestures, its meaning clear even if its language is not. It seems to be warning you of danger ahead, urging caution in your journey through the jungle.", "yellow")
        time.sleep(1)
        printc("Thanks to your decision to communicate with the birds, you've gained valuable insight into the dangers lurking within the jungle, and perhaps even made some unexpected allies along the way. But remember, the path ahead is still fraught with peril, and every choice you make could have far-reaching consequences.", "green")
        time.sleep(1)
        actThree()
    else:
        printc("Invalid decision. Please choose one of the available options.", "red")
        printc(act2_decisions, "cyan")
        decision = input("CHOOSE: ")

start_act2()
