import os
import csv

#declaring variables I will be using
total=0
monthList=[]
valueList=[] 
changeTotal=0

csvpath = os.path.join("Resources", "budget_data.csv") #reading in the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skips the header
    for row in csvreader: 
	    monthList.append(row[0]) #every date is saved as a string to monthList
	    valueList.append(int(row[1])) #every profit/loss is saved as float
	    total=total+int(row[1]) #updating total by every profit/loss

for temp in range(len(valueList)-1): #calulating the difference/change between every month and the next one and adding that to a total
    changeTotal=changeTotal+(valueList[temp+1]-valueList[temp])


months=len(monthList) #returns the length of monthList which is how many months are in the csv File
averageChange=changeTotal/(len(valueList)-1) #returns my changeTotal diveded by the number of months-1 to return the average change
averageChange=round(averageChange,2) #rounding the average change to two decimals
minProfit=min(valueList) #uses the built in min command to reutrn the smallest value in the list
minMonth=monthList[valueList.index(minProfit)] #uses the index command to return what index the smallest value was at, which is the same index as its corresponding month
maxProfit=max(valueList) #repeating what i did for min but for max this time
maxMonth=monthList[valueList.index(maxProfit)]

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: $" +str(total))
print("Average Change: $" +str(averageChange))
print("Greatest Increase in Profits: "+maxMonth+" ($"+str(maxProfit)+")")
print("Greatest Decrease in Profits: "+minMonth+" ($"+str(minProfit)+")")

f = open("KennyDanielsPyBank.txt","w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write("Total Months: " + str(months)+"\n")
f.write("Total: $" +str(total)+"\n")
f.write("Average Change: $" +str(averageChange)+"\n")
f.write("Greatest Increase in Profits: "+maxMonth+" ($"+str(maxProfit)+")\n")
f.write("Greatest Decrease in Profits: "+minMonth+" ($"+str(minProfit)+")\n")
f.close()
