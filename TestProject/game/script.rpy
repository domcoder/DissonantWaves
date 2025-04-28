# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    class Actor:
        def __init__ (self, character, name):
            self.c = character
            self.n = name

define e = Actor(Character("Eileen", image = "e"), "Eileen")

image e happy = "e_h"
image e happy = "e_u"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    e.c happy "Happy!"

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    label Test:
        e "Test 1"
    
    label Test2:
        e "Test 2"

    e "Test 3"

    # This ends the game.

    return
