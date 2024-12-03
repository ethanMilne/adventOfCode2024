#in this puzzle you have a large text file with two columns
#You have to sort the two columns into ascending order (smallest to largest, use .sort())
#and the find the distance between the two columns
#make each column a separate list
def workLists(fileName):
    #empty lists to append values into
    listOne = []
    listTwo = []
    
    file = open(fileName)
    file.seek(0)

    for line in file:
        #split two columns into two separate lists
        lineList = line.split()
        listOne.append(int(lineList[0]))
        listTwo.append(int(lineList[1]))
    

    file.close()

    #order the two lists from smallest to largest
    listOne.sort()
    listTwo.sort()

    #now iterate between the ordered list and find the difference between each value
    #you can use absolute value (abs()) to find differences
    counter = 0 #will use to find correct corresponding value from other list
    totalDistance = 0
    for item in listOne:
        distance = abs(item - listTwo[counter])
        totalDistance += distance
        counter += 1
    
    #now you should have the total distance so return it and you're all done
    return totalDistance


def main():
    totalDistance = workLists("puzzleInput.txt")
    print("The total distance in between the two lists is", totalDistance)

    # string = "value1     value2"
    # print(string)
    # string = string.split()
    # print(string)


main()