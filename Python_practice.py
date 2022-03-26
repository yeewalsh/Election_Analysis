print("Practice Campaign Data")
print("Lists of Dictionaries")

#creating list of counties
counties = ["Arapahoe", "Denver", "Jefferson"]

#creating list of dictionaries of county data
voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})

print(voting_data)

#Add El Paso in 2nd position:

voting_data.insert(1,{"county":"El Paso","registered_voters":461149})

print(voting_data)

#remove Arapahoe data. No built-in keyword to remove from list of dictionaries
for index in range(len(voting_data)):
    if voting_data[index]['county'] == 'Arapahoe':
        del voting_data[index]
        break

print(voting_data)

#reverse list items 
voting_data.reverse()



print(voting_data)

#Add arapahoe back
voting_data.append({'county':'Arapahoe','registered_voters':422829})

print("Final Version after changes")
print(voting_data)

#conditionals

#how many votes did you get?
my_votes = int(input("How many votes did you get in the election?"))
#total voes in election
total_votes = int(input("What is the total number of votes in the election?"))
#calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("You received " + str(percentage_votes)+"5 of the total votes")

if counties[1] == "Denver":
    print(counties[1])

#practice with if-else statments
temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC.")
else: 
    print("Open the windows.")

#practice w/ nested ifs
#What is the score?
score = int(input("What was your score?"))
if score >= 90:
    print("You got an A!")
else:
    if score >= 80:
        print("You got a B")
    else: 
        if score >= 70:
            print("You got a C")
        else: 
            if score >= 60:
                print("You got a D")
            else: 
                print("You got an F")

#combine this code using elif:
score = int(input("What was your score?"))
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
elif score >= 60:
    print("You got a D")
else: 
    print("You got an F")


# Import the datetime module
import datetime
# Use the now() attribute on the datetime class to get the present time. 
# or use the abreviated alias dt for datetime module. 
now = datetime.datetime.now()
#print the present time
print("The time right now is ", now)


