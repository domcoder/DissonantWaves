# Audio and visual resources pre-loaded for everything else

# Banned names text file
init python:
    with renpy.file("bannedNames.txt") as bannedNames:
            bannedContent = bannedNames.read().decode("utf-8") 
    bannedContent = [bannedName.strip().lower() for bannedName in bannedContent.split(",") if bannedName.strip()]

# Background images
image black:
    "#000000"
image bg hut:
    "bg_hut"
image bg diner:
    "bg_diner"
image bg plane:
    "bg_plane"
image bg ship:
    "bg_ship"

# Characters

# Main characters: angry, annoyed, concerned/worried, determined/serious, flirting, happy, neutral, sad, surprised, cry, excited, laugh, nervous, blush, and sleeping
# Side characters: neutral, negative (could be thoughtful, annoyed, puzzled, worried, etc depending on personality), positive (happy, laughing, joking, smirking, flirting, etc)

# Home Cast Images
image Luke neutral:
    "Luke_neutral.png"
image Luke happy:
    "Luke_happy.png"
image Luke sad:
    "Luke_sad.png"
image Luke worried:
    "Luke_worried.png"

image May neutral:
    "May_neutral.png"
image May happy:
    "May_happy.png"
image May sad:
    "May_sad.png"
image May worried:
    "May_worried.png"

# Main Cast Images
image Joe neutral:
    "Joe_neutral.png"

image Jason neutral:
    "Jason_neutral.png"

image Willow neutral:
    "Willow_neutral.png"


# Side Cast Images
image Claire happy:
    "Claire_happy.png"
image Claire happy:
    "Claire_worried.png"

image Captain neutral:
    "Captain_neutral.png"

image Shane neutral:
    "Shane_neutral.png"