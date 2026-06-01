
# create the encounter class
class Encounter:
    def __init__(self, name, deck, relics, potions_used, damage_taken):
        self.name = name
        self.deck = deck
        self.relics = relics
        self.potions_used = potions_used
        self.damage_taken = damage_taken

# takes a run file string (.json)
# returns a list of encounter objects
def run_to_encounters(file):
    
    #   import test file as data
    import json
    data = json.load(open(file))

    # list with starting deck
    starting_deck = []
    
    # list with starting relics
    starting_relics = []
    
    # starting deck and relic selection
    
    if data["players"][0]["character"]=="CHARACTER.IRONCLAD":
        starting_deck.extend(["CARD.STRIKE_IRONCLAD", "CARD.STRIKE_IRONCLAD", "CARD.STRIKE_IRONCLAD", "CARD.STRIKE_IRONCLAD", "CARD.STRIKE_IRONCLAD", 
                    "CARD.DEFEND_IRONCLAD", "CARD.DEFEND_IRONCLAD", "CARD.DEFEND_IRONCLAD", "CARD.DEFEND_IRONCLAD", "CARD.BASH"])
        starting_relics.append("RELIC.BURNING_BLOOD")
    
    if data["players"][0]["character"]=="CHARACTER.SILENT":
        starting_deck.extend(["CARD.STRIKE_SILENT", "CARD.STRIKE_SILENT", "CARD.STRIKE_SILENT", "CARD.STRIKE_SILENT", "CARD.STRIKE_SILENT", 
                    "CARD.DEFEND_SILENT", "CARD.DEFEND_SILENT", "CARD.DEFEND_SILENT", "CARD.DEFEND_SILENT", "CARD.DEFEND_SILENT",
                    "CARD.SURVIVOR", "CARD.NEUTRALIZE"])
        starting_relics.append("RELIC.RING_OF_THE_SNAKE")
        
    if data["players"][0]["character"]=="CHARACTER.REGENT":
        starting_deck.extend(["CARD.STRIKE_REGENT", "CARD.STRIKE_REGENT", "CARD.STRIKE_REGENT", "CARD.STRIKE_REGENT", "CARD.DEFEND_REGENT",
                     "CARD.DEFEND_REGENT", "CARD.DEFEND_REGENT", "CARD.DEFEND_REGENT", "CARD.FALLING_STAR", "CARD.VENERATE"])
        starting_relics.append("RELIC.DIVINE_RIGHT")
        
    if data["players"][0]["character"]=="CHARACTER.NECROBINDER":
        starting_deck.extend(["CARD.STRIKE_NECROBINDER", "CARD.STRIKE_NECROBINDER", "CARD.STRIKE_NECROBINDER", "CARD.STRIKE_NECROBINDER", "CARD.DEFEND_NECROBINDER",
                     "CARD.DEFEND_NECROBINDER", "CARD.DEFEND_NECROBINDER", "CARD.DEFEND_NECROBINDER", "CARD.BODYGUARD", "CARD.UNLEASH"])
        starting_relics.append("RELIC.BOUND_PHYLACTERY")
        
    if data["players"][0]["character"]=="CHARACTER.DEFECT":
        starting_deck.extend(["CARD.STRIKE_DEFECT", "CARD.STRIKE_DEFECT", "CARD.STRIKE_DEFECT", "CARD.STRIKE_DEFECT", "CARD.DEFEND_DEFECT",
                     "CARD.DEFEND_DEFECT", "CARD.DEFEND_DEFECT", "CARD.DEFEND_DEFECT", "CARD.ZAP", "CARD.DUALCAST"])
        starting_relics.append("RELIC.CRACKED_CORE")
        
    if data["ascension"]>=5:
        starting_deck.append("CARD.ASCENDERS_BANE")
            
    # list of our encounters
    encounters = []
    
    # initiate deck and relics
    curr_deck = starting_deck
    deck = curr_deck
    
    curr_relics = starting_relics
    relics = curr_relics
    
    # we first cycle through the number of acts that we get through
    for i in range(len(data["map_point_history"])):
        # now we cycle through the floors in that act
        for j in range(len(data["map_point_history"][i])):
            
            # simplify data call
            room_stats = data["map_point_history"][i][j]["player_stats"][0]
            room = data["map_point_history"][i][j]["rooms"][0]
            
            # string of room type
            room_type = room["room_type"]
            # if we are in an encounter we add it to our list
            if room_type=="monster" or room_type=="elite" or room_type=="boss":
                # list for the potions used
                new_potions = []
                # if we used potion(s) it gets added here
                if "potion_used" in room_stats:
                    new_potions.extend(room_stats["potion_used"])
                # we now add a new encounter!
                new_encounter = Encounter(room["model_id"], deck, relics, new_potions, room_stats["damage_taken"])
                encounters.append(new_encounter)
                
            
            #update current deck and relics
            
            # adding cards to the deck
            if "cards_gained" in room_stats:
                for k in range(len(room_stats["cards_gained"])):
                    curr_deck.append(room_stats["cards_gained"][k]["id"])
            # removing cards from the deck
            if "cards_removed" in room_stats:
                for k in range(len(room_stats["cards_removed"])):
                    curr_deck.remove(room_stats["cards_removed"][k]["id"])
            # transforming cards
            if "cards_transformed" in room_stats:
                for k in range(len(room_stats["cards_transformed"])):
                    curr_deck.append(room_stats["cards_transformed"][k]["final_card"]["id"])
                    curr_deck.remove(room_stats["cards_transformed"][k]["original_card"]["id"])
            # adding relics
            if "relic_choices" in room_stats:
                for k in range(len(room_stats["relic_choices"])):
                    if room_stats["relic_choices"][k]["was_picked"]:
                        curr_relics.append(room_stats["relic_choices"][k]["choice"])
            # removing relics
            if "relics_removed" in room_stats:
                for k in range(len(room_stats["relics_removed"])):
                    curr_relics.remove(room_stats["relics_removed"][k])
                    
            
            # copy current deck and relics 
            deck = curr_deck[:]
            relics = curr_relics[:]
        
    return encounters
