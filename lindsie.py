import os
import time
import sys


# Color formatting codes
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def typing_effect(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def open_gift():
    # Frame 1: Closed Gift
    gift_closed = """
           ______
        |__  __|
        |  ||  |
        |__||__|
        [      ]
        [      ]
        [______]
    """

    # Frame 2: Opening
    gift_opening = """
           \\  /
          __||__
         [      ]
         [      ]
         [______]
    """

    # Frame 3: Opened / Burst
    gift_open = """
        ✨  .  * ✨
         \\  |  /
        -- 🎁 --
         /  |  \\
        ✨  * .  ✨
    """

    frames = [gift_closed, gift_opening, gift_open]
    for frame in frames:
        clear()
        print(f"\n\n\n{Color.YELLOW}{frame}{Color.END}")
        time.sleep(0.8)


# --- THE SEQUENCE ---

clear()
print(f"\n\n\n{Color.BOLD}Lindsie, you have a delivery...{Color.END}")
time.sleep(2)

open_gift()

print(f"\n{Color.CYAN}{Color.BOLD}Happy Birthday, Lindsie.{Color.END}\n")

# Your specific message
message = (
    "I wish you all the best in the world, and please take care of yourself "
    "because I'm not around to watch you. I hope I'm there to celebrate "
    "your birthday with you.\n\n"
    "I love you, and I miss you so much."
)

typing_effect(f"{Color.PURPLE}{message}{Color.END}", 0.07)

# Final Heart
print(f"\n{Color.RED}       ♥   ♥")
print("      ♥♥♥♥♥♥♥")
print("       ♥♥♥♥♥")
print(f"        ♥♥♥{Color.END}")
print(f"         {Color.RED}♥{Color.END}")

print(f"\n{Color.DARKCYAN}(Press Ctrl+C to close this message){Color.END}")

# Keep the window open
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nGoodbye!")