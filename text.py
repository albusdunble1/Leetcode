import pyfiglet
from colorama import init
from termcolor import colored

init()

user_input = input("Please enter your text: ")
color = input("What color do you want?: ")
available_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

if color not in available_colors:
    color = 'magenta'

result = colored(pyfiglet.figlet_format(user_input), color)
print(result) 