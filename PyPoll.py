# practice w/ pseudocode
# open the data file
# Find the total number of all votes cast
# make a list of the names of all candidates who recieved votes
# get the vote count for each candidate
# calculate the percentage won per candidate
# the winner receives the highest percentage of votes

# import the csv and os modules
import csv
import os


# assign a variable to load the data file via the path
file_to_load = os.path.join('Resources', 'election_results.csv')

# assign a variable to save the file to a path for the anlysis
file_to_create = os.path.join('analysis', 'election_analysis.txt')

# initialize a total vote counter
total_votes = 0

# create a list for candidate names
candidate_options = []

# create a dictionary for the votes per candidate
candidate_votes = {}

# initialize a winning count, percentage, and candidate tracker
winning_count = 0
winning_percentage = 0
winning_candidate = ''

# open the election file and read the data
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row using next to exclude it from analysis
    headers = next(file_reader)

    # Print each row in the csv file.
    for row in file_reader:

        # increment total_votes by 1 per row
        total_votes = total_votes + 1

        # get the candidate's name from each row
        candidate_name = row[2]

        # if the candidate name does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # create each candidate as a key in the votes dictionary to count their votes
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's total count
        candidate_votes[candidate_name] += 1

# use the with statement to open the file as a text file.
with open(file_to_create, 'w') as text_file:

    # Print Election results
    election_results = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")
    print(election_results, end="")
    # save election results to new text_file
    text_file.write(election_results)
   
    # loop through the candidates to calculate their percentage of the total vote
    # iterate through the candidate_options to get the candidates name
    for candidate_name in candidate_votes:
        
        # get the votes of the candidate from the candidate_votes dictionary
        votes = candidate_votes.get(candidate_name)

        # calculate the percentage of the votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # save the candidate name and percentage of votes for printing
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # save candidate results to text_file
        text_file.write(candidate_results)

        # If statement to determine which vote / vote percentage is higher than winning count / percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # set the winning count / percentage equal to the votes
            winning_count = votes
            winning_percentage = vote_percentage

            #set the winning_candidate equal to candidate's name
            winning_candidate = candidate_name

    # write three counties to the new text_file
    #text_file.write('Counties in the Election\n')
    #text_file.write('----------------------------\n')
    #text_file.write('Arapahoe\nDenver\nJefferson')
    print('----------------------------\n')
    text_file.write('----------------------------\n')

    # print the winning candidate information
    winning_candidate_summary = (
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    text_file.write(winning_candidate_summary)



#Find the total number of all votes cast  - DONE

#make a list of the names of all candidates who recieved votes - DONE

#get the vote count for each candidate - DONE

#calculate the percentage won per candidate - DONE

#the winner receives the highest percentage of votes - DONE

