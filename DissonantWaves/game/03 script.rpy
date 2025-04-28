# This first section will be used to define characters, images and sound variables.
# It will also call upon the label required to jump to Act 1.

# Initialising Ray
init python:
    # Temporary Ray
    TempRay = PlayerCharacter(Character("You"), name = "")

    def assignRay(customName):
        global Ray
        Ray = PlayerCharacter(Character(customName), customName)

    # Home crew
    Luke = Person(
        character = Character("Luke", image = "Luke"), 
        name = "Luke",
        tagline = "Bestest friendo",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Luke neutral",
            "happy": "Luke happy",
            "worried": "Luke worried"
            }
        )

    May = Person(
        character = Character("May", image = "May"), 
        name = "May",
        tagline = "They grow up so fast",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "May neutral",
            "happy": "May happy",
            "worried": "May worried"
            }
        )    


    # Island cast
    Jason = Person(
        character = Character("Jason", image = "Jason"), 
        name = "Jason",
        tagline = "King of edge",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Jason neutral",
            "happy": "Jason happy",
            "worried": "Jason worried"
            }
        )    

    Arthur = Person(
        character = Character("Arthur", image = "Arthur"), 
        name = "Arthur",
        tagline = "Riddle me this",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Arthur neutral",
            "happy": "Arthur happy",
            "worried": "Arthur worried"
            }
        )    

    Senna = Person(
        character = Character("Senna", image = "Senna"), 
        name = "Senna",
        affection = 1-1,
        tagline = "Aka Zed, ",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Senna neutral",
            "happy": "Senna happy",
            "worried": "Senna worried"
            }
        )    

    Willow = Person(
        character = Character("Willow", image = "Willow"), 
        name = "Willow",
        tagline = "Once a Raven",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Willow neutral",
            "happy": "Willow happy",
            "worried": "Willow worried"
            }
        )    

    Camilla = Person(
        character = Character("Camilla", image = "Camilla"), 
        name = "Camilla",
        tagline = "Into the Iris",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Camilla neutral",
            "happy": "Camilla happy",
            "worried": "Camilla worried"
            }
        )    

    Addison = Person(
        character = Character("Addison", image = "Addison"), 
        name = "Addison",
        tagline = "Pep time",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Addison neutral",
            "happy": "Addison happy",
            "worried": "Addison worried"
            }
        )   

    Cain = Person(
        character = Character("Cain", image = "Cain"), 
        name = "Cain",
        tagline = "Cappin' Cain",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Cain neutral",
            "happy": "Cain happy",
            "worried": "Cain worried"
            }
        )   

    Riley = Person(
        character = Character("Riley", image = "Riley"), 
        name = "Riley",
        tagline = "A Valentine worth remembering",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Riley neutral",
            "happy": "Riley happy",
            "worried": "Riley worried"
            }
        )   

    Aaron = Person(
        character = Character("Aaron", image = "Aaron"), 
        name = "Aaron",
        tagline = "NORMALGUY",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Aaron neutral",
            "happy": "Aaron happy",
            "worried": "Aaron worried"
            }
        )   

    Charlotte = Person(
        character = Character("Charlotte", image = "Charlotte"), 
        name = "Charlotte",
        tagline = "Ms connections",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Charlotte neutral",
            "happy": "Charlotte happy",
            "worried": "Charlotte worried"
            }
        )   

    Nick = Person(
        character = Character("Nick", image = "Nick"), 
        name = "Nick",
        tagline = "A dashing draconic figure",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Nick neutral",
            "happy": "Nick happy",
            "worried": "Nick worried"
            }
        )   

    Elliot = Person(
        character = Character("Elliot", image = "Elliot"), 
        name = "Elliot",
        tagline = "Cutest boi",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Elliot neutral",
            "happy": "Elliot happy",
            "worried": "Elliot worried"
            }
        )   

    Emma = Person(
        character = Character("Emma", image = "Emma"), 
        name = "Emma",
        tagline = "Would have made a great Sophia",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Emma neutral",
            "happy": "Emma happy",
            "worried": "Emma worried"
            }
        )   

    Juliette = Person(
        character = Character("Juliette", image = "Juliette"), 
        name = "Juliette",
        tagline = "Queen of Sweissland, princess of noodling",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Juliette neutral",
            "happy": "Juliette happy",
            "worried": "Juliette worried"
            }
        )   

    Alek = Person(
        character = Character("Alek", image = "Alek"), 
        name = "Alek",
        tagline = "Has chicken leg",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Alek neutral",
            "happy": "Alek happy",
            "worried": "Alek worried"
            }
        )   

    Star = Person(
        character = Character("Star", image = "Star"), 
        name = "Star",
        affection = 80085,
        tagline = "Or is it black?",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Star neutral",
            "happy": "Star happy",
            "worried": "Star worried"
            }
        )   

    Javier = Person(
        character = Character("Javier", image = "Javier"), 
        name = "Javier",
        tagline = "Now who's laughing",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Javier neutral",
            "happy": "Javier happy",
            "worried": "Javier worried"
            }
        )   

    Joe = Person(
        character = Character("Joe", image = "Joe"), 
        name = "Joe",
        tagline = "A wishful fantasy",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Joe neutral",
            "happy": "Joe happy",
            "worried": "Joe worried"
            }
        )   

    Toast = Person(
        character = Character("Toast", image = "Toast"), 
        name = "Toast",
        tagline = "Goodest boi",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Toast neutral",
            "happy": "Toast happy",
            "worried": "Toast worried"
            }
        )   


    # Supporting cast
    Shane = Person(
        character = Character("Shane", image = "Shane"), 
        name = "Shane",
        tagline = "Ambition is volatile",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Shane neutral",
            "happy": "Shane happy",
            "worried": "Shane worried"
            }
        )   

    Goruka = Person(
        character = Character("Goruka", image = "Goruka"), 
        name = "Goruka",
        tagline = "Memories of a city of dusk",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Goruka neutral",
            "happy": "Goruka happy",
            "worried": "Goruka worried"
            }
        )   

    Claire = Person(
        character = Character("Claire", image = "Claire"), 
        name = "Claire",
        tagline = "Memories of a city of dusk",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Claire neutral",
            "happy": "Claire happy",
            "worried": "Claire worried"
            }
        )   

    Unknown = Person(
        character = Character("Unknown", image = "Unknown"), 
        name = "Unknown",
        tagline = "Memories of a city of dusk",
        preferedMc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Unknown neutral",
            "happy": "Unknown happy",
            "worried": "Unknown worried"
            }
        ) 

# Jumps to Prologue.rpy Act0, transition to dialogue-focused files
label start:
    jump Act0

return
