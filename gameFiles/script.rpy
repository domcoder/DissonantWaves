#This first section will be used to define characters, images and sound variables.
#It will also call upon the label required to jump to Act 1.

#Main Cast
define Ray = Character(" ")
define Luke = Character("Luke", who_color="#d92938")
define May = Character("May", who_color="#d92938")

define Jason = Character("Jason", who_color="#d92938")
#Jace, king of edge

define Arthur = Character("Arthur", who_color="#994f00")
#Riddle me this

define Senna = Character("Senna", who_color="#ebfeff")
#Aka Zed

define Willow = Character("Willow", who_color="#eaccff")
#Once a Raven

define Camilla = Character("Camilla", who_color="#fbff91")
#Into the Iris

define Addison = Character("Addison", who_color="#508754")
#Pep time

define Cain = Character("Harrison Cain", who_color="#57c29c")
#Cappin Cain

define Riley = Character("Riley", who_color="#d92938")
#A Valentine worth remembering

define Aaron = Character("Aaron", who_color="#d92938")
#NORMALGUY

define Charlotte = Character("Charlotte", who_color="#d92938")
#Connections

define Nick = Character("Nick", who_color="#d92938")
#A dashing draconic figure

define Elliot = Character("Elliot", who_color="#d92938")
#Cutest boi

define Emma = Character("Emma", who_color="#d92938")
#Would have made a great Sophia

define Juliette = Character("Juliette", who_color="#d92938")
#Queen of Sweissland, princess of noodling

define Alek = Character("Alek", who_color="#d92938")
#Has chicken leg

define Star = Character("Star", who_color="#d92938")
#Or is it black?

define Javier = Character("Javier", who_color="#d92938")
#Now who's laughing

define Joe = Character("Uncle Joe", who_color="#d92938")
#A wishful fantasy

define Toast = Character("Toast", who_color="#d92938")
#Goodest boi

define Shane = Character("Producer Shane", who_color="#d92938")
#Ambition is volatile

define Goruka = Character("Director Goruka Chimurida", who_color="#d92938")
#Memories of a city of dusk

#Side Cast
define Claire = Character("Claire")
define Unknown = Character("???")

#Scene Images
image black = "#000"
image bg Hut = "bg_hut.jpg"
image bg Diner = "bg diner.jpg"
image bg Plane = "bg plane.jpg"
image bg Ship = "bg ship.jpg"

#Home Cast Images
image Luke Neutral = "Luke_Neutral.png"
image Luke Happy = "Luke_Happy.png"
image Luke Worried = "Luke_Worried.png"

image May Neutral = "May Neutral.png"
image May Happy = "May Happy.png"
image May Worried = "May Worried.png"

#Main Cast Images
image Joe Neutral = "Joe Neutral.png"

image Jason Neutral = "Jason Neutral.png"

image Willow Neutral = "Willow Neutral.png"


#Side Cast Images
image Claire Happy = "Claire Happy.png"

image Captain Neutral = "Captain Neutral.png"

image Shane Neutral = "Shane Neutral.png"

#Character Stats
init python:
    #Ray Personality Stats
    Nice = 0        #Confirmed r/niceguys
    Dick = 0        #You monster
    Shy = 0         #Quiet but caring
    Snarky = 0      #Our personal favourite to write for

    #Character friendship
    Luke_Friendship = 0
    Jason_Friendship = 0
    Arthur_Friendship = 0
    Senna_Friendship = 1-1
    Willow_Friendship = 0
    Camilla_Friendship = 0
    Addiso_Friendship = 0
    Cain_Friendship = 0
    Riley_Friendship = 0
    Aaron_Friendship = 0
    Charlotte_Friendship = 0
    Nick_Friendship = 0
    Elliot_Friendship = 0
    Emma_Friendship = 0
    Juliette_Friendship = 0
    Ale_Friendship = 0
    Star_Friendship = 80085
    Javier_Friendship = 0
    Joe_Friendship = 0
    Toast_Friendship = 0

    #Variables
    NameCount = 5
    NameChosen = False
    Watch_Intro_Vid = False
    Intro_Vid_Feelings = 0
    Shane_Time_Limit = 2


#Positions
transform halfleft:
    xalign 0.25 yalign 1.5

transform halfright:
    xalign 0.75 yalign 1.5

transform mid:
    xalign 0.5 yalign 1.5

label start:

    jump Act_1

return
