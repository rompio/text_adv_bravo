from stringcolor import cs
import os

def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')