from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return = sum

def retreieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    #remove new lines and double quotations
    text = text.replace("\n", " ")
    text = text.replace("\""), "")

    #check whether symbols are included in markov chain
    punctuation = [',' , '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + " ")

    words = text.split(" ")
    #remove empty word
    words = [word for word in words if word != ""]

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            #make new dictionary for this word
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] += 1

    return wordDict

text = str(urlopen(http://pythonscraping.com/files/inaugrationSpeech.txt)
            .read(), 'utf-8')

wordDict = buildWordDict(text)

#genrate new sentences
length = 100
chain = ""
currentWord = "I"
for i in range(0, length):
    chain += currentWord+ " "
    currentWord = retreieveRandomWord(wordDict[currentWord])

print(chain)
