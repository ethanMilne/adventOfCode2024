#in this puzzle you have to iterate through a text file and turn it into a long set of lists
#each list has a set of numbers from 5 - 8 digits long
#you have to find out whether the set is "safe" or not
#a set is safe if:
#   the levels are all increasing or all decreasing
#   any two adjacent levels differ by at least one and at most three
#use elif tree to check if each respective list follows the rules

def fileRunner(fileName):
    print("run your files with this simple trick")
    #count how many lists are safe
    safetyCount = 0
    file = open(fileName)

    #Change each line into its own separate list
    for line in file:
        # print(line)
        lineList = line.split()
        listLength = len(lineList)
        #turns each item of the list into an int for later
        for item in range(listLength):
            lineList[item] = int(lineList[item])

        #iterate through each list and checking how it compares to the rules
        #having different possibilities based on the length of the list :/
        if listLength == 5:

            if ((lineList[0] > lineList[1] and lineList[1] > lineList[2] and lineList[2] > lineList[3] and lineList[3] > lineList[4]) or
                (lineList[0] < lineList[1] and lineList[1] < lineList[2] and lineList[2] < lineList[3] and lineList[3] < lineList[4])):
                #This crazy if statement tells if the difference between the levels is at least one and at most three
                if(((abs(lineList[0] - lineList[1]) >= 1 and abs(lineList[0] - lineList[1]) <= 3) and 
                    (abs(lineList[1] - lineList[2]) >= 1 and abs(lineList[1] - lineList[2]) <= 3) and 
                    (abs(lineList[2] - lineList[3]) >= 1 and abs(lineList[2] - lineList[3]) <= 3) and 
                    (abs(lineList[3] - lineList[4]) >= 1 and abs(lineList[3] - lineList[4]) <= 3))):
                    safetyCount += 1

        elif listLength == 6:
            if ((lineList[0] > lineList[1] and lineList[1] > lineList[2] and lineList[2] > lineList[3] and lineList[3] > lineList[4] and lineList[4] > lineList[5]) or
                (lineList[0] < lineList[1] and lineList[1] < lineList[2] and lineList[2] < lineList[3] and lineList[3] < lineList[4] and lineList[4] < lineList[5])):
                if(((abs(lineList[0] - lineList[1]) >= 1 and abs(lineList[0] - lineList[1]) <= 3) and 
                    (abs(lineList[1] - lineList[2]) >= 1 and abs(lineList[1] - lineList[2]) <= 3) and 
                    (abs(lineList[2] - lineList[3]) >= 1 and abs(lineList[2] - lineList[3]) <= 3) and 
                    (abs(lineList[3] - lineList[4]) >= 1 and abs(lineList[3] - lineList[4]) <= 3) and 
                    (abs(lineList[4] - lineList[5]) >= 1 and abs(lineList[4] - lineList[5]) <= 3))):
                    safetyCount += 1

        elif listLength == 7:
            if ((lineList[0] > lineList[1] and lineList[1] > lineList[2] and lineList[2] > lineList[3] and lineList[3] > lineList[4] and lineList[4] > lineList[5] and lineList[5] > lineList[6]) or
                (lineList[0] < lineList[1] and lineList[1] < lineList[2] and lineList[2] < lineList[3] and lineList[3] < lineList[4] and lineList[4] < lineList[5] and lineList[5] < lineList[6])):
                if(((abs(lineList[0] - lineList[1]) >= 1 and abs(lineList[0] - lineList[1]) <= 3) and 
                    (abs(lineList[1] - lineList[2]) >= 1 and abs(lineList[1] - lineList[2]) <= 3) and 
                    (abs(lineList[2] - lineList[3]) >= 1 and abs(lineList[2] - lineList[3]) <= 3) and 
                    (abs(lineList[3] - lineList[4]) >= 1 and abs(lineList[3] - lineList[4]) <= 3) and 
                    (abs(lineList[4] - lineList[5]) >= 1 and abs(lineList[4] - lineList[5]) <= 3) and 
                    (abs(lineList[5] - lineList[6]) >= 1 and abs(lineList[5] - lineList[6]) <= 3))):
                    safetyCount += 1

        elif listLength == 8:
            if ((lineList[0] > lineList[1] and lineList[1] > lineList[2] and lineList[2] > lineList[3] and lineList[3] > lineList[4] and lineList[4] > lineList[5] and lineList[5] > lineList[6] and lineList[6] > lineList[7]) or
                (lineList[0] < lineList[1] and lineList[1] < lineList[2] and lineList[2] < lineList[3] and lineList[3] < lineList[4] and lineList[4] < lineList[5] and lineList[5] < lineList[6] and lineList[6] < lineList[7])):
                if(((abs(lineList[0] - lineList[1]) >= 1 and abs(lineList[0] - lineList[1]) <= 3) and 
                    (abs(lineList[1] - lineList[2]) >= 1 and abs(lineList[1] - lineList[2]) <= 3) and 
                    (abs(lineList[2] - lineList[3]) >= 1 and abs(lineList[2] - lineList[3]) <= 3) and 
                    (abs(lineList[3] - lineList[4]) >= 1 and abs(lineList[3] - lineList[4]) <= 3) and 
                    (abs(lineList[4] - lineList[5]) >= 1 and abs(lineList[4] - lineList[5]) <= 3) and 
                    (abs(lineList[5] - lineList[6]) >= 1 and abs(lineList[5] - lineList[6]) <= 3) and 
                    (abs(lineList[6] - lineList[7]) >= 1 and abs(lineList[6] - lineList[7]) <= 3))):
                    safetyCount += 1


    file.close()

    return safetyCount



def main():
    print("run your functions with this simple trick")
    safetyCount = fileRunner("puzzleInput.txt")
    print("There are", safetyCount, "safe files")

main()