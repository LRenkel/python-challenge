import pandas as pd

#import file
data = pd.read_csv('election_data_1.csv')

#create dictionary of Candidates and their total votes 
candidate_dict = dict((data.Candidate.value_counts()))

#Calculate total number of votes in election
total_votes = sum(data.Candidate.value_counts())

#Pull out list of votes for each candidate for use in percentage 
calculation
cand_votes = list(candidate_dict.values())

#create empty percentage list to put in percentage calculations
percentage_list = []

#calculate percentage of total votes for each candidate by iterating 
through list of votes
for x in cand_votes:
    percentage = x / total_votes
    percentage_list.append(percentage) #add to percentage_list

#combine candidate name and votes with percentage
candidate_percentage_list = 
list(zip(candidate_dict.keys(),candidate_dict.values(),percentage_list))

with open('some_results.txt', 'w') as f:
    print("Election Results")
    print("-----------------------")
    print("Total Votes: {}".format(total_votes))
    print("-----------------------")
    for x in candidate_percentage_list:
        _cand, _votes, _pct = x
        print("{:10s}: {:.1%} {:10d} ".format(_cand, _pct, _votes))
        f.write("{:10s}: {:.1%} {:10d} ".format(_cand, _pct, _votes) 
+ "\n")
    print("-----------------------")
    print("Winner: " + candidate_percentage_list[0][0]  + "\n")
    f.write("Winner: " + candidate_percentage_list[0][0]  + "\n")

