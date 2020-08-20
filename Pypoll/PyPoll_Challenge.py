# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os
import pandas as pd

# Add a variable to load a file from a path.
file_to_load=os.path.join(os.getcwd(),'election_results.csv')
# Add a variable to save the file to a path.
file_to_save = os.path.join(os.getcwd(), "analysis\election_analysis.txt")
#print(file_to_save)

#file_to_load=os.path.join("election_results.csv")

# Step 1: Candidate Options and candidate votes.
# Initialize a total vote counter.
total_votes = 0
candidate_options=[]
candidate_votes={}

# Step 2:Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Step 3:While reading the election results from each row inside the for loop,
#write a script that gets the county name from each row.
#for list
#print("options===================list================")
with open(file_to_load) as election_data:
    reader=csv.reader(election_data)
    for row in reader:
        candidate_options=row[2]

        #print(candidate_options)

  #for dictionary


#print("=========dictionary  ================voting=====================")
with open(file_to_load) as election_data:
    for row in csv.DictReader(election_data):
     candidate_votes=row['County']

     #print(candidate_votes)

# 4a: Write a decision statement that checks that the
# county does not match any existing county in the county list.

if candidate_options not in candidate_options[1]:
     candidate_options_new=[]
else:
      candidate_options['County']

# 4b: Add the existing county to the list of counties.
candidate_options_new.append(candidate_votes)
#print(candidate_options_new)


# 4c: Begin tracking the county's vote count.
with open(file_to_load) as election_data:
    reader=csv.reader(election_data)
    for row in reader:
        total_votes+=1
        county_votes= len(row[1])




    #print("county vote ",county_votes)
    #print("total_votes ",total_votes)
# 5: Add a vote to that county's vote count.

# Save the results to our text file.

# Print the final vote count (to terminal)
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n\n"
    f"County Votes:\n")

#print(election_results, end="")


# 6a: Write a repetition statement to get the county from the county dictionary.

#print("=========dictionary  ================voting=====================")
with open(file_to_load) as election_data:
    for row in csv.DictReader(election_data):
        candidate_votes=row['County']

       # print(candidate_votes)


# 6b: Retrieve the county vote count.
county_votes= len(row['County'])
#print(county_votes)

# 6c: Calculate the percent of total votes for the county.
with open(file_to_load) as election_data:
    for row in csv.DictReader(election_data):
        candidate_votes=row['Candidate']

        candidate_name=candidate_votes[2]

    votes = len(row['Candidate'])
   # print(" ---",votes)

    vote_percentage = float((votes)) / float(total_votes) * 100
    candidate_results = (
    f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")







# Print each candidate's voter count and percentage to the
# terminal.
#print(candidate_results)
#  Save the candidate results to our text file.

# Determine winning vote count, winning percentage, and candidate.
if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

# Print the winning candidate (to terminal)
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
with open(file_to_save, "w") as txt_file:
    txt_file.write(election_results)
    txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)

# Save the winning candidate's name to the text file

















