import pygame
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Social Network")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 200)
GREEN = (50, 180, 100)
RED = (220, 60, 60)
GRAY = (220, 220, 220)
DARK_GRAY = (100, 100, 100)

# Fonts
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)

# User data
users = {
    "kanhaiya": {
        "username": "kanhaiya",
        "followers": [],
        "following": []
    },
    "rahul": {
        "username": "rahul",
        "followers": [],
        "following": []
    },
    "amit": {
        "username": "amit",
        "followers": [],
        "following": []
    },
    "rohit": {
        "username": "rohit",
        "followers": [],
        "following": []
    },
    "suresh": {
        "username": "suresh",
        "followers": [],
        "following": []
    }
}

# Current logged-in user
current_user = users["kanhaiya"]

# Buttons
buttons = {
    "1": pygame.Rect(50, 120, 300, 55),
    "2": pygame.Rect(50, 200, 300, 55),
    "3": pygame.Rect(50, 280, 300, 55),
    "4": pygame.Rect(50, 360, 300, 55),
    "5": pygame.Rect(50, 440, 300, 55)
}

menu_items = [
    "1. View Followers",
    "2. Remove Follower",
    "3. Add Follower",
    "4. View Following",
    "5. Logout"
]

# Variables
message = ""
input_text = ""
input_active = False
input_action = None
logged_in = True
show_list = None

clock = pygame.time.Clock()


# Draw text function
def draw_text(text, x, y, color=BLACK, font_type=small_font):
    image = font_type.render(text, True, color)
    screen.blit(image, (x, y))


# Start input
def start_input(action):
    global input_active, input_action, input_text, message

    input_active = True
    input_action = action
    input_text = ""
    message = ""


# Handle input submission
def submit_input():
    global input_active, input_action, input_text
    global message, show_list

    username = input_text.strip().lower()

    if not username:
        message = "Please enter a username."
        return

    if username not in users:
        message = "User not found."
        return

    target_user = users[username]

    if username == current_user["username"]:
        message = "You cannot follow yourself."
        return

    # Add follower / follow user
    if input_action == "add":

        if target_user in current_user["following"]:
            message = "Already following this user."

        else:
            current_user["following"].append(target_user)
            target_user["followers"].append(current_user)

            message = f"You are now following {username}."

    # Remove follower
    elif input_action == "remove":

        if target_user in current_user["followers"]:

            current_user["followers"].remove(target_user)

            # Remove the corresponding following relationship
            if current_user in target_user["following"]:
                target_user["following"].remove(current_user)

            message = f"{username} removed from your followers."

        else:
            message = f"{username} is not your follower."

    input_active = False
    input_action = None
    input_text = ""


# Main loop
while True:

    screen.fill(WHITE)

    # Title
    draw_text(
        "MINI SOCIAL NETWORK",
        250,
        35,
        BLUE,
        font
    )

    if logged_in:

        draw_text(
            f"Logged in as: {current_user['username']}",
            50,
            80,
            GREEN
        )

        # Draw buttons
        for key, rect in buttons.items():

            pygame.draw.rect(screen, GRAY, rect)

            pygame.draw.rect(
                screen,
                DARK_GRAY,
                rect,
                2
            )

            text = small_font.render(
                menu_items[int(key) - 1],
                True,
                BLACK
            )

            screen.blit(
                text,
                (rect.x + 15, rect.y + 15)
            )

        # Display followers
        draw_text("Followers:", 450, 120, BLUE)

        if current_user["followers"]:

            for i, follower in enumerate(
                current_user["followers"]
            ):
                draw_text(
                    follower["username"],
                    450,
                    160 + i * 30
                )

        else:
            draw_text("No followers.", 450, 160, RED)

        # Display following
        draw_text("Following:", 650, 120, BLUE)

        if current_user["following"]:

            for i, following in enumerate(
                current_user["following"]
            ):
                draw_text(
                    following["username"],
                    650,
                    160 + i * 30
                )

        else:
            draw_text("Not following anyone.", 650, 160, RED)

        # Input box
        if input_active:

            draw_text(
                "Enter username:",
                400,
                400,
                BLUE
            )

            input_box = pygame.Rect(400, 440, 350, 50)

            pygame.draw.rect(
                screen,
                WHITE,
                input_box
            )

            pygame.draw.rect(
                screen,
                BLUE,
                input_box,
                2
            )

            draw_text(
                input_text,
                410,
                452
            )

            draw_text(
                "Press ENTER to submit",
                400,
                500,
                DARK_GRAY
            )

        # Display message
        if message:
            draw_text(
                message,
                50,
                550,
                GREEN if "not" not in message.lower()
                and "cannot" not in message.lower()
                else RED
            )

    else:

        draw_text(
            "You are logged out!",
            300,
            280,
            RED,
            font
        )

    pygame.display.update()

    # Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard input
        if input_active and event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                submit_input()

            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]

            elif event.key == pygame.K_ESCAPE:
                input_active = False
                input_action = None
                input_text = ""
                message = "Input cancelled."

            else:
                if event.unicode.isprintable():
                    input_text += event.unicode

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and logged_in:

            if input_active:
                continue

            for key, rect in buttons.items():

                if rect.collidepoint(event.pos):

                    # View Followers
                    if key == "1":
                        show_list = "followers"
                        message = (
                            f"Total followers: "
                            f"{len(current_user['followers'])}"
                        )

                    # Remove Follower
                    elif key == "2":
                        start_input("remove")

                    # Add Follower
                    elif key == "3":
                        start_input("add")

                    # View Following
                    elif key == "4":
                        show_list = "following"
                        message = (
                            f"Total following: "
                            f"{len(current_user['following'])}"
                        )

                    # Logout
                    elif key == "5":
                        logged_in = False
                        message = "Logged out."