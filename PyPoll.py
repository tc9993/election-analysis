# 1. The toal number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number ofvotes each candidate won
# 5. Winner of the election based on popular vote

# Import csv
import csv
# Import OS
import os

# Assign variable to load a file from path
file_to_load = os.path.join('Resources' , 'election_results.csv')

# Assign variable to save file to path
file_to_save = os.path.join('Analysis' , 'election_analysis.txt')

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with reader function
    file_reader = csv.reader(election_data)

    # Read and print header row
    headers = next(file_reader)
    print(headers)
    print(file_reader)
