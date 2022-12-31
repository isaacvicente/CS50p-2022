import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)
    print(f"Output:\n{figlet.renderText(text)}")
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    chosen_font = sys.argv[2]
    if chosen_font in fonts:
        text = input("Input: ")
        figlet.setFont(font=chosen_font)
        print(f"Output:\n{figlet.renderText(text)}")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
