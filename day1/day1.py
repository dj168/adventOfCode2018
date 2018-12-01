# Here are other example situations:

# +1, +1, +1 results in  3
# +1, +1, -2 results in  0
# -1, -2, -3 results in -6
# Starting with a frequency of zero, 
# what is the resulting frequency after all of 
#the changes in frequency have been applied?

def getFinalFrequency(arr):
    numList = [int(x) for x in arr]
    return sum(numList)

def readFileToList(fileName):
    f = open(fileName, 'r')
    x = f.read().splitlines()
    f.close()
    return x

def getFirstRepeatedFrequency(arr):
    freqSeen = set()
    freqSeen.add(0)
    numList = [int(x) for x in arr]
    total = 0
    while True:
        for elem in numList:
            total += elem
            if total in freqSeen:
                return total
            freqSeen.add(total)



freqArr = readFileToList('input.txt')
print(getFinalFrequency(freqArr))
print(getFirstRepeatedFrequency(freqArr))