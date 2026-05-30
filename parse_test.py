#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:02:04 2026

@author: JHB
"""


#   import test file as data
import json

f = open('1780101781.json')
data = json.load(f)


#   some tests

#print(data)
#print(data["acts"])
#print(data["ascension"])
#print(data["map_point_history"])


#   neow bonus
#print(data["map_point_history"][0][0])
#print(data["map_point_history"][0][0]["player_stats"][0]["cards_gained"])


#   floor 1 combat
#print(data["map_point_history"][0][1])
#print(data["map_point_history"][0][1]["player_stats"][0]["cards_gained"])



#   gives number of floors in the run?
num_floors = len(data["map_point_history"][0])


#   get list of all cards gained
cards_added = []
for floor in range(num_floors):
    # something bad happens on these floors - shop or event?
    if floor !=7 and floor !=8:
        #print("floor =" +str(floor))
        card = data["map_point_history"][0][floor]["player_stats"][0]["cards_gained"]
        cards_added.append(card)

print(cards_added)

#   another way to get the final deck?
#print(data["players"][0]["deck"])

final_deck = []
total_cards = len(data["players"][0]["deck"])
for n in range(total_cards):
    final_deck.append(data["players"][0]["deck"][n]["id"].split(".")[1])

print(final_deck)

