'''
********** RUN WITH CAUTION **********
THE FIRST TIME YOU RUN THIS FILE, A HECK TON OF PICKLES ARE SPAWNED.
IF YOU RUN IT AGAIN WITHOUT CHANGING THE RUN FILES IN folder_path,
A DUPLICATE OF THOSE SAME ENCOUNTERS WILL BE ADDED TO THE PICKLES.
only run once per sample of runs;
otherwise you must delete the .pickle files and start over
'''

from pathlib import Path
from sorting_v1_0 import sample_to_sort
from parsing_v1_0 import run_to_encounters


# update this path string with the path of the folder containing
#    run .json files that you wish to add to the data set
folder_path = Path('/Users/JHB/Desktop/sts2_analysis_v1_0/runs')

# initialize list of runs
runs = []

# Loop through all items in folder filter for .json files
for file in folder_path.iterdir():
    if file.suffix == '.json':
        
        # convert .json run file to a list of encounters
        encounters = run_to_encounters(file)
        
        # add that run to our list of runs
        runs.append(encounters)

# using this list of runs, sort and dump the encounters into pickle files
sample_to_sort(runs)
