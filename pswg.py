# Gabe Clark
# GabeClark99@gmail.com

import sys

### GLOBALS ###
subChars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()')

### FUNCTIONS ###
def genMultiSubstitutionWordlist(masterList, numSubs):
    if numSubs <= 0:
        return list()
    
    singleSubList = genSingleSubstitutionListFromList(masterList)
    masterList = union(masterList, singleSubList)

    multiSubList = genMultiSubstitutionWordlist(masterList, numSubs - 1)
    masterList = union(masterList, multiSubList)

    return masterList

def genSingleSubstitutionListFromList(oldList):
    newList = list()
    for i in oldList:
        newList += genSingleSubtitutionListFromPass(i)
    return newList

def genSingleSubtitutionListFromPass(oldPass):
    passList = list()
    for i in range(0, len(oldPass)):
        for j in range(0, len(subChars)):
            newPass = list(oldPass)
            newPass[i] = subChars[j]
            newPass = toString(newPass)
            passList.append(newPass)
    return passList

def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 | set2
    return list(intersection)

def toString(charArr):
    return ''.join(charArr)

def printList(passList):
    for i in passList:
        print(i)

### MAIN ###
wordlist = genMultiSubstitutionWordlist( [ sys.argv[1] ], int(sys.argv[2]) )
printList( sorted(wordlist) )