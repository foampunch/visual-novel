﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    $ password1 = "piss"
    $ password2 = "piss"

    $ code = renpy.input("What's Chloe's favourite liquid?")

    if code.lower() == password1:
        e "That's right babey!"

        return

    #Breaking code

    else:
        e "Nice try, dipshit!"
        
        jump start

    e "Nice to meet you, %(name)s!"

    # This ends the game.

    return
