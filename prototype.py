#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:50:27 2026

@author: peterhogan
"""

#   import test file as data
import json

data = json.load(open('1780162403.json'))

# list with current deck
deck = []

# list with current relics
relics = []

# starting deck and relic selection

if data["players"][0]["character"]=="CHARACTER.IRONCLAD":
    deck.extend(["CARD.STRIKE_IRONCLAD", "CARD.STRIKE_IRONCLAD", "CARD.STRIKE_IRONCLAD", "CARD.STRIKE_IRONCLAD", "CARD.STRIKE_IRONCLAD", 
                "CARD.DEFEND_IRONCLAD", "CARD.DEFEND_IRONCLAD", "CARD.DEFEND_IRONCLAD", "CARD.DEFEND_IRONCLAD", "CARD.BASH"])
    relics.append("RELIC.BURNING_BLOOD")

if data["players"][0]["character"]=="CHARACTER.SILENT":
    deck.extend(["CARD.STRIKE_SILENT", "CARD.STRIKE_SILENT", "CARD.STRIKE_SILENT", "CARD.STRIKE_SILENT", "CARD.STRIKE_SILENT", 
                "CARD.DEFEND_SILENT", "CARD.DEFEND_SILENT", "CARD.DEFEND_SILENT", "CARD.DEFEND_SILENT", "CARD.DEFEND_SILENT",
                "CARD.SURVIVOR", "CARD.NEUTRALIZE"])
    relics.append("RELIC.RING_OF_THE_SNAKE")
    
if data["players"][0]["character"]=="CHARACTER.REGENT":
    deck.extend(["CARD.STRIKE_REGENT", "CARD.STRIKE_REGENT", "CARD.STRIKE_REGENT", "CARD.STRIKE_REGENT", "CARD.DEFEND_REGENT",
                 "CARD.DEFEND_REGENT", "CARD.DEFEND_REGENT", "CARD.DEFEND_REGENT", "CARD.FALLING_STAR", "CARD.VENERATE"])
    relics.append("RELIC.DIVINE_RIGHT")
    
if data["players"][0]["character"]=="CHARACTER.NECROBINDER":
    deck.extend(["CARD.STRIKE_NECROBINDER", "CARD.STRIKE_NECROBINDER", "CARD.STRIKE_NECROBINDER", "CARD.STRIKE_NECROBINDER", "CARD.DEFEND_NECROBINDER",
                 "CARD.DEFEND_NECROBINDER", "CARD.DEFEND_NECROBINDER", "CARD.DEFEND_NECROBINDER", "CARD.BODYGUARD", "CARD.UNLEASH"])
    relics.append("RELIC.BOUND_PHYLACTERY")
    
if data["players"][0]["character"]=="CHARACTER.DEFECT":
    deck.extend(["CARD.STRIKE_DEFECT", "CARD.STRIKE_DEFECT", "CARD.STRIKE_DEFECT", "CARD.STRIKE_DEFECT", "CARD.DEFEND_DEFECT",
                 "CARD.DEFEND_DEFECT", "CARD.DEFEND_DEFECT", "CARD.DEFEND_DEFECT", "CARD.ZAP", "CARD.DUALCAST"])
    relics.append("RELIC.CRACKED_CORE")
    
if data["ascension"]>=5:
    deck.append("CARD.ASCENDERS_BANE")
    
# create the encounter class
class Encounter:
    def __init__(self, name, deck, relics, potions, damage):
        self.name = name
        self.deck = deck
        self.relics = relics
        self.potions = potions
        self.damage = damage
        
# list of our encounters
encounters = []

# we first cycle through the number of acts that we get through
for i in range(len(data["map_point_history"])):
    
    # now we cycle through the floors in that act
    for j in range(len(data["map_point_history"][i])):
        
        # if we are in an encounter we add it to our list
        if data["map_point_history"][i][j]["rooms"][0]["room_type"]=="monster" or 
        data["map_point_history"][i][j]["rooms"][0]["room_type"]=="elite" or 
        data["map_point_history"][i][j]["rooms"][0]["room_type"]=="boss":
            
            # list for the potions used
            new_potions = []
            
            # if we used potion(s) it gets added here
            if "potion_used" in data["map_point_history"][i][j]["player_stats"][0]:
                new_potions.extend(data["map_point_history"][i][j]["player_stats"][0]["potion_used"])
                
            # we now add a new encounter!
            new_encounter = Encounter(data["map_point_history"][i][j]["rooms"][0]["model_id"], deck, relics, new_potions, data["map_point_history"][i][j]["player_stats"][0]["damage_taken"])
            encounters.append(new_encounter)
            
        # adding cards to the deck
        if "cards_gained" in data["map_point_history"][i][j]["player_stats"][0]:
            for k in range(len(data["map_point_history"][i][j]["player_stats"][0]["cards_gained"])):
                deck.append(data["map_point_history"][i][j]["player_stats"][0]["cards_gained"][k]["id"])
                
        # removing cards from the deck
        if "cards_removed" in data["map_point_history"][i][j]["player_stats"][0]:
            for k in range(len(data["map_point_history"][i][j]["player_stats"][0]["cards_removed"])):
                deck.remove(data["map_point_history"][i][j]["player_stats"][0]["cards_removed"][k]["id"])
                
        # transforming cards
        if "cards_transformed" in data["map_point_history"][i][j]["player_stats"][0]:
            for k in range(len(data["map_point_history"][i][j]["player_stats"][0]["cards_transformed"])):
                deck.append(data["map_point_history"][i][j]["player_stats"][0]["cards_transformed"][k]["final_card"]["id"])
                deck.remove(data["map_point_history"][i][j]["player_stats"][0]["cards_transformed"][k]["original_card"]["id"])
                
        # adding relics
        if "relic_choices" in data["map_point_history"][i][j]["player_stats"][0]:
            for k in range(len(data["map_point_history"][i][j]["player_stats"][0]["relic_choices"])):
                if data["map_point_history"][i][j]["player_stats"][0]["relic_choices"][k]["was_picked"]:
                    relics.append(data["map_point_history"][i][j]["player_stats"][0]["relic_choices"][k]["choice"])
                    
        # removing relics
        if "relics_removed" in data["map_point_history"][i][j]["player_stats"][0]:
            for k in range(len(data["map_point_history"][i][j]["player_stats"][0]["relics_removed"])):
                relics.remove(data["map_point_history"][i][j]["player_stats"][0]["relics_removed"][k])
                
print(encounters[-1].name)
print(encounters[-1].deck)
print(encounters[-1].relics)
