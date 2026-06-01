# import helper function
from parsing import run_to_encounters

# load and reformat a bunch of runs into encounters
encounters0 = run_to_encounters("1780101781.json")
encounters1 = run_to_encounters("1780162403.json")
encounters2 = run_to_encounters("1780165215.json")

sample = [encounters0, encounters1, encounters2]

# dump all encounters into a list
all_encounters = []
for run in sample:
    for encounter in run:
        all_encounters.append(encounter)



# nifty module for storing data in files
import pickle

# dump all the encounters into a file
# should create a file named 'test_file.pickle' in the current directory
with open('test_file.pickle', 'wb') as file:
    pickle.dump(all_encounters, file, pickle.HIGHEST_PROTOCOL)
    