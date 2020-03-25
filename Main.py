import Vocabulary
import gram
from collections import Counter
import math


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
    smooth_value = 0.1
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

for key, value in esList.items():
    esList[key] = value+smooth_value

for key, value in enList.items():
    enList[key] = value+smooth_value

for key, value in ptList.items():
    ptList[key] = value+smooth_value

for key, value in euList.items():
    euList[key] = value+smooth_value

for key, value in caList.items():
    caList[key] = value+smooth_value

for key, value in glList.items():
    glList[key] = value+smooth_value

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
        enScore += math.log(((enList.get(i, smooth_value)) / enWords),10)
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

if whichGram == 2:
    test = ['ia', 'am', 'mc', 'co', 'oo', 'ol']

    enProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in enList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        enProb += math.log((enList.get(i, smooth_value)) / firstCharProb, 10)
    print(enProb)

    esProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in esList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        esProb += math.log((esList.get(i, smooth_value)) / firstCharProb, 10)
    print(esProb)

    ptProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in ptList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        ptProb += math.log((ptList.get(i, smooth_value)) / firstCharProb, 10)
    print(ptProb)

    euProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in euList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        euProb += math.log((euList.get(i, smooth_value)) / firstCharProb, 10)
    print(euProb)

    caProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in caList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        caProb += math.log((caList.get(i, smooth_value)) / firstCharProb, 10)
    print(caProb)

    glProb = 0
    for i in test:
        firstCharProb = 0
        for key, value in glList.items():
            if key[0] == i[0]:
                firstCharProb += int(value)

        glProb += math.log((glList.get(i, smooth_value)) / firstCharProb, 10)
    print(glProb)

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
