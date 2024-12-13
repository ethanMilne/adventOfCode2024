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
        levelIsSafe = isSafe(lineList)
        if(levelIsSafe):
            safetyCount += 1



    file.close()

    return safetyCount


def isSafe(lineList):

    listLength = len(lineList)
    direction = lineList[0] - lineList[1] #this num will be negative or positive, showing the direction the
                                          #String should be going the whole time
    if direction < 0:
        direction = -1
    elif direction > 0:
        direction = 1
    safety = True #we will test against this variable

    i = 0
    #this loop iterates through the lineList passed in through the variable
    for i in range(listLength - 1):
        if((abs(lineList[i] - lineList[i+1]) < 1) or
            (abs(lineList[i] - lineList[i+1]) > 3)):
            safety = False
            break
        if((lineList[i] - lineList[i+1] < 0 and direction != -1) or
           (lineList[i] - lineList[i+1] > 0 and direction != 1)):
            safety = False
            break
    return safety
         

def main():
    print("run your functions with this simple trick")
    safetyCount = fileRunner("puzzleInput.txt")
    # safetyCount = fileRunner("exampleInput.txt")
    print("There are", safetyCount, "safe files")

main()