import Vocabulary
import gram
from collections import Counter

enList = []
esList = []
euList = []
ptList = []
caList = []
glList = []
for i in Vocabulary.read():
    # print(i.message)
    whichGram = 1
    arr = gram.gram(i.message, whichGram)
    if i.language == 'en':
        enList += arr
    elif i.language == 'es':
        esList += arr
    elif i.language == 'ca':
        caList += arr
    elif i.language == 'pt':
        ptList += arr
    elif i.language == 'eu':
        euList += arr
    elif i.language == 'gl':
        glList += arr

print(Counter(esList))
print(Counter(enList))
print(Counter(ptList))
print(Counter(euList))
print(Counter(caList))
print(Counter(glList))
