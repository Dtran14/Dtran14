#method which reads the trade volumes and returns two lists
def readFile(filename):
    try:
        day,trades=[[],[]]
        fil = open(filename)
        lines=fil.readlines()
        #iterate the read lines
        for line in lines:
            #split the lines and append the values to list
            a,b=line.split()
            day.append(a)
            trades.append(float(b))
        #finally return the list
        return day,trades
    except Exception as ex:
        print(ex)
        print("File {} not found , try again".format(filename))
        exit(0)

#methdo to get the max and min trades Index
def getMaxMinTrades(trades):
    #initially assume max and min are at index 0
    maximum,minimum=[0,0]
    for t in range(len(trades)):
        if trades[t] >trades[maximum]:
            maximum=t
        if trades[t] <trades[minimum]:
            minimum=t  
    #return the index
    return maximum,minimum

#methdo to find the average trades
def getAverageTrades(days,trades):
    feb,march=[[],[]]
    for i in range(len(days)):
        if days[i].split("/")[1]=="02":
            feb.append(float(trades[i]))
        else:
            march.append(float(trades[i]))
    return sum(feb)/len(feb),sum(march)/len(march)
#make call to get the days and trades
days = trades = open("AAPL.txt", "r")
foo = days,trades.read()
print(foo)
quit()
#find the maximum and minimum trade volumnes
maximum,minimum= getMaxMinTrades(trades)
#display the result
print("{} has the maximum trade value of {}".format(days[maximum],trades[maximum]))
print("{} has the minimum trade value of {}".format(days[minimum],trades[minimum]))

#make method call to get getAverageTrades
febAvg,marchAvg = getAverageTrades(days,trades)
print("The average trade volume of February is {}".format(febAvg))
print("The average trade volume of March is {}".format(marchAvg))
#finally display the greatest average
print("AAPL has higher trading volume in {}.".format("March" if marchAvg > febAvg else "February"))
