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

# assign a variable to create the file for the analysis
file_to_create = os.path.join('analysis', 'election_analysis.txt')

# use the with statement to open the file as a text file.
with open(file_to_create, 'w') as outfile:

    # write three counties to the new outfile
    outfile.write('Counties in the Election\n')
    outfile.write('----------------------------\n')
    outfile.write('Arapahoe\nDenver\nJefferson')

# open the file to read the data
with open(file_to_load) as election_data:
    print(election_data)

    # Read election_data with reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the csv file.
    #for row in file_reader:
     #   print(row)


#Find the total number of all votes cast

#make a list of the names of all candidates who recieved votes

#get the vote count for each candidate

#calculate the percentage won per candidate

#the winner receives the highest percentage of votes

