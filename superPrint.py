from time import sleep
import sys
from colorama import Fore


def Sprint(text, color="WHITE"):

    color = color.upper()
    
    if color == "RED":
        Color = Fore.RED

    elif color == "GREEN":
        Color = Fore.GREEN

    elif color == "BLUE":
        Color = Fore.BLUE

    elif color == "CYAN":
        Color = Fore.CYAN

    elif color == "LIGHTMAGENTA":
        Color = Fore.LIGHTMAGENTA_EX

    elif color == "LIGHTYELLOW":
        Color = Fore.LIGHTYELLOW_EX

    elif color == "LIGHTBLUE":
        Color = Fore.LIGHTBLUE_EX

    else:
        Color = Fore.WHITE

    for x in text:
        print(Color, x, end='', sep='')
        sys.stdout.flush()
        sleep(0.05)

    print(Fore.WHITE, end="")

