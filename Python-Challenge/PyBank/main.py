import os
import csv

#Variable initialization/declaration
monthCount = 0
money = 0
i = 0
profitLoss = []
changes = []
sumChanges = 0
greatestIncrease = 0
greatestDecrease = 0
greatestIncreaseDate = ""
greatestDecreaseDate = ""
tempCount = 0

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, encoding='UTF-8') as csvfile:
    #csv is read
    csvreader = csv.reader(csvfile, delimiter=',')
    #csv header is stored
    csv_header = next(csvreader)

    for row in csvreader:
        #months are counted
        monthCount += 1
        #Total is calculated
        money += int(row[1])
        #profitLoss list used to create changes list
        profitLoss.append(int(row[1]))
        if i > 0:
            #changes list used to determine greatest loss, greatest increase, and average change
            changes.append(profitLoss[i] - profitLoss[i - 1])
            if changes[tempCount] > greatestIncrease:
                greatestIncrease = changes[tempCount]
                greatestIncreaseDate = row[0]
            elif changes[tempCount] < greatestDecrease:
                greatestDecrease = changes[tempCount]
                greatestDecreaseDate = row[0]
            tempCount += 1
        i += 1
    
    #separate for loop used to create needed averageChange variable
    for i in changes:
        sumChanges += i

    averageChange = round(sumChanges/(monthCount - 1),2)

#remainder of code used to export analysis to txt file
output = f"""Financial Analysis
----------------------------
Total Months: {monthCount}
Total: ${money}
Average Change: ${averageChange}
Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})
Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})
"""

print(output)

with open('analysis/PyBankResults.txt', 'w') as results:
    results.write(output)