

def checkString(stringToCheck, usedLetters):
    for letter in stringToCheck:
        #if string has any repeating letters in itself
        if stringToCheck.count(letter) > 1:
            return False
        #if letter has already been used
        if letter in usedLetters:
            return False

    return True

    

def findAllCombos(initialString, stringsArray):
    usedLetters = {x for x in initialString}
    allVariations = []

    #Base case: no strings to add
    if len(stringsArray) == 0:
        if len(initialString) == 0:
            return []
        allVariations.append(initialString)
    
    #Base case: if initialString empty, cannot generate a concatenation. else check if can append
    elif len(stringsArray) == 1:
        if len(initialString) == 0:
            return []
        string = stringsArray[0]
        variation = initialString
        if checkString(string, usedLetters):
            variation += string
        allVariations.append(variation)

    #Recursive chunk
    else:
        arrayIndex = 0
        variations = []
        for string in stringsArray:
            variation = initialString
            if checkString(string, usedLetters):
                variation += string

                #slices array with each loop because order does not matter
                #### ("abc", ["yy"]) will return abc which would be fine if initial string is not empty
                variations = findAllCombos(variation, stringsArray[arrayIndex+1:])
                if len(variations) != 0 and variations[0] == variation:
                    if initialString != "":
                        allVariations += variations
                else:
                    allVariations += variations
            arrayIndex += 1

    return allVariations



def task2code(A):
    allCombos = findAllCombos('', A)
    print(allCombos)
    #return length of longest string in list
    if len(allCombos) == 0:
        return 0
    return len(max(allCombos, key=len))

def task2():
    strings = ["abc", "yy"]
    return task2code(strings)

##############
print(task2())