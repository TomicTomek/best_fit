chunksList = [6, 6, 10, 10, 11, 11, 19]
maxCapacity = 71

# prepare base parameters
INV = -1     # invalid
base = []    # [0,  1,  2,  3,  4,  5, ...]

for i in range(len(chunksList)):
    base.append(i)    
    
print (base)


# define functions
"""
Prepare list with indexes up to provided index (upToPosition),
rest is "-1" (INV).
As indexes cannot repeat use basePattern which guarantee this.
"""
def prepareIndexesList(listLength, upToPosition, basePattern = base):
    resultList = list()
    for i in range(listLength):
        resultList.append(INV)
    for i in range(upToPosition + 1):
        resultList[i] = basePattern[i]
    return resultList

"""
Returns max not repetitive value in inputList, 
which can be placed on provided index.
"""
def nextNonRepetitive(inputList, index):
    maxIndex = len(inputList)
    currentValueIndex = inputList[index]
    nextValueIndex = (currentValueIndex + 1) % maxIndex
    listCopy = inputList.copy()
    listCopy[index] = maxIndex     # to mask current value
    
    while nextValueIndex in listCopy:
        nextValueIndex = (nextValueIndex + 1) % maxIndex
        
    return nextValueIndex
        

"""
Increment values in the listToModify starting from back, 
but not increment values marked as invalid "-1" (INV).
Returns True if all listToModify values overflows.
"""
def incrementFromRigthOmitRepetition(listToModify):
    overflow = False
    for i in range(len(listToModify)-1, -1, -1):
        if listToModify[i] != INV:
            nextValue = nextNonRepetitive(listToModify, i)
            if nextValue == listToModify[i]:
                return True
            localOverflow = nextValue < listToModify[i]
            listToModify[i] = nextValue
            
            if localOverflow:
                if i == 0:
                    overflow = True
            else:
                break

    return overflow



############################################################## 
closestResult = 0
closestResultValues = None

for i in range(len(chunksList)):
    isOverflow = False
    actual = prepareIndexesList(len(chunksList), i)
    # print("START, up to position: ", i, ", actual: ", actual)
    while True:
        print("Actual under test: ", actual)
        result = 0
        for actualPosition in actual:
            if actualPosition != INV:
                #print("actualPosition: ", actualPosition)
                result += chunksList[actualPosition]
        print("Test value: ", result)
        
        if result > closestResult and result <= maxCapacity:
            # winner
            closestResult = result
            closestResultValues = actual.copy()
        
        # increment non INV indexes from right with omiting repetition
        isOverflow = incrementFromRigthOmitRepetition(actual)
        if isOverflow:
            #print("Actual overflow: ", actual)
            break


    
winnerValues = list()
for index in closestResultValues:
    if index != INV:
        winnerValues.append(chunksList[index])

winnerValues.sort()
print("\nThe closest result is: ", closestResult,  ", with values: ", winnerValues)
