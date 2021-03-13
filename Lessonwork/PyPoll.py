# 1. The toal number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number ofvotes each candidate won
# 5. Winner of the election based on popular vote

# Import csv
import csv
# Import OS
import os

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percent = 0

# Initialize a total vote counter
total_votes = 0

# Create Candidates List
candidate_options = []

# Create empty candidate dictionary
candidate_votes = {}

# Assign variable to load a file from path
file_to_load = os.path.join('Lessonwork', 'Resources' , 'election_results.csv')

# Assign variable to save file to path
file_to_save = os.path.join('Analysis' , 'election_analysis.txt')

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # Read the file object with reader function
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidate names
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            
            #Add candidate to list of options
            candidate_options.append(candidate_name)

            #Begin counting that candidates votes
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the total votes
print(total_votes)

# Print candidate list
print(candidate_options)

# Print candidate vote dictionary
print(candidate_votes)

# Go through candidate list
for candidate_name in candidate_votes:
    
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes

    vote_percentage = float(votes) / float(total_votes) * 100

    # Print the candidate name and percent of votes
    print(f"{candidate_name}: received {vote_percentage : .1f}% of the vote.") 

    # Determine if the vote count calculated is greater than the winning_count
    if votes > winning_count and vote_percentage > winning_percent:

        # Set winning count, winning percent, and winning candidate
        winning_count = votes
        winning_percent = vote_percentage
        winning_candidate = candidate_name

print(f"{winning_candidate} has won the election with {winning_count:,} votes, or {winning_percent:.1f}% of the total vote.")