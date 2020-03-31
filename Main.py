import Vocabulary
import gram
from collections import Counter
import math


def countWords(dictionary):
    count = 0
    for key, value in dictionary.items():
        count += value
    return count


def addSmoothValue(languagelist, smooth_value):
    for key, value in languagelist.items():
        languagelist[key] = value + smooth_value


enList = []
esList = []
euList = []
ptList = []
caList = []
glList = []

enCount = 0
esCount = 0
euCount = 0
ptCount = 0
caCount = 0
glCount = 0

# Create the dictionary of words and their count
for i in Vocabulary.read():
    whichGram = 2
    smooth_value = 0.1
    # create a dictionary of uni/bi/tri-gram
    arr = gram.gram(i.message, whichGram)
    if i.language == 'en':
        enCount += 1
        enList += arr
    elif i.language == 'es':
        esCount += 1
        esList += arr
    elif i.language == 'ca':
        caCount += 1
        caList += arr
    elif i.language == 'pt':
        ptCount += 1
        ptList += arr
    elif i.language == 'eu':
        euCount += 1
        euList += arr
    elif i.language == 'gl':
        glCount += 1
        glList += arr

# use Counter library to create dictionary with unique keys (character) and the count of the keys
esList = (Counter(esList))
enList = (Counter(enList))
ptList = (Counter(ptList))
euList = (Counter(euList))
caList = (Counter(caList))
glList = (Counter(glList))

# add the smooth value to each value of the key in the list
addSmoothValue(esList, smooth_value)
addSmoothValue(enList, smooth_value)
addSmoothValue(ptList, smooth_value)
addSmoothValue(euList, smooth_value)
addSmoothValue(caList, smooth_value)
addSmoothValue(glList, smooth_value)

# Count how many words there is in that language
enWords = countWords(enList)
esWords = countWords(esList)
ptWords = countWords(ptList)
euWords = countWords(euList)
caWords = countWords(caList)
glWords = countWords(glList)

# create the probability of each language for a tweet
totalTweet = enCount + esCount + ptCount + euCount + caCount + glCount
enTweetProb = enCount / totalTweet
esTweetProb = esCount / totalTweet
ptTweetProb = ptCount / totalTweet
euTweetProb = euCount / totalTweet
caTweetProb = caCount / totalTweet
glTweetProb = glCount / totalTweet

# TODO change this to read value from file
test = 'iamcool'
# when gram = 1, apply bayes formula with log of 10
if whichGram == 1:
    enScore = enTweetProb
    for i in test:
        enScore += math.log(((enList.get(i, smooth_value)) / enWords), 10)
    print("======")
    print(enScore)

    esScore = esTweetProb
    for i in test:
        esScore += math.log(((esList.get(i, smooth_value)) / esWords), 10)
    print("======")
    print(esScore)

    ptScore = ptTweetProb
    for i in test:
        ptScore += math.log(((ptList.get(i, smooth_value)) / ptWords), 10)
    print("======")
    print(ptScore)

    euScore = euTweetProb
    for i in test:
        euScore += math.log(((euList.get(i, 0)) / euWords), 10)
    print("======")
    print(euScore)

    caScore = caTweetProb
    for i in test:
        caScore += math.log(((caList.get(i, smooth_value)) / caWords), 10)
    print("======")
    print(caScore)

    glScore = glTweetProb
    for i in test:
        glScore += math.log(((glList.get(i, smooth_value)) / glWords), 10)
    print("======")
    print(glScore)

# calculate probability when gram is 2 for each language
# for loop is to find the probability of the first character of the bigram
if whichGram == 2:
    # TODO change this to dynamic value read from file
    test = ['ia', 'am', 'mc', 'co', 'oo', 'ol']

    enProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in enList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        enProb += math.log((enList.get(i, smooth_value)) / firstCharProb, 10)
    print('En value: ')
    print(enProb)

    esProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in esList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        esProb += math.log((esList.get(i, smooth_value)) / firstCharProb, 10)
    print('Es value: ')
    print(esProb)

    ptProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in ptList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        ptProb += math.log((ptList.get(i, smooth_value)) / firstCharProb, 10)
    print('Pt value: ')
    print(ptProb)

    euProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in euList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        euProb += math.log((euList.get(i, smooth_value)) / firstCharProb, 10)
    print('Eu value: ')
    print(euProb)

    caProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in caList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        caProb += math.log((caList.get(i, smooth_value)) / firstCharProb, 10)
    print('Ca value: ')
    print(caProb)

    glProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in glList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        glProb += math.log((glList.get(i, smooth_value)) / firstCharProb, 10)
    print('Gl value: ')
    print(glProb)
