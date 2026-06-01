
# create specific encounter class
class Specific:
    def __init__(self, deck, relics, potions_used, damage_taken):
        self.deck = deck
        self.relics = relics
        self.potions_used = potions_used
        self.damage_taken = damage_taken
        
# defining every single possible encounter
        
AEONGLASS_BOSS = []
AXEBOTS_NORMAL = []
BOWLBUGS_NORMAL = []
BOWLBUGS_WEAK = []
BYGONE_EFFIGY_ELITE = []
BYRDONIS_ELITE = []
CEREMONIAL_BEAST_BOSS = []
CHOMPERS_NORMAL = []
CONSTRUCT_MENAGERIE_NORMAL = []
CORPSE_SLUGS_NORMAL = []
CORPSE_SLUGS_WEAK = []
CUBEX_CONSTRUCT_NORMAL = []
CULTISTS_NORMAL = []
DECIMILLIPEDE_ELITE = []
DEVOTED_SCULPTOR_WEAK = []
ENTOMANCER_ELITE = []
EXOSKELETONS_NORMAL = []
EXOSKELETONS_WEAK = []
FABRICATOR_NORMAL = []
FLYCONID_NORMAL = []
FOGMOG_NORMAL = []
FOSSIL_STALKER_NORMAL = []
FROG_KNIGHT_NORMAL = []
FUZZY_WURM_CRAWLER_WEAK = []
GLOBE_HEAD_NORMAL = []
GREMLIN_MERC_NORMAL = []
HAUNTED_SHIP_NORMAL = []
HUNTER_KILLER_NORMAL = []
INFESTED_PRISMS_ELITE = []
INKLETS_NORMAL = []
KAISER_CRAB_BOSS = []
KNIGHTS_ELITE = []
KNOWLEDGE_DEMON_BOSS = []
LAGAVULIN_MATRIARCH_BOSS = []
LIVING_FOG_NORMAL = []
LOUSE_PROGENITOR_NORMAL = []
MAWLER_NORMAL = []
MECHA_KNIGHT_ELITE = []
MYTES_NORMAL = []
NIBBITS_NORMAL = []
NIBBITS_WEAK = []
OVERGROWTH_CRAWLERS = []
OVICOPTER_NORMAL = []
OWL_MAGISTRATE_NORMAL = []
PHANTASMAL_GARDENERS_ELITE = []
PHROG_PARASITE_ELITE = []
PUNCH_CONSTRUCT_NORMAL = []
QUEEN_BOSS = []
RUBY_RAIDERS_NORMAL = []
SCROLLS_OF_BITING_NORMAL = []
SCROLLS_OF_BITING_WEAK = []
SEAPUNK_NORMAL = []
SEAPUNK_WEAK = []
SEWER_CLAM_NORMAL = []
SHRINKER_BEETLE_WEAK = []
SKULKING_COLONY_ELITE = []
SLIMED_BERSERKER_NORMAL = []
SLIMES_NORMAL = []
SLIMES_WEAK = []
SLITHERING_STRANGLER_NORMAL = []
SLUDGE_SPINNER_WEAK = []
SLUMBERING_BEETLE_NORMAL = []
SNAPPING_JAXFRUIT_NORMAL = []
SOUL_FYSH_BOSS = []
SOUL_NEXUS_ELITE = []
SPINY_TOAD_NORMAL = []
TERROR_EEL_ELITE = []
TEST_SUBJECT_BOSS = []
THE_INSATIABLE_BOSS = []
THE_KIN_BOSS = []
THE_LOST_AND_FORGOTTEN_NORMAL = []
THE_OBSCURA_NORMAL = []
THIEVING_HOPPER_WEAK = []
TOADPOLES_WEAK = []
TUNNELER_NORMAL = []
TUNNELER_WEAK = []
TURRET_OPERATOR_WEAK = []
TWO_TAILED_RATS_NORMAL = []
VANTOM_BOSS = []
VINE_SHAMBLER_NORMAL = []
WATERFALL_GIANT_BOSS = []

# function which updates each specific event with the specific object for a given encounter
        
