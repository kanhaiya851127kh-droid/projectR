import time
from colorama import Fore, Style, init

init(autoreset=True)

def typing_effect(text, delay=0.04):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def send_message(sender, message, color):
    typing_effect(color + f"{sender}: {message}")
    time.sleep(1)

def seen():
    print(Fore.GREEN + "✓✓ Seen")
    time.sleep(1)

def typing(name="GF"):
    print(Fore.YELLOW + f"{name} is typing...")
    time.sleep(2)

# Chat start
send_message("You", "Hii ", Fore.CYAN)

seen()

typing("GF")

send_message("GF", "hi 🙂", Fore.MAGENTA)

send_message("You", "Miss you ❤️", Fore.CYAN)

seen()

typing("GF")

send_message("GF", "show what ...", Fore.MAGENTA)

time.sleep(0.25)

typing("GF")

send_message("GF", "🚫 You are blocked.", Fore.RED)