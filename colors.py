from colorama import init
from termcolor import colored

init()

print(colored("Hello", "cyan", "on_magenta", attrs=['blink']))