def update_encounter(encounter):
    
    if encounter.name.split(".")[1]=="AEONGLASS_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        AEONGLASS_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="AXEBOTS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        AXEBOTS_NORMAL.append(new_specific)
    
    elif encounter.name.split(".")[1]=="BOWLBUGS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        BOWLBUGS_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="BOWLBUGS_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        BOWLBUGS_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="BYGONE_EFFIGY_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        BYGONE_EFFIGY_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="BYRDONIS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        BYRDONIS_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="CEREMONIAL_BEAST_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        CEREMONIAL_BEAST_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="CHOMPERS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        CHOMPERS_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="CONSTRUCT_MENAGERIE_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        CONSTRUCT_MENAGERIE_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="CORPSE_SLUGS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        CORPSE_SLUGS_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="CORPSE_SLUGS_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        CORPSE_SLUGS_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="CUBEX_CONSTRUCT_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        CUBEX_CONSTRUCT_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="CULTISTS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        CULTISTS_NORMAL.append(new_specific)
    
    elif encounter.name.split(".")[1]=="DECIMILLIPEDE_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        DECIMILLIPEDE_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="DEVOTED_SCULPTOR_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        DEVOTED_SCULPTOR_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="ENTOMANCER_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        ENTOMANCER_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="EXOSKELETONS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        EXOSKELETONS_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="EXOSKELETONS_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        EXOSKELETONS_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="FABRICATOR_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        FABRICATOR_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="FLYCONID_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        FLYCONID_NORMAL.append(new_specific)
    
    elif encounter.name.split(".")[1]=="FOGMOG_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        FOGMOG_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="FOSSIL_STALKER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        FOSSIL_STALKER_NORMAL.append(new_specific)
    
    elif encounter.name.split(".")[1]=="FROG_KNIGHT_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        FROG_KNIGHT_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="FUZZY_WURM_CRAWLER_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        FUZZY_WURM_CRAWLER_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="GLOBE_HEAD_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        GLOBE_HEAD_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="GREMLIN_MERC_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        GREMLIN_MERC_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="HAUNTED_SHIP_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        HAUNTED_SHIP_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="HUNTER_KILLER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        HUNTER_KILLER_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="INFESTED_PRISMS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        INFESTED_PRISMS_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="INKLETS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        INKLETS_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="KAISER_CRAB_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        KAISER_CRAB_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="KNIGHTS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        KNIGHTS_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="KNOWLEDGE_DEMON_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        KNOWLEDGE_DEMON_BOSS.append(new_specific)
    
    elif encounter.name.split(".")[1]=="LAGAVULIN_MATRIARCH_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        LAGAVULIN_MATRIARCH_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="LIVING_FOG_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        LIVING_FOG_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="LOUSE_PROGENITOR_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        LOUSE_PROGENITOR_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="MAWLER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        MAWLER_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="MECHA_KNIGHT_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        MECHA_KNIGHT_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="MYTES_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        MYTES_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="NIBBITS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        NIBBITS_NORMAL.append(new_specific)
    
    elif encounter.name.split(".")[1]=="NIBBITS_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        NIBBITS_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="OVERGROWTH_CRAWLERS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        OVERGROWTH_CRAWLERS.append(new_specific)
    
    elif encounter.name.split(".")[1]=="OVICOPTER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        OVICOPTER_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="OWL_MAGISTRATE_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        OWL_MAGISTRATE_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="PHANTASMAL_GARDENERS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        PHANTASMAL_GARDENERS_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="PHROG_PARASITE_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        PHROG_PARASITE_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="PUNCH_CONSTRUCT_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        PUNCH_CONSTRUCT_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="QUEEN_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        QUEEN_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="RUBY_RAIDERS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        RUBY_RAIDERS_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SCROLLS_OF_BITING_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SCROLLS_OF_BITING_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SCROLLS_OF_BITING_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SCROLLS_OF_BITING_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SEAPUNK_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SEAPUNK_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SEAPUNK_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SEAPUNK_WEAK.append(new_specific)
    
    elif encounter.name.split(".")[1]=="SEWER_CLAM_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SEWER_CLAM_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SHRINKER_BEETLE_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SHRINKER_BEETLE_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SKULKING_COLONY_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SKULKING_COLONY_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SLIMED_BERSERKER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SLIMED_BERSERKER_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SLIMES_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SLIMES_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SLIMES_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SLIMES_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SLITHERING_STRANGLER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SLITHERING_STRANGLER_NORMAL.append(new_specific)
    
    elif encounter.name.split(".")[1]=="SLUDGE_SPINNER_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SLUDGE_SPINNER_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SLUMBERING_BEETLE_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SLUMBERING_BEETLE_NORMAL.append(new_specific)
    
    elif encounter.name.split(".")[1]=="SNAPPING_JAXFRUIT_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SNAPPING_JAXFRUIT_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SOUL_FYSH_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SOUL_FYSH_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SOUL_NEXUS_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SOUL_NEXUS_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="SPINY_TOAD_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        SPINY_TOAD_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="TERROR_EEL_ELITE":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        TERROR_EEL_ELITE.append(new_specific)
        
    elif encounter.name.split(".")[1]=="TEST_SUBJECT_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        TEST_SUBJECT_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="THE_INSATIABLE_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        THE_INSATIABLE_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="THE_KIN_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        THE_KIN_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="THE_LOST_AND_FORGOTTEN_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        THE_LOST_AND_FORGOTTEN_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="THE_OBSCURA_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        THE_OBSCURA_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="THIEVING_HOPPER_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        THIEVING_HOPPER_WEAK.append(new_specific)
    
    elif encounter.name.split(".")[1]=="TOADPOLES_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        TOADPOLES_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="TUNNELER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        TUNNELER_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="TUNNELER_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        TUNNELER_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="TURRET_OPERATOR_WEAK":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        TURRET_OPERATOR_WEAK.append(new_specific)
        
    elif encounter.name.split(".")[1]=="TWO_TAILED_RATS_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        TWO_TAILED_RATS_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="VANTOM_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        VANTOM_BOSS.append(new_specific)
        
    elif encounter.name.split(".")[1]=="VINE_SHAMBLER_NORMAL":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        VINE_SHAMBLER_NORMAL.append(new_specific)
        
    elif encounter.name.split(".")[1]=="WATERFALL_GIANT_BOSS":
        new_specific = Specific(encounter.deck, encounter.relics, encounter.potions_used, encounter.damage_taken)
        WATERFALL_GIANT_BOSS.append(new_specific)
        
# function which updates specific encounters when given a 'sample' which is a list of runs which is itself a list of encounters
        
def sample_to_sort(sample):
    
    for i in range(len(sample)):
        
        for j in range(len(sample[i])):
            
            update_encounter(sample[i][j])
