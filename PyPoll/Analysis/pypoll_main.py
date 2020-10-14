
#library imports
import os  
import csv

#set filepath 
filepath = os.path.join("Resource","election_data.csv")
print(filepath)
outputfilepath = os.path.join("Analysis","pypollanalysis.txt")

#open and read file
with open(filepath) as file: 
    csvreader = csv.reader(file)
    header = next(csvreader)

    #set variables
    total_votes = 0
    total_candidates = []
    candidate_votes = 0
    candidate_list = []
    votes_list = []
    percent = 0
    percent_votes = []

    #create candidate list
    for row in csvreader:
        
        total_votes = total_votes + 1
        total_candidates.append(row[2])

        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    #calculate votes for each candidate
    for i in range(len(candidate_list)):
        for j in range(len(total_candidates)):
            if candidate_list[i] == total_candidates[j]:
                candidate_votes = candidate_votes + 1
        votes_list.append(candidate_votes)
        candidate_votes = 0

    #calculate percentage of votes
    for x in range(len(votes_list)):
        percent = 100*(votes_list[x]/sum(votes_list))
        percent_votes.append(percent)

    #print summary variables in terminal
    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------")
    for y in range(len(candidate_list)):
        print(f"{candidate_list[y]}: {percent_votes[y]:.3f}% ({votes_list[y]})")
        if percent_votes[y] > percent_votes[y-1]:
            winner = candidate_list[y]
    print("---------------------")
    print(f"Winner: {winner}")
    print("---------------------")


    result1 = [("Election Results",),("---------------------",),("Total Votes: ",total_votes),("---------------------",)]
    bar = ("---------------------",)

#open output file
with open(outputfilepath, 'w') as file:
    csvwriter = csv.writer(file)
    
    #print summary variables in txt file
    csvwriter.writerows(result1)
    for p in range(len(candidate_list)):
        result2 = [(candidate_list[p],),(percent_votes[p],) , (votes_list[p])]
        csvwriter.writerow(result2)
    
    #write same results to text file
    csvwriter.writerow(bar)
    result3 = [("Winner :",),(winner)]
    csvwriter.writerow(result3)
    csvwriter.writerow(bar)