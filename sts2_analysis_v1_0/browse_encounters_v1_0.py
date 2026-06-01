
import pickle


# takes an encounter id string (ex: "BYRDONIS_ELITE")
# returns a list of all encounters in dataset with that id
def get_encounters(encounter_type):
    
    encounters = []
    
    with open('{}.pickle'.format(encounter_type), 'rb') as file:
        while True:
            try:
                encounter = pickle.load(file)
                encounters.append(encounter)
            except EOFError:
                break
    return encounters
            


# example
f = 'KAISER_CRAB_BOSS'

krabs = get_encounters(f)

print(krabs[0].damage_taken)
print(krabs[1].relics)