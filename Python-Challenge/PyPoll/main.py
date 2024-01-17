import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#Variable initialization/declaration
idCount = 0
uniqueCandidates = []
candidateOneVotes = 0
candidateTwoVotes = 0
candidateThreeVotes = 0
electionWinner = ""

with open(csvpath, encoding='UTF-8') as csvfile:
    #csv is read
    csvreader = csv.reader(csvfile, delimiter=',')
    #header is stored
    csv_header = next(csvreader)
    
    for row in csvreader:
        #Total votes calculated
        idCount += 1
        #Candidate total votes calculated
        if row[2] not in uniqueCandidates:
            uniqueCandidates.append(row[2])
        if row[2] == uniqueCandidates[0]:
            candidateOneVotes += 1
        elif row[2] == uniqueCandidates[1]:
            candidateTwoVotes += 1
        elif row[2] == uniqueCandidates[2]:
            candidateThreeVotes += 1
            
#Candidate vote percentage calculated
candidateOnePercent = round(100*candidateOneVotes/idCount,3)
candidateTwoPercent = round(100*candidateTwoVotes/idCount,3)
candidateThreePercent = round(100*candidateThreeVotes/idCount,3)

#Winner determined
if max(candidateOneVotes,candidateTwoVotes,candidateThreeVotes) == candidateOneVotes:
    electionWinner = uniqueCandidates[0]
elif max(candidateOneVotes,candidateTwoVotes,candidateThreeVotes) == candidateTwoVotes:
    electionWinner = uniqueCandidates[1]
elif max(candidateOneVotes,candidateTwoVotes,candidateThreeVotes) == candidateThreeVotes:
    electionWinner = uniqueCandidates[2]

#Remainder of code used to export analysis to txt file
output = f"""Election Results
-------------------------
Total Votes: {idCount}
-------------------------
{uniqueCandidates[0]}: {candidateOnePercent}% ({candidateOneVotes})
{uniqueCandidates[1]}: {candidateTwoPercent}% ({candidateTwoVotes})
{uniqueCandidates[2]}: {candidateThreePercent}% ({candidateThreeVotes})
-------------------------
Winner: {electionWinner}
-------------------------
"""

print(output)

with open('analysis/PyPollResults.txt','w') as results:
    results.write(output)
