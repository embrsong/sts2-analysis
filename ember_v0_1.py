

#   import test file as data
import json

f = open('1780101781.json')
data = json.load(f)


# SIMPLIFY!


#   gets cards from a list of card dict objects

def get_cards(cards_dict):
    cards = []
    for card_dict in cards_dict:
        card = card_dict.get("id").split(".")[1]
        cards.append(card)
    return cards



#   function to get relic added from relic choices
    #   floor 6 has elite relic

#   so far only works if only one relic is chosen
def relic_from_choices(relic_choices):
    if relic_choices != None:
        for choice in relic_choices:
            #print(choice)
            if choice.get("was_picked") == True:
                relic = choice.get("choice").split(".")[1]
        return relic
    else:
        return relic_choices
    
'''
floor6stats = data["map_point_history"][0][6]["player_stats"][0]
relic_choices = floor6stats.get("relic_choices")
print(relic_from_choices(relic_choices))
'''

num_floors = len(data["map_point_history"][0])

floor1stats = data["map_point_history"][0][1]["player_stats"][0]

#print(floor1stats["damage_taken"])
#print(floor1stats.get("potion_used"))

#   relics gained
#print(relic_from_choices(floor1stats.get("relic_choices")))

#   relics lost
#print(floor1stats.get("relics_removed"))


#   cards gained
#print(get_cards(floor1stats.get("cards_gained")))

#   cards lost
#   cards upgraded
#   cards transformed
#   ^^^do these once we have a run that cares
#           this run cares about cards lost from bridge event!

#starting deck

def get_starting_deck(data):
    deck = data["players"][0]["deck"]
    starting_cards = []
    for card in deck:
        if card['floor_added_to_deck'] == 1:
            starting_cards.append(card)
    
    formatted_deck = get_cards(starting_cards)
    return(formatted_deck)

#   NOTE: cards added to deck from neow bonus on floor 1 are also part of
#       starting deck calculation here, so don't do deck change calculations
#       for floor 1 (index 0)


#   same for relics
def get_starting_relics(data):
    relics = data["players"][0]["relics"]
    starter_relics = []
    for relic in relics:
        if relic['floor_added_to_deck'] == 1:
            starter_relics.append(relic)
        
    
    formatted_relics = get_cards(starter_relics)
    return(formatted_relics)




class Encounter:
    def __init__(self, encounter, damage, pots, relics, deck):
        self.encounter = encounter
        self.damage = damage
        self.pots = pots
        self.relics = relics
        self.deck = deck





encounters = []

curr_deck = get_starting_deck(data)
curr_relics = get_starting_relics(data)

for i in range(num_floors):
    
    map_point_type = data["map_point_history"][0][i]["map_point_type"]
    curr_stats = data["map_point_history"][0][i]["player_stats"][0]
    
    #  get relevant id
    if map_point_type != "shop": #NEED to account for others here
        curr_room = data["map_point_history"][0][i]["rooms"][0]["model_id"]
         
        
        #   get damage taken
        damage = curr_stats["damage_taken"]
        
        #   get potions used in encounters
        pots = curr_stats.get("potion_used")
        
        
        #   save curr_room, damage, pots, relics, deck in an object, and add to list
        curr_encounter = Encounter(curr_room,damage,pots,curr_relics,curr_deck) 
        encounters.append(curr_encounter)
    
    if i>=1:
        cards_gained = curr_stats.get("cards_gained")
        if cards_gained != None:
            cards_gained = get_cards(cards_gained)
            for card in cards_gained:
                curr_deck = curr_deck + [card]
        
        relic = relic_from_choices(curr_stats.get("relic_choices"))
        if relic != None:
            curr_relics = curr_relics + [relic]




for floor in encounters:
    #print(floor.encounter)
    #print(floor.damage)
    #print(floor.deck)
    #print(floor.relics)
    #print(floor.pots)
    pass
    
    
#   need to filter out the events somehow - shouldn't be too hard
    
    
    
    
    