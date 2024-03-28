from stringcolor import cs
import time

def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

printc("Act 2: The Hunt", "gold")
printc('Together with the pirates, you embark on a perilous journey through dense jungles, treacherous cliffs, and hidden caves, all while evading the islands dangers and discovering its secrets. Along the way, you forge uneasy alliances, navigate deadly traps, and face off against wild beasts')
printc('build : "a scarecrow is built but was not able to scare the bird so you died!" | hide: "you hide in a big tree  - but the bird cracked  the tree open "| arrows: "you shoot an arrow and killed the bird!"', "blue")

decision = input("What do you do?: ")

if decision.lower() == "build":
    printc("The gaint bird gets furious and attacks!.", "red")
    time.sleep(3)
    printc("YOU AND THE GUYS ARE TOAST!", "yellow")
    time.sleep(2)
    printc("YOU ARE DEAD!", "black")
    # restart?
    restart = input("Do you want to try again? ")
    if restart.lower() == "yes":
        exec(open("./story_app_nessa.pyhide").read())
    elif restart.lower() == "no":
        time.sleep(2)
        printc("YOU ARE DEAD!")
elif decision.lower() == "hide":
    # printc("The giant bird attackes the tree! and destroy the tree!")
    printc("The bird gets angry and destroyed and cracks the tree open...", "red")
    time.sleep(3)
    printc("... that the tree is cracked open", "yellow")
    time.sleep(2)
    printc("YOU AND THE GUYS FALL OUT OF THE TREE TO THE GROUND!", "red")
    time.sleep(3)
    printc("YOU ARE DEAD!", "black")
    restart = input("Do you want to try again? ")
    if restart.lower() == "yes":
        exec(open("./story_app_nessa.py").read())
    elif restart.lower() == "no":
        time.sleep(2)
        printc("YOU ARE DEAD!")
elif decision.lower() == "arrow":
    printc("you aim at the gaint monter and shoot an arrow .", "green")
    time.sleep(2)
    printc("You pears the heart of the bird with the arrow.", "yellow")
    time.sleep(2)
    printc("the gaint bird fell down and died.", "blue")
    time.sleep(6)
    printc("you won 100 points!", "gold")
    #next print + new input + new if elif
else :
    printc("You have to choose one of the options!")
    time.sleep(2)
    exec(open("./story_app_nessa.py").read())
    # act3()
    # #next print + new input + new if elif
# def gameOver()

# def act2()

# def act3()