import os
os.system('cls')

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
# Open the election results and read the file
with open(uploading_file) as election_data:
    
    
    # CSV reader specifies delimiter and variable that holds contents
    file_reader = csv.reader(election_data, delimiter=',')

   

    # Read the header row first (skip this step if there is now header)
    headers = next(file_reader)
    print(headers)

    #Read each row of data after the header
    for row in file_reader:
       print(row)



election_data.close()