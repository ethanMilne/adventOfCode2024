#in this puzzle you have to iterate through a text file and turn it into a long set of lists
#each list has a set of numbers from 5 - 8 digits long
#you have to find out whether the set is "safe" or not
#a set is safe if:
#   the levels are all increasing or all decreasing
#   any two adjacent levels differ by at least one and at most three
#use elif tree to check if each respective list follows the rules

#now on part 2!
#problem dampener can remove one index from each list
#if removing that index means the list is safe, the list now becomes safe
#create a function that iterates through a list and removes each sequential index
#while calling isSafe() on each runthrough to see if the new list is safe

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
        # levelIsSafe = isSafe(lineList)
        levelIsSafe = removeLevels(lineList)
        safetyCount += levelIsSafe



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
         
def removeLevels(lineList):

    levelCounter = 0 #to count how many safe levels there are
    originalTest = isSafe(lineList)# if a level is safe, we don't need to iterate through and remove levels
    if (not originalTest):
        #sequentially remove each index in lineList and test whether isSafe()
        # print("Now you're removing levels")
        lineLength = len(lineList)
        for index in range(lineLength):

            newLineList = []
            for listIndex in lineList: #copy into temp variable so actual list doesn't get changed
                newLineList.append(listIndex)

            print("This is the original line:", lineList)
            print("This is the copied line:", newLineList)
            newLineList.remove(newLineList[index])
            # print("This is the original line:", lineList)
            print("This is the changed line:", newLineList)
            boolean = isSafe(newLineList)
            if boolean:
                levelCounter += 1
                break
    else:# if the original level was actually just safe
        # add one to the level counter and move on
        levelCounter += 1

    return levelCounter



def main():
    print("run your functions with this simple trick")
    safetyCount = fileRunner("puzzleInput.txt")
    print("There are", safetyCount, "safe files")

main()