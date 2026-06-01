
import pickle


# open the file and load the data into a variable
with open('test_file.pickle', 'rb') as file:
    encounters = pickle.load(file)
    
    
# and as you can see we can easily access the encounters!
for enc in encounters:
    print(enc.name)
    print(enc.damage_taken)