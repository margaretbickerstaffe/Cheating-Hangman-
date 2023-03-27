#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:46:23 2023

@author: maggiebickerstaffe
"""
#Running Total 
alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
dictionary = []
wordsToPlay = []
topLetters = {}
applicable = False
guesses = False
gameOver = False
stillPlaying = True


with open("dictionary.txt") as file:
    for line in file:
        dictionary.append(line.strip())

def displayWordsLeft():
    print("Words Left: ", len(wordsToPlay))
        
def blankDisplayWord(): 
    i = 0
    word = ""
    while i < wordLength:
        word += "_ "
        i += 1
    return word
    
def guess():        
    userGuess = input("\nGuess a letter: ")
    return userGuess

def groupFamilies(letter): 
    familiesSingularPresence = {}
    occurances =[]
    multipleOccurences = []
    for word in wordsToPlay:
        if (word.count(letter) <= 1):
            occurances.append(word.find(letter))
        else:
            indexes = []
            while(word.find(letter)!= -1):
                indexes.append(word.index(letter))
                word=word.replace(letter,"_",1)
            multipleOccurences.append(indexes)
            
    i = -1
    while i < wordLength:
        count = 0
        for occurance in occurances:
            if (i == occurance):
                count += 1
        familiesSingularPresence[i] = count
        i+=1
    maxPosition = -1
    maxCount = 0
    for position in familiesSingularPresence:
        if (familiesSingularPresence[position] > maxCount):
            maxPosition = position
            maxCount = familiesSingularPresence[position]
    for indexes in multipleOccurences:
        if (multipleOccurences.count(indexes) > maxCount):
            maxPosition = indexes
            maxCount = multipleOccurences.count(indexes)
    
    return maxPosition

def eliminateWordsByLength():
    for word in dictionary: 
        if (len(word) == wordLength):
            wordsToPlay.append(word)

def eliminateWords(maxPosition, guess):
    if (isinstance(maxPosition, int)):
        wordList = wordsToPlay.copy()
        for word in wordList:
            if (word.find(guess) != maxPosition):
                wordsToPlay.remove(word)
    else:
        wordList = wordsToPlay.copy()
        for index in maxPosition:
            for word in wordsToPlay:
                if (word[index] != guess):
                    wordsToPlay.remove(word)

def storeGuesses(guessedLetter, maxPosition):
    topLetters[guessedLetter] = maxPosition

def generateDisplayWord(wordLength):
    i = 0
    word = ""
    while i < wordLength:
        word += "_"
        i += 1
    for letter in topLetters:
        maxLetter = topLetters[letter]
        if (isinstance(maxLetter, int)):
            if (maxLetter != -1):
                word = word[:maxLetter] + letter + word[maxLetter + 1:]
        else:
            for num in maxLetter:
                word = word[:num] + letter + word[num + 1:]
    displayWord = ""
    for letter in word:
        letter += " "
        displayWord += letter
    return "\n" + displayWord

def displayAlphabet(guessedLetter):
    alphabetList.remove(guessedLetter)
    alphabetString = ""
    for letter in alphabetList:
        alphabetString += letter
    return alphabetString

def runningTotal():
    seeList = input("Do you want to see a running total of the number of words remaining (Y/N): ")
    return seeList

def checkForWin(displayWord):
    if (displayWord.find("_") == -1):
        return True
    
def lostMessage():
    print("\nSorry you lost. The word was " + wordsToPlay.pop() + ".")
    
    
def wonMessage():
    print("\nYou won!")

def stillPlaying():
    continueGame = input("\nDo you want to keep playing(Y/N): ")
    if (continueGame == "Y"):
        return True
    return False

while stillPlaying:    
    while not applicable:
        wordLength  = input("Enter a word length: ")
        wordLength = int(wordLength)
        for word in dictionary:
            if (len(word) == wordLength):
               applicable = True;
        
    
    while not guesses:
        guessNum = input("Enter a number of guesses: ")
        guessNum = int(guessNum)
        if (guessNum > 0):
            guesses = True;
    
    displayWords = runningTotal()
       
    print("\nSTART GAME\n")
    
    print("Number of guesses left: ", guessNum)
    eliminateWordsByLength()
    
    word = blankDisplayWord()
    print(word) 
    print("Remaining letters: " + alphabet)
    
    
    while not gameOver:
        if (displayWords == "Y"):
            displayWordsLeft()
        guessedLetter = guess() 
        while (alphabetList.count(guessedLetter) == 0):
            guessedLetter = guess() 
        guessNum -= 1
        maxPosition = groupFamilies(guessedLetter)
        storeGuesses(guessedLetter, maxPosition)
        displayWord = generateDisplayWord(wordLength)
        print(displayWord)
        eliminateWords(maxPosition, guessedLetter)
        print("Number of guesses left: ", guessNum)
        alphabetString = displayAlphabet(guessedLetter)
        print("Remaining letters: " + alphabetString)
        won = checkForWin(displayWord)
        if (won):
            gameOver = True
        if (guessNum == 0):
            gameOver = True
    
    if gameOver:
        applicable = False
        guesses = False
        gameOver = False
        alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
        if (won):
            wonMessage()
            if not (stillPlaying()):
                stillPlaying = False
        else:
            lostMessage()
            if not (stillPlaying()):
                stillPlaying = False