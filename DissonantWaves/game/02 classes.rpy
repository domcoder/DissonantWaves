init python:
    # Player character class definition
    class PlayerCharacter:
        def __init__(self, character, name, colour = "#000000", friendly = 0, sarcastic = 0, direct = 0, shy = 0):
            self.c = character
            self.name = name
            self.friendly = friendly
            self.sarcastic = sarcastic
            self.direct = direct
            self.shy = shy

    # NPC character class definition
    class Person:
        def __init__(self, character, name, alive = True, affection=0, tagline="", prefered_mc=[], images=None):
            self.c = character
            self.name = name
            self.alive = alive
            self.affection = affection
            self.tagline = tagline
            self.prefered_mc = prefered_mc
            self.images = images

        # Procedure to modify character affection value taking a positive or negative integer
        def affectionChange(self, change):
            self.affection += change

        # WIP wide system to return general attitude of character
        def returnAffectionState(self, player):
            # Maps preferred_mc traits to player variable
            trait_map = {
                "friendly": player.friendly,
                "sarcastic": player.sarcastic,
                "direct": player.direct,
                "shy": player.shy
            }

            # Filter the trait values to only those in NPC’s preferred list
            preferred_values = [trait_map[trait] for trait in self.prefered_mc if trait in trait_map]

            # Get the max preferred trait value, or 0 if empty
            bonus = sqrt(max(preferred_values)) if preferred_values else 0

            score = self.affection + bonus
            
            # Map thresholds to symbols
            thresholds = [0, 5, 10, 15, 20, 25]
            symbols = ["---", "--", "-", "+", "++", "+++"]

            for t, s in zip(thresholds, symbols):
                if score <= t:
                    return s
            # error return message
            return "\_(o.o)_/"