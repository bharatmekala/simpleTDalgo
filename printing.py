# creating map printing function
from colorama import Fore, Style
import numpy as np

def print_colored_number(number):
    color = determine_color(number)
    colored_number = f"{color}{number}{Style.RESET_ALL}"
    print(colored_number, end='\t')

def determine_color(number):
    normalized_value = (number + 200) / 400  # Normalize the value between 0 and 1
    # Interpolate the color based on the normalized value
    r = int(255 * (1 - normalized_value))
    g = int(255 * normalized_value)
    b = 0
    return f"\033[38;2;{r};{g};{b}m"

# Printing the array with colored numbers
def color_map_print(map):
    for row in map:
        for shape in row:
            print_colored_number(shape.value)
        print()

def map_print(map, value=False):
    if value:
        p = "state" + "." + value
    else:
        p = "state"
    print(p)
    for row in map:
        for state in row:
            print(eval(p), end='\t')
        print()

