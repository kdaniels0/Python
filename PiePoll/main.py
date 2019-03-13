import os
import csv

#declaring variables I will be using
totalVotes=0
candidatesList=[]
voteList=[] 

csvpath = os.path.join("Resources", "election_data.csv") #reading in the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skips the header
    for row in csvreader: 
        totalVotes+=1 #increasing the number of people who voted by 1
        foundthem=False #boolean to find if i updated the list or not
        for x in range(len(candidatesList)): #going through my candidate list to see if that candidate has received any votes yet
            if row[2]==candidatesList[x]:
                voteList[x]=voteList[x]+1
                foundthem=True
        if foundthem==False: #if i didn't find that candidate in my list, add them to said list and give them 1 vote
            candidatesList.append(row[2])
            voteList.append(1)
print("Election Results")
print("-------------------------")
print("Total Votes: "+str(totalVotes))
print("-------------------------")
for x in range(len(candidatesList)):
    print(candidatesList[x]+": "+str('%.3f' % ((voteList[x]/totalVotes)*100))+"% ("+str(voteList[x])+")")
print("-------------------------")
winningVotes=max(voteList)
winningCandidate=candidatesList[voteList.index(winningVotes)]
print("Winner: "+winningCandidate)
print("-------------------------")

f = open("KennyDanielsPyPoll.txt","w")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: "+str(totalVotes)+"\n")
f.write("-------------------------\n")
for x in range(len(candidatesList)):
    f.write(candidatesList[x]+": "+str('%.3f' % ((voteList[x]/totalVotes)*100))+"% ("+str(voteList[x])+")\n")
f.write("-------------------------\n")
f.write("Winner: "+winningCandidate+"\n")
f.write("-------------------------\n")
f.close()