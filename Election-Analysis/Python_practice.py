print ("Hello World")
voting_data = []
voting_data.append({"County":"Arapahoe", "registered_voters": 422829})
voting_data.append({"County":"Denver", "registered_voters": 463353})
voting_data.append({"County":"Jefferson", "registered_voters": 432438})

voting_data.insert(1,({'County':'El Paso', 'registered_voters':461149}))

voting_data.pop(0)
{'County': 'Arapahoe', 'registered_voters': 422829}

voting_data.pop(1)
{'County': 'Denver', 'registered_voters': 463353}
voting_data.append({"County":"Denver", "registered_voters": 463353})
voting_data.append({"County":"Arapahoe", "registered_voters": 422829})
voting_data

counties = ["Arapahoe", 'Denver','Jefferson']
if counties[1] == 'Denver':
    print(counties[1])


# temperature = int (input("What is the temperature outside?"))
# #int(converting the user input data typer from a string to an intger)
# if temperature > 80: 
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# #nested if-else statments
# #example is grading score A, B, C, D, F
# #what is the score?
# score = int(input("What is your test score?"))

# #determine the grade using nested if else statements
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B')
#     else:
#         if score>=70:
#             print ('Your grade is a C')
#         else:
#             if score>=60:
#                 print ('Your grade is a D')
#             else:
#                 print('Your grade is an F')

# #if-elif-else statements for same grading codes
# #what is the score?
# score = int(input('What is your test score?'))
# # determine the grade
# if score >=90:
#     print("Your score is an A")
# elif score >= 80:
#     print('Your score is a B')
# elif score >= 70: 
#     print('Your score is a C')
# elif score >=60:
#     print('Your score is a D')
# else:
#     print('Your score is an F')
# #cleaner code to write... easier to read. length of the horizontal nested else - if statment will give you and indicator to use nested or (if elif else)

counties = ["Arapahoe","Denver", "Jerfferson"]
if "El Paso" in counties:
    print ("El Paso is in the list of counties.")
else:
    print ('El Paso is not in the list of counties.')
#. The 
# and operator = Evaluates two Boolean expressions into one compound expression. The compound expression is true if both Boolean expressions are true. If one of the expressions is false, then the compound expression is false

# or operator = Ealuates two Boolean expressions into one compound expression. The compound expression is true if either Boolean expression is true.
# # If one of the expressions is false, then the compound expression is true. If both expressions are false, then the compound expression is false

# not operator = evaluates a Boolean expression. the expression is true if the conditional is False


# for looop by iterating through list of counties
for county in counties:
    print(county)

#range function for iterating through list 
# for i in range(len(counties)):
#     print(counties[i])
    
#a variable being used to iterate through a for loop is chosen arbirtatily and could be anything.

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for loop to get only the keys from the dictionary
# for county in counties_dict:
#     print(county)
for county in counties_dict.keys():
    print (county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
    
for county_dict in voting_data:
    print (county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

#nested loop to retieve only the values from each dictionary
for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)


#this retrieves the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# print (f"I REceived {my_votes / total_votes * 100}% of the total votes.")

##for county, voters in counties_dict.items():
    print(f"The {county} county has")


# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You recieved {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes. ")

#.2f equals two decimal places (f = float)
# print(message_to_candidate)
