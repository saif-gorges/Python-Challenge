
#library imports
import os  
import csv

#set filepath 
filepath = os.path.join("Resource","budget_data.csv")
print(filepath)
outputfilepath = os.path.join("Analysis","pybankanalysis.txt")

#open and read file
with open(filepath) as file: 
    csvreader = csv.reader(file)
    header = next(csvreader)

    #set variables
    total_months = 0
    total = 0
    average = 0
    profit_list = []
    difference_list = []
    highest_profit = []
    lowest_profit = []

    #create profit and difference list
    for row in csvreader:
        
        total_months = total_months +1
        total = total + int(row[1])
        profit_list.append(row[1])
    
    for profit in range(len(profit_list)):
        if profit == 0:
            continue
        else:
            difference_list.append(int(profit_list[profit]) - int(profit_list[profit - 1]))

    #calculate summary variables
    average = sum(difference_list)/len(difference_list)
    highest_profit = max(difference_list)
    lowest_profit = min(difference_list)

    #print summary variables in terminal
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average:.2f}")
    print(f"Greatest Increase in Profits : ${highest_profit}")
    print(f"Greatest Decrease in Profits : ${lowest_profit}")

result = [("Total Months: ",total_months),("Total: $",total),("Average Change: $",average),("Greatest Increase in Profits : $",highest_profit),("Greatest Decrease in Profits : $",lowest_profit)]
    
#open output file
with open(outputfilepath, 'w') as file:
    csvwriter = csv.writer(file)

    #print summary variables in txt file
    csvwriter.writerows(result)