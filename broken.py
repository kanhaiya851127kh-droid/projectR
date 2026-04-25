import time
from colorama import Fore, Style, init
import random

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

# simple GF replies
gf_replies = ["hi 🙂", "kya kar rahe ho?", "hmm...", "to ky ❤️", "busy hu"]

# chat loop
while True:
    user_msg = input("You: ")
    
    if user_msg.lower() == "bye":
        send_message("GF", "Bye 🙂", Fore.MAGENTA)
        break

    send_message("You", user_msg, Fore.CYAN)

    seen()
    typing("GF")

    # random reply
    reply = random.choice(gf_replies)
    send_message("GF", reply, Fore.MAGENTA)

    # prank block condition 😅
    if "miss you" in user_msg.lower():
        typing("GF")
        send_message("GF", "🚫 You are blocked.", Fore.RED)
        break


##kugubtuuggu6fo

  