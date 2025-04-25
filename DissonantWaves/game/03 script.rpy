# This first section will be used to define characters, images and sound variables.
# It will also call upon the label required to jump to Act 1.

# Initialising Ray
init python:
    # Ray
    Ray = Character("Ray")
    RayChar = PlayerCharacter(
        character = Ray, 
        name = ""
        )


    # Home crew
    Luke = Character("Luke")
    LukeChar = Person(
        character = Luke, 
        name = "Luke",
        tagline = "Bestest friendo",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Luke Neutral",
            "happy": "Luke Happy",
            "worried": "Luke Worried"
            }
        )

    May = Character("May")
    MayChar = Person(
        character = May, 
        name = "May",
        tagline = "They grow up so fast",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "May Neutral",
            "happy": "May Happy",
            "worried": "May Worried"
            }
        )    


    # Island cast
    Jason = Character("Jason")
    JasonChar = Person(
        character = Jason, 
        name = "Jason",
        tagline = "King of edge",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Jason Neutral",
            "happy": "Jason Happy",
            "worried": "Jason Worried"
            }
        )    

    Arthur = Character("Arthur")
    ArthurChar = Person(
        character = Arthur, 
        name = "Arthur",
        tagline = "Riddle me this",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Arthur Neutral",
            "happy": "Arthur Happy",
            "worried": "Arthur Worried"
            }
        )    

    Senna = Character("Senna")
    SennaChar = Person(
        character = Senna, 
        name = "Senna",
        affection = 1-1,
        tagline = "Aka Zed, ",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Senna Neutral",
            "happy": "Senna Happy",
            "worried": "Senna Worried"
            }
        )    

    Willow = Character("Willow")
    WillowChar = Person(
        character = Willow, 
        name = "Willow",
        tagline = "Once a Raven",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Willow Neutral",
            "happy": "Willow Happy",
            "worried": "Willow Worried"
            }
        )    

    Camilla = Character("Camilla")
    CamillaChar = Person(
        character = Camilla, 
        name = "Camilla",
        tagline = "Into the Iris",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Camilla Neutral",
            "happy": "Camilla Happy",
            "worried": "Camilla Worried"
            }
        )    

    Addison = Character("Addison")
    AddisonChar = Person(
        character = Addison, 
        name = "Addison",
        tagline = "Pep time",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Addison Neutral",
            "happy": "Addison Happy",
            "worried": "Addison Worried"
            }
        )   

    Cain = Character("Cain")
    CainChar = Person(
        character = Cain, 
        name = "Cain",
        tagline = "Cappin' Cain",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Cain Neutral",
            "happy": "Cain Happy",
            "worried": "Cain Worried"
            }
        )   

    Riley = Character("Riley")
    RileyChar = Person(
        character = Riley, 
        name = "Riley",
        tagline = "A Valentine worth remembering",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Riley Neutral",
            "happy": "Riley Happy",
            "worried": "Riley Worried"
            }
        )   

    Aaron = Character("Aaron")
    AaronChar = Person(
        character = Aaron, 
        name = "Aaron",
        tagline = "NORMALGUY",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Aaron Neutral",
            "happy": "Aaron Happy",
            "worried": "Aaron Worried"
            }
        )   

    Charlotte = Character("Charlotte")
    CharlotteChar = Person(
        character = Charlotte, 
        name = "Charlotte",
        tagline = "Ms connections",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Charlotte Neutral",
            "happy": "Charlotte Happy",
            "worried": "Charlotte Worried"
            }
        )   

    Nick = Character("Nick")
    NickChar = Person(
        character = Nick, 
        name = "Nick",
        tagline = "A dashing draconic figure",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Nick Neutral",
            "happy": "Nick Happy",
            "worried": "Nick Worried"
            }
        )   

    Elliot = Character("Elliot")
    ElliotChar = Person(
        character = Elliot, 
        name = "Elliot",
        tagline = "Cutest boi",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Elliot Neutral",
            "happy": "Elliot Happy",
            "worried": "Elliot Worried"
            }
        )   

    Emma = Character("Emma")
    EmmaChar = Person(
        character = Emma, 
        name = "Emma",
        tagline = "Would have made a great Sophia",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Emma Neutral",
            "happy": "Emma Happy",
            "worried": "Emma Worried"
            }
        )   

    Juliette = Character("Juliette")
    JulietteChar = Person(
        character = Juliette, 
        name = "Juliette",
        tagline = "Queen of Sweissland, princess of noodling",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Juliette Neutral",
            "happy": "Juliette Happy",
            "worried": "Juliette Worried"
            }
        )   

    Alek = Character("Alek")
    AlekChar = Person(
        character = Alek, 
        name = "Alek",
        tagline = "Has chicken leg",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Alek Neutral",
            "happy": "Alek Happy",
            "worried": "Alek Worried"
            }
        )   

    Star = Character("Star")
    StarChar = Person(
        character = Star, 
        name = "Star",
        affection = 80085,
        tagline = "Or is it black?",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Star Neutral",
            "happy": "Star Happy",
            "worried": "Star Worried"
            }
        )   

    Javier = Character("Javier")
    JavierChar = Person(
        character = Javier, 
        name = "Javier",
        tagline = "Now who's laughing",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Javier Neutral",
            "happy": "Javier Happy",
            "worried": "Javier Worried"
            }
        )   

    Joe = Character("Joe")
    JoeChar = Person(
        character = Joe, 
        name = "Joe",
        tagline = "A wishful fantasy",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Joe Neutral",
            "happy": "Joe Happy",
            "worried": "Joe Worried"
            }
        )   

    Toast = Character("Toast")
    ToastChar = Person(
        character = Toast, 
        name = "Toast",
        tagline = "Goodest boi",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Toast Neutral",
            "happy": "Toast Happy",
            "worried": "Toast Worried"
            }
        )   


    # Supporting cast
    Shane = Character("Shane")
    ShaneChar = Person(
        character = Shane, 
        name = "Shane",
        tagline = "Ambition is volatile",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Shane Neutral",
            "happy": "Shane Happy",
            "worried": "Shane Worried"
            }
        )   

    Goruka = Character("Goruka")
    GorukaChar = Person(
        character = Goruka, 
        name = "Goruka",
        tagline = "Memories of a city of dusk",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Goruka Neutral",
            "happy": "Goruka Happy",
            "worried": "Goruka Worried"
            }
        )   

    Claire = Character("Claire")
    ClaireChar = Person(
        character = Claire, 
        name = "Claire",
        tagline = "Memories of a city of dusk",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Claire Neutral",
            "happy": "Claire Happy",
            "worried": "Claire Worried"
            }
        )   

    Unknown = Character("Unknown")
    UnknownChar = Person(
        character = Unknown, 
        name = "Unknown",
        tagline = "Memories of a city of dusk",
        prefered_mc = ["friendly", "sarcastic", "direct", "shy"],
        images = {
            "neutral": "Unknown Neutral",
            "happy": "Unknown Happy",
            "worried": "Unknown Worried"
            }
        ) 

# Jumps to Prologue.rpy Act0, transition to dialogue-focused files
label start:
    jump Act_0

return
