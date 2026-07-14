import time

lyrics = [
    "💖 ...",
    "🎶 Naina Laage Toh Jaage....",
    "💖 Bina Dori Ya Dhaage....",
    "🤗 Bandhte Hai Do Naina Khwaab Se....",
    "🥰 Na Ataa Ho",
    "🩷 Na Pta Ho...",
    "💖 Kore Nazino Main Koi Aa Bse....",
    "🤍 Iska Uska Na Iska Hai...",
    "🤔 Jaane Kitna Hai Kiska Hai...",
    "💝 Kaisi Bhasha Mai Bhasha Mai Hai Likha..."
]

delays = [0.6, 0.6, 0.9, 2.9, 1.4, 1.4, 2.7, 1.0, 2.4, 8.3]

def type_line(line):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()

for line, delay in zip(lyrics, delays):
    type_line(line)
    time.sleep(delay)