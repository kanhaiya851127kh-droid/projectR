import math
import time
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) \
           - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(2)              # slow speed
bgcolor("black")
color("red")
penup()

# text
goto(0, -200)
color("pink")
write("only s", align="center", font=("Arial", 15, "bold"))

color("red")

# heart draw slow
for i in range(6000):
    k = i * 0.01
    goto(hearta(k) * 20, heartb(k) * 20)
    dot(3)
    time.sleep(0.01)   # increase to 0.02 or 0.03 for more slow

goto(0, 0)
done()