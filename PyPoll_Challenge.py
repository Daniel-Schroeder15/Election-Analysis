# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of counties
# 3. A dictionary of counties and respective vote count
# 4. Declare a variable that represents the number of votes that a county received
# 5. The percentage of votes each country contributed to election
# 6. Largest County Turnout


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Assign a cariable for the file to load and the path.
uploading_file = os.path.join("Resources\election_results.csv")



# Assign a variable to save the file to a path
saving_file = os.path.join("analysis", "election_results.txt")

# 1. Initialize a total vote counter.
total_votes = 0

candidates = []
# 1. Candidate Dictionary with votes for the value.
candidate_votes = {}

# 2. initate counties list
counties = []

# 3. Dictionary of counties with respective vote count
county_votes = {}

#4. Variable for the number of county votes
c_votes = int

# 5. county percentage
county_percentage = int

# 6. largest county turnout
largest_turnout = ""
largest_county = 0 
largest_percentage = 0

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
    #print(headers)

    #Read each row of data after the header
    for row in file_reader:
        # 1. Add the rows to the total vote count
        total_votes +=1

        # Candadates names from each row
        candidate_name = row[2]

        # County names for each row
        county_name = row[1]

        if candidate_name not in candidates:
            # Add it to the list of candidates
            candidates.append(candidate_name)

             # Begin tracking Candidate's vote count
            candidate_votes[candidate_name] = 0 

        # Adds a vote to the candidate's count
        candidate_votes[candidate_name] += 1
        
        
        if county_name not in counties:
            # Add it to the list of counties
            counties.append(county_name)

            # Begin tracking county's vote count
            county_votes[county_name] = 0 

        # Adds a vote to the county's count
        county_votes[county_name] += 1

# Save the results to text file
with open(saving_file, "w") as text_file:

    # Print the final vote count to the terminal
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print(election_results, end="")
    

    # Save the final vote count to the text file.
    text_file.write(election_results)
    
    county_vote_results = (
        ""
        f"County Votes:\n")
    print(county_vote_results, end="")
    # save the string to text file.
    text_file.write(county_vote_results)
    
    # find the percentage of votes per county by looping through counts
    for county in county_votes:

        # Retrieve vote count for county
        c_votes = county_votes[county]

        # Calculate the percentage of votes
        county_percentage = int(c_votes) / int(total_votes)*100

        # Print the county name and percentage of votes
        county_results = (
            f"{county}: {county_percentage:.1f}% ({c_votes:,})\n")
        print(county_results)

        # save the county's results to the text file.
        text_file.write(county_results)
        
        # Determine largest turnout
        if (c_votes > largest_county) and (county_percentage > largest_percentage):

           # if true then set largest_turnout = c_votes and largest percentage = county percentage
           largest_county = c_votes

           # set largest turnout equal to county name 
           largest_turnout = county

           largest_percentage = county_percentage
            
    largest_county_turnout = (
        
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n")
    print(largest_county_turnout, end="")

    # save the largest turnout result to the text file.
    text_file.write(largest_county_turnout)
            
    # find the percentage of votes per candidate by looping through counts
    # iterate through the candidate list
    for candidate in candidate_votes:

        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]

        # Calculate the percentage of votes
        vote_percentage = int(votes) / int(total_votes)*100

        # Print the candidate name and percentage of votes
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # save the winning candidate's results to the text file.
        text_file.write(candidate_results)


        #determine winning vote count and candidate
        #determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # if true then set winning_count = votes and winnig percent = vote percentage
            winning_count = votes

            # set winning_candidate equal to the candidate's name.
            winning_candidate = candidate

            winning_percentage = vote_percentage
           

        

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # save the winning candidate's results to the text file.
    text_file.write(winning_candidate_summary)







election_data.close()