#in this puzzle you have a large text file with two columns
#You have to find the similarity score between the two columns
#iterate through the left column and count how many times the current number
#appears in the right list
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


    #iterate throug the left list and count how many times the current number appears in the
    #right list
    #To calculate similarity: multiply current number by how many times it appears
    #add that number to the current similarity score
    totalSimilarityScore = 0
    counter = 0
    for item in listOne:
        itemCount = listTwo.count(item)
        similarity = item * itemCount
        totalSimilarityScore += similarity
        counter += 1
    
    #now you should have the total distance so return it and you're all done
    return totalSimilarityScore


def main():
    totalSimilarityScore = workLists("puzzleInput.txt")
    print("The total distance in between the two lists is", totalSimilarityScore)

    # string = "value1     value2"
    # print(string)
    # string = string.split()
    # print(string)


main()