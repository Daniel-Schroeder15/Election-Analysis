# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
# Assign a cariable for the file to load and the path.
uploading_file = os.path.join("Resources\election_results.csv")



# Assign a variable to save the file to a path
saving_file = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#Canidates
candidates = []

# 1. Candidate Dictionary with votes for the value.
candidate_votes = {}

# Winning Candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(uploading_file) as election_data:
    
    
    # CSV reader specifies delimiter and variable that holds contents
    file_reader = csv.reader(election_data, delimiter=',')

   

    # Read the header row first (skip this step if there is now header)
    headers = next(file_reader)
    print(headers)

    #Read each row of data after the header
    for row in file_reader:
        # 1. Add the rows to the total vote count
        total_votes +=1

        # Candadates names from each row
        candidate_name = row[2]

        if candidate_name not in candidates:
            # Add it to the list of candidates
            candidates.append(candidate_name)

            # Begin tracking Candidate's vote count
            candidate_votes[candidate_name] = 0 

        # Adds a vote to the candidate's count
        candidate_votes[candidate_name] += 1
        
# find the percentage of votes per candidate by looping through counts
# iterate through the candidate list
for candidate in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes)*100
    # Print the candidate name and percentage of votes
    print(f"{candidate}: received {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count and candidate
    #determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage>winning_percentage):
        # if true then set winning_count = votes and winnig percent = 
        # vote percentage
        winning_count = votes
        winnng_percentage = vote_percentage
        # set winning_candidate equal to the candidate's name.
        winning_candidate = candidate

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)




print(total_votes)
#369711

print(candidates)

print(candidate_votes)



election_data.close()