import re
from parse import *
#this puzzle takes a lot of text that is mostly garbage but has some useful information
#iterate through the texts and find the useful information
#mul(3,4) is what we're looking for
#get rid of all spaces, words, and special characters
def multiply(num1,num2):
    product = num1 * num2
    return product

def main():
    print("main function")
    fileToRun = "exampleInput.txt"
    # fileToRun = "puzzleInput.txt"
    finalNumber = fileRunner(fileToRun)
    print("the final number is:", finalNumber)

def fileRunner(fileName):

    total = 0
    listOfMatches = []
    file = open(fileName, 'r')
    fileTxt = file.read()
    file.close()

    print(fileTxt)
    stringToFind = "mul("
    amountOfTimesFound = fileTxt.count(stringToFind)
    tryThis = findall("mul({:d},{:d})","xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    # listOfMatches.append(tryThis)
    print(tryThis)
    # print(tryThis[0])
    x = findall("mul(",fileTxt)
    print(x)
    maybeThis = parse("mul({:d},{:d})",fileTxt)
    print(maybeThis)
    # print(amountOfTimesFound)

    return total

main()