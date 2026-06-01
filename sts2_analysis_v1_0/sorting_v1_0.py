import pickle

# create specific encounter class
class Specific:
    def __init__(self, deck, relics, potions_used, damage_taken):
        self.deck = deck
        self.relics = relics
        self.potions_used = potions_used
        self.damage_taken = damage_taken


# function which updates the proper .pickle file with a Spesific encounter
# takes an encounter object (with name attribute), returns None
# ok there is for sure a way to simplify this now. not sure we need to tho lol

def update_encounter(encounter):
    
    if encounter.name.split(".")[1]=="AEONGLASS_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('AEONGLASS_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="AXEBOTS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('AXEBOTS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="BOWLBUGS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('BOWLBUGS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="BOWLBUGS_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('BOWLBUGS_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="BYGONE_EFFIGY_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('BYGONE_EFFIGY_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="BYRDONIS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('BYRDONIS_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="CEREMONIAL_BEAST_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('CEREMONIAL_BEAST_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="CHOMPERS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('CHOMPERS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="CONSTRUCT_MENAGERIE_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('CONSTRUCT_MENAGERIE_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="CORPSE_SLUGS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('CORPSE_SLUGS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="CORPSE_SLUGS_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('CORPSE_SLUGS_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="CUBEX_CONSTRUCT_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('CUBEX_CONSTRUCT_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="CULTISTS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('CULTISTS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="DECIMILLIPEDE_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('DECIMILLIPEDE_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="DEVOTED_SCULPTOR_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('DEVOTED_SCULPTOR_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="ENTOMANCER_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('ENTOMANCER_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="EXOSKELETONS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('EXOSKELETONS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="EXOSKELETONS_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('EXOSKELETONS_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="FABRICATOR_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('FABRICATOR_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="FLYCONID_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('FLYCONID_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="FOGMOG_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('FOGMOG_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="FOSSIL_STALKER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('FOSSIL_STALKER_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="FROG_KNIGHT_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('FROG_KNIGHT_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="FUZZY_WURM_CRAWLER_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('FUZZY_WURM_CRAWLER_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="GLOBE_HEAD_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('GLOBE_HEAD_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="GREMLIN_MERC_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('GREMLIN_MERC_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="HAUNTED_SHIP_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('HAUNTED_SHIP_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="HUNTER_KILLER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('HUNTER_KILLER_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="INFESTED_PRISMS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('INFESTED_PRISMS_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="INKLETS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('INKLETS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="KAISER_CRAB_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('KAISER_CRAB_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="KNIGHTS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('KNIGHTS_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="KNOWLEDGE_DEMON_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('KNOWLEDGE_DEMON_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="LAGAVULIN_MATRIARCH_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('LAGAVULIN_MATRIARCH_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="LIVING_FOG_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('LIVING_FOG_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="LOUSE_PROGENITOR_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('LOUSE_PROGENITOR_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="MAWLER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('MAWLER_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="MECHA_KNIGHT_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('MECHA_KNIGHT_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="MYTES_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('MYTES_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="NIBBITS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('NIBBITS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="NIBBITS_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('NIBBITS_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="OVERGROWTH_CRAWLERS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('OVERGROWTH_CRAWLERS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="OVICOPTER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('OVICOPTER_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="OWL_MAGISTRATE_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('OWL_MAGISTRATE_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="PHANTASMAL_GARDENERS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('PHANTASMAL_GARDENERS_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="PHROG_PARASITE_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('PHROG_PARASITE_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="PUNCH_CONSTRUCT_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('PUNCH_CONSTRUCT_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="QUEEN_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('QUEEN_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="RUBY_RAIDERS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('RUBY_RAIDERS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SCROLLS_OF_BITING_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SCROLLS_OF_BITING_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SCROLLS_OF_BITING_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SCROLLS_OF_BITING_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SEAPUNK_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SEAPUNK_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SEAPUNK_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SEAPUNK_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="SEWER_CLAM_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SEWER_CLAM_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SHRINKER_BEETLE_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SHRINKER_BEETLE_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SKULKING_COLONY_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SKULKING_COLONY_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SLIMED_BERSERKER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SLIMED_BERSERKER_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SLIMES_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SLIMES_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SLIMES_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SLIMES_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SLITHERING_STRANGLER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SLITHERING_STRANGLER_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="SLUDGE_SPINNER_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SLUDGE_SPINNER_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SLUMBERING_BEETLE_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SLUMBERING_BEETLE_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="SNAPPING_JAXFRUIT_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SNAPPING_JAXFRUIT_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SOUL_FYSH_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SOUL_FYSH_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SOUL_NEXUS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SOUL_NEXUS_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="SPINY_TOAD_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('SPINY_TOAD_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="TERROR_EEL_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('TERROR_EEL_ELITE.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="TEST_SUBJECT_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('TEST_SUBJECT_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="THE_INSATIABLE_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('THE_INSATIABLE_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="THE_KIN_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('THE_KIN_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="THE_LOST_AND_FORGOTTEN_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('THE_LOST_AND_FORGOTTEN_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="THE_OBSCURA_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('THE_OBSCURA_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="THIEVING_HOPPER_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('THIEVING_HOPPER_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
    
    elif encounter.name.split(".")[1]=="TOADPOLES_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('TOADPOLES_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="TUNNELER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('TUNNELER_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="TUNNELER_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('TUNNELER_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="TURRET_OPERATOR_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('TURRET_OPERATOR_WEAK.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="TWO_TAILED_RATS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('TWO_TAILED_RATS_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="VANTOM_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('VANTOM_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="VINE_SHAMBLER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('VINE_SHAMBLER_NORMAL.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
    elif encounter.name.split(".")[1]=="WATERFALL_GIANT_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        with open('WATERFALL_GIANT_BOSS.pickle', 'ab') as file:
            pickle.dump(new_specific, file, pickle.HIGHEST_PROTOCOL)
        
        
# function which updates specific encounters when given a 'sample' list of runs
    # each being a list of encounters
# returns None
def sample_to_sort(sample):
    
    for i in range(len(sample)):
        
        for j in range(len(sample[i])):
            
            update_encounter(sample[i][j])





