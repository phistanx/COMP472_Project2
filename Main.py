import Vocabulary
import gram
from collections import Counter


def countWords(dictionary):
    count = 0
    for key, value in dictionary.items():
        count += value
    return count


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

for i in Vocabulary.read():
    # print(i.message)
    whichGram = 2
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

esList = (Counter(esList))
enList = (Counter(enList))
ptList = (Counter(ptList))
euList = (Counter(euList))
caList = (Counter(caList))
glList = (Counter(glList))

enWords = countWords(enList)
esWords = countWords(esList)
ptWords = countWords(ptList)
euWords = countWords(euList)
caWords = countWords(caList)
glWords = countWords(glList)

totalTweet = enCount + esCount + ptCount + euCount + caCount + glCount
enTweetProb = enCount / totalTweet
esTweetProb = esCount / totalTweet
ptTweetProb = ptCount / totalTweet
euTweetProb = euCount / totalTweet
caTweetProb = caCount / totalTweet
glTweetProb = glCount / totalTweet

# i go to school
test = 'iamcool'
if whichGram == 1:
    enScore = enTweetProb
    for i in test:
        enScore += int(enList.get(i, 0)) / enWords
    print("======")
    print(enScore)

    esScore = esTweetProb
    for i in test:
        esScore += int(esList.get(i, 0)) / esWords
    print("======")
    print(esScore)

    ptScore = ptTweetProb
    for i in test:
        ptScore += int(ptList.get(i, 0)) / ptWords
    print("======")
    print(ptScore)

    euScore = euTweetProb
    for i in test:
        euScore += int(euList.get(i, 0)) / euWords
    print("======")
    print(euScore)

    caScore = caTweetProb
    for i in test:
        caScore += int(caList.get(i, 0)) / caWords
    print("======")
    print(caScore)

    glScore = glTweetProb
    for i in test:
        glScore += int(glList.get(i, 0)) / glWords
    print("======")
    print(glScore)

if whichGram == 2:
    test = ['ia', 'am', 'mc','co','oo','ol']
    enProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in enList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        enProb *= int(enList.get(i, 0)) / firstCharProb
    print(enProb)
# print(Counter(enList))
# print(Counter(esList))
# print(Counter(ptList))
# print(Counter(euList))
# print(Counter(caList))
# print(Counter(glList))
#
# print(enWords)
# print(esWords)
# print(ptWords)
# print(euWords)
# print(caWords)
# print(glWords)
#
# print("=========")
#
# print(enCount)
# print(esCount)
# print(ptCount)
# print(euCount)
# print(caCount)
# print(glCount)
# en ng gl
#
# string x = split(gl)
# x[0] = e
# int y;
# for i in map:
#     if x[0] == i[0]:
#         y += i.value
