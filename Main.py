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

vocabulary = 1
whichGram = 1
smooth_value = 0.1
# accuracy
accuracy_numerator = 0
number_tweet = 0
accuracy_percentage = 0

# precision
es_precision = 0
es_precision_num = 0
es_precision_den = 0

gl_precision = 0
gl_precision_num = 0
gl_precision_den = 0

eu_precision = 0
eu_precision_num = 0
eu_precision_den = 0

pt_precision = 0
pt_precision_num = 0
pt_precision_den = 0

en_precision = 0
en_precision_num = 0
en_precision_den = 0

ca_precision = 0
ca_precision_num = 0
ca_precision_den = 0

# Recall
es_recall = 0
es_recall_num = 0
es_recall_den = 0

gl_recall = 0
gl_recall_num = 0
gl_recall_den = 0

eu_recall = 0
eu_recall_num = 0
eu_recall_den = 0

pt_recall = 0
pt_recall_num = 0
pt_recall_den = 0

en_recall = 0
en_recall_num = 0
en_recall_den = 0

ca_recall = 0
ca_recall_num = 0
ca_recall_den = 0

# F1
eu_f1 = 0
en_f1 = 0
es_f1 = 0
pt_f1 = 0
gl_f1 = 0
ca_f1 = 0

solution_file_name = "trace_" + str(vocabulary) + "_" + str(whichGram) + "_" + str(smooth_value) + ".txt"
solution_file = open(solution_file_name, 'w+', encoding='utf-8')

# Create the dictionary of words and their count
for i in Vocabulary.read("training-tweets.txt"):
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

enScore = math.log(enTweetProb, 10)
esScore = math.log(esTweetProb, 10)
euScore = math.log(euTweetProb, 10)
ptScore = math.log(ptTweetProb, 10)
caScore = math.log(caTweetProb, 10)
glScore = math.log(glTweetProb, 10)

# Evaluate Test tweets
for i in Vocabulary.read("test-tweets-given.txt"):
    print('=====================')
    tweetId = i.tweetId
    language = i.language
    test = gram.gram(i.message, whichGram)
    # i = 439379404574453760	aritzabrodes	es	@AnderDelPozo @PesqueWhite hahaha yo tambien me he quedao pillao ahahha
    # when gram = 1, apply bayes formula with log of 10
    if whichGram == 1:
        for i in test:
            enScore += math.log(((enList.get(i, smooth_value)) / enWords), 10)
            esScore += math.log(((esList.get(i, smooth_value)) / esWords), 10)
            ptScore += math.log(((ptList.get(i, smooth_value)) / ptWords), 10)
            euScore += math.log(((euList.get(i, smooth_value)) / euWords), 10)
            caScore += math.log(((caList.get(i, smooth_value)) / caWords), 10)
            glScore += math.log(((glList.get(i, smooth_value)) / glWords), 10)

    # calculate probability when gram is 2 for each language
    # for loop is to find the probability of the first character of the bigram
    if whichGram == 2:
        enProb = 0
        for i in test:
            firstCharCount = 0
            for key, value in enList.items():
                if key[0] == i[0]:
                    firstCharCount += int(value)

            enProb += math.log((enList.get(i, smooth_value)) / firstCharCount, 10)
        print('En value: ')
        print(enProb)

        esProb = 0
        for i in test:
            firstCharCount = 0
            for key, value in esList.items():
                if key[0] == i[0]:
                    firstCharCount += int(value)

            esProb += math.log((esList.get(i, smooth_value)) / firstCharCount, 10)
        print('Es value: ')
        print(esProb)

        ptProb = 0
        for i in test:
            firstCharCount = 0
            for key, value in ptList.items():
                if key[0] == i[0]:
                    firstCharCount += int(value)

            ptProb += math.log((ptList.get(i, smooth_value)) / firstCharCount, 10)
        print('Pt value: ')
        print(ptProb)

        euProb = 0
        for i in test:
            firstCharCount = 0
            for key, value in euList.items():
                if key[0] == i[0]:
                    firstCharCount += int(value)

            euProb += math.log((euList.get(i, smooth_value)) / firstCharCount, 10)
        print('Eu value: ')
        print(euProb)

        caProb = 0
        for i in test:
            firstCharCount = 0
            for key, value in caList.items():
                if key[0] == i[0]:
                    firstCharCount += int(value)

            caProb += math.log((caList.get(i, smooth_value)) / firstCharCount, 10)
        print('Ca value: ')
        print(caProb)

        glProb = 0
        for i in test:
            firstCharCount = 0
            for key, value in glList.items():
                if key[0] == i[0]:
                    firstCharCount += int(value)

            glProb += math.log((glList.get(i, smooth_value)) / firstCharCount, 10)
        print('Gl value: ')
        print(glProb)

    if whichGram == 3:
        enList2 = []
        enCount2 = 0
        # Create the dictionary of words and their count
        for i in Vocabulary.read():
            whichGram = 2
            smooth_value = 0.1
            # create a dictionary of uni/bi/tri-gram
            arr = gram.gram(i.message, whichGram)
            if i.language == 'en':
                enCount2 += 1
                enList2 += arr

        # use Counter library to create dictionary with unique keys (character) and the count of the keys
        enList2 = (Counter(enList2))

        # add the smooth value to each value of the key in the list
        addSmoothValue(enList2, smooth_value)
        # TODO change this to dynamic value read from file
        test = ['iam']
        enProb = 0
        for i in test:
            # enList2 = BIGRAM list, enList = TRIGRAM list
            firstCharProb = 0
            for key, value in enList2.items():
                if key[0] == i[0]:
                    firstCharProb += int(value)
            # ia
            enProb = math.log((enList2.get(i, smooth_value)) / firstCharProb, 10)

        enProb2 = 0
        for i in test:
            firstCharProb = 0
            for key, value in enList2.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            # am
            enProb2 = math.log((enList2.get(i, smooth_value)) / firstCharProb, 10)
        enProb3 = 0
        for i in test:
            firstCharProb = 0
            for key, value in enList.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            enProb3 += math.log((enList.get(i, smooth_value)) / firstCharProb, 10)

        trigramProb = enProb * enProb2 / enProb3
        print('En value: ')
        print(trigramProb)

        esList2 = []
        esCount2 = 0
        # Create the dictionary of words and their count
        for i in Vocabulary.read():
            whichGram = 2
            smooth_value = 0.1
            # create a dictionary of uni/bi/tri-gram
            arr = gram.gram(i.message, whichGram)
            if i.language == 'es':
                esCount2 += 1
                esList2 += arr

        # use Counter library to create dictionary with unique keys (character) and the count of the keys
        esList2 = (Counter(esList2))

        # add the smooth value to each value of the key in the list
        addSmoothValue(esList2, smooth_value)
        # TODO change this to dynamic value read from file
        test = ['iam']
        esProb = 0
        for i in test:
            # enList2 = BIGRAM list, enList = TRIGRAM list
            firstCharProb = 0
            for key, value in esList2.items():
                if key[0] == i[0]:
                    firstCharProb += int(value)
            # ia
            esProb = math.log((esList2.get(i, smooth_value)) / firstCharProb, 10)

        esProb2 = 0
        for i in test:
            firstCharProb = 0
            for key, value in esList2.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            # am
            esProb2 = math.log((esList2.get(i, smooth_value)) / firstCharProb, 10)
        esProb3 = 0
        for i in test:
            firstCharProb = 0
            for key, value in esList.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            esProb3 += math.log((esList.get(i, smooth_value)) / firstCharProb, 10)

        trigramProb = esProb * esProb2 / esProb3
        print('Es value: ')
        print(trigramProb)

        ptList2 = []
        ptCount2 = 0
        # Create the dictionary of words and their count
        for i in Vocabulary.read():
            whichGram = 2
            smooth_value = 0.1
            # create a dictionary of uni/bi/tri-gram
            arr = gram.gram(i.message, whichGram)
            if i.language == 'pt':
                ptCount2 += 1
                ptList2 += arr

        # use Counter library to create dictionary with unique keys (character) and the count of the keys
        ptList2 = (Counter(ptList2))

        # add the smooth value to each value of the key in the list
        addSmoothValue(ptList2, smooth_value)
        # TODO change this to dynamic value read from file
        test = ['iam']
        ptProb = 0
        for i in test:
            # ptList2 = BIGRAM list, ptList = TRIGRAM list
            firstCharProb = 0
            for key, value in ptList2.items():
                if key[0] == i[0]:
                    firstCharProb += int(value)
            # ia
            ptProb = math.log((ptList2.get(i, smooth_value)) / firstCharProb, 10)

        ptProb2 = 0
        for i in test:
            firstCharProb = 0
            for key, value in ptList2.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            # am
            ptProb2 = math.log((ptList2.get(i, smooth_value)) / firstCharProb, 10)
        ptProb3 = 0
        for i in test:
            firstCharProb = 0
            for key, value in ptList.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            ptProb3 += math.log((ptList.get(i, smooth_value)) / firstCharProb, 10)

        trigramProb = ptProb * ptProb2 / ptProb3
        print('pt value: ')
        print(trigramProb)

        euList2 = []
        euCount2 = 0
        # Create the dictionary of words and their count
        for i in Vocabulary.read():
            whichGram = 2
            smooth_value = 0.1
            # create a dictionary of uni/bi/tri-gram
            arr = gram.gram(i.message, whichGram)
            if i.language == 'eu':
                euCount2 += 1
                euList2 += arr

        # use Counter library to create dictionary with unique keys (character) and the count of the keys
        euList2 = (Counter(euList2))

        # add the smooth value to each value of the key in the list
        addSmoothValue(euList2, smooth_value)
        # TODO change this to dynamic value read from file
        test = ['iam']
        euProb = 0
        for i in test:
            # euList2 = BIGRAM list, euList = TRIGRAM list
            firstCharProb = 0
            for key, value in euList2.items():
                if key[0] == i[0]:
                    firstCharProb += int(value)
            # ia
            euProb = math.log((euList2.get(i, smooth_value)) / firstCharProb, 10)

        euProb2 = 0
        for i in test:
            firstCharProb = 0
            for key, value in euList2.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            # am
            euProb2 = math.log((euList2.get(i, smooth_value)) / firstCharProb, 10)
        euProb3 = 0
        for i in test:
            firstCharProb = 0
            for key, value in euList.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            euProb3 += math.log((euList.get(i, smooth_value)) / firstCharProb, 10)

        trigramProb = euProb * euProb2 / euProb3
        print('eu value: ')
        print(trigramProb)

        caList2 = []
        caCount2 = 0
        # Create the dictionary of words and their count
        for i in Vocabulary.read():
            whichGram = 2
            smooth_value = 0.1
            # create a dictionary of uni/bi/tri-gram
            arr = gram.gram(i.message, whichGram)
            if i.language == 'ca':
                caCount2 += 1
                caList2 += arr

        # use Counter library to create dictionary with unique keys (character) and the count of the keys
        caList2 = (Counter(caList2))

        # add the smooth value to each value of the key in the list
        addSmoothValue(caList2, smooth_value)
        # TODO change this to dynamic value read from file
        test = ['iam']
        caProb = 0
        for i in test:
            # caList2 = BIGRAM list, caList = TRIGRAM list
            firstCharProb = 0
            for key, value in caList2.items():
                if key[0] == i[0]:
                    firstCharProb += int(value)
            # ia
            caProb = math.log((caList2.get(i, smooth_value)) / firstCharProb, 10)

        caProb2 = 0
        for i in test:
            firstCharProb = 0
            for key, value in caList2.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            # am
            caProb2 = math.log((caList2.get(i, smooth_value)) / firstCharProb, 10)
        caProb3 = 0
        for i in test:
            firstCharProb = 0
            for key, value in caList.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            caProb3 += math.log((caList.get(i, smooth_value)) / firstCharProb, 10)

        trigramProb = caProb * caProb2 / caProb3
        print('ca value: ')
        print(trigramProb)

        glList2 = []
        glCount2 = 0
        # Create the dictionary of words and their count
        for i in Vocabulary.read():
            whichGram = 2
            smooth_value = 0.1
            # create a dictionary of uni/bi/tri-gram
            arr = gram.gram(i.message, whichGram)
            if i.language == 'gl':
                glCount2 += 1
                glList2 += arr

        # use Counter library to create dictionary with unique keys (character) and the count of the keys
        glList2 = (Counter(glList2))

        # add the smooth value to each value of the key in the list
        addSmoothValue(glList2, smooth_value)
        # TODO change this to dynamic value read from file
        test = ['iam']
        glProb = 0
        for i in test:
            # glList2 = BIGRAM list, glList = TRIGRAM list
            firstCharProb = 0
            for key, value in glList2.items():
                if key[0] == i[0]:
                    firstCharProb += int(value)
            # ia
            glProb = math.log((glList2.get(i, smooth_value)) / firstCharProb, 10)

        glProb2 = 0
        for i in test:
            firstCharProb = 0
            for key, value in glList2.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            # am
            glProb2 = math.log((glList2.get(i, smooth_value)) / firstCharProb, 10)
        glProb3 = 0
        for i in test:
            firstCharProb = 0
            for key, value in glList.items():
                if key[0] == i[1]:
                    firstCharProb += int(value)
            glProb3 += math.log((glList.get(i, smooth_value)) / firstCharProb, 10)

        trigramProb = glProb * glProb2 / glProb3
        print('gl value: ')
        print(trigramProb)

    # TODO Write to Trace File
    # It needs: tweet Id, the guess, the value, the real language, wrong/correct
    guess = ""
    label = ""
    largest_number = max(enScore, esScore, ptScore, glScore, caScore, euScore)
    if largest_number == enScore:
        guess = "en"
    elif largest_number == esScore:
        guess = "es"
    elif largest_number == glScore:
        guess = "gl"
    elif largest_number == ptScore:
        guess = "pt"
    elif largest_number == euScore:
        guess = "eu"
    elif largest_number == caScore:
        guess = "ca"
    if guess == language:
        label = "correct"
    else:
        label = "wrong"
    # TODO read those values dynamically if needed (Double check)
    solution_line = tweetId + "  " + str(guess) + " " + "{:.2e}".format(
        largest_number) + "  " + str(language) + "  " + str(label) + "\n"
    solution_file.write(solution_line)
    number_tweet += 1
    # TODO Write to Evaluation file
    # accuracy
    if label == "correct":
        accuracy_numerator += 1

    # Precision
    if guess == "es":
        es_precision_den += 1
        if label == "correct":
            es_precision_num += 1

    if guess == "ca":
        ca_precision_den += 1
        if label == "correct":
            ca_precision_num += 1

    if guess == "en":
        en_precision_den += 1
        if label == "correct":
            en_precision_num += 1

    if guess == "eu":
        eu_precision_den += 1
        if label == "correct":
            eu_precision_num += 1

    if guess == "gl":
        gl_precision_den += 1
        if label == "correct":
            gl_precision_num += 1

    if guess == "pt":
        pt_precision_den += 1
        if label == "correct":
            pt_precision_num += 1

    # Recall 
    if language == "es":
        es_recall_den += 1
        if label == "correct":
            es_recall_num += 1

    if language == "en":
        en_recall_den += 1
        if label == "correct":
            en_recall_num += 1

    if language == "pt":
        pt_recall_den += 1
        if label == "correct":
            pt_recall_num += 1

    if language == "eu":
        eu_recall_den += 1
        if label == "correct":
            eu_recall_num += 1

    if language == "ca":
        ca_recall_den += 1
        if label == "correct":
            ca_recall_num += 1

    if language == "gl":
        gl_recall_den += 1
        if label == "correct":
            gl_recall_num += 1

accuracy_percentage = accuracy_numerator / number_tweet
try:
    en_precision = en_precision_num / en_precision_den
except:
    en_precision = 0
try:
    eu_precision = eu_precision_num / eu_precision_den
except:
    eu_precision = 0
try:
    gl_precision = gl_precision_num / gl_precision_den
except:
    gl_precision = 0
try:
    pt_precision = pt_precision_num / pt_precision_den
except:
    pt_precision = 0
try:
    es_precision = es_precision_num / es_precision_den
except:
    es_precision = 0
try:
    ca_precision = ca_precision_num / ca_precision_den
except:
    ca_precision = 0

gl_recall = gl_recall_num / gl_recall_den
ca_recall = ca_recall_num / ca_recall_den
eu_recall = eu_recall_num / eu_recall_den
pt_recall = pt_recall_num / pt_recall_den
es_recall = es_recall_num / es_recall_den
en_recall = en_recall_num / en_recall_den
# F1-measure
try:
    es_f1 = (2 * es_precision * es_recall) / (es_precision + es_recall)
except:
    es_f1 = 0
try:
    gl_f1 = (2 * gl_precision * gl_recall) / (gl_precision + gl_recall)
except:
    gl_f1 = 0
try:
    pt_f1 = (2 * pt_precision * pt_recall) / (pt_precision + pt_recall)
except:
    pt_f1 = 0
try:
    ca_f1 = (2 * ca_precision * ca_recall) / (ca_precision + ca_recall)
except:
    ca_f1 = 0
try:
    eu_f1 = (2 * eu_precision * eu_recall) / (eu_precision + eu_recall)
except:
    eu_f1 = 0
try:
    en_f1 = (2 * en_precision * en_recall) / (en_precision + en_recall)
except:
    en_f1 = 0

# Macro F1 weighted-average F1
macro_f1 = (es_f1 + en_f1 + eu_f1 + pt_f1 + ca_f1 + gl_f1) / 6
weight_f1 = (
                    es_recall_den * es_f1 + en_precision_den * en_f1 + eu_recall_den * eu_f1 + ca_recall_den * ca_f1 + gl_recall_den * gl_f1) / number_tweet

eval_file_name = "eval_" + str(vocabulary) + "_" + str(whichGram) + "_" + str(smooth_value) + ".txt"

eval_file = open(eval_file_name, 'w+', encoding='utf-8')
accuracy_line = str(accuracy_percentage) + "\n"
eval_file.write(accuracy_line)

precision_line = str(eu_precision) + "  " + str(ca_precision) + "  " + str(gl_precision) + "  " + str(
    es_precision) + "  " + str(en_precision) + "  " + str(pt_precision) + "  " + "\n"
eval_file.write(precision_line)

recall_line = str(eu_recall) + "  " + str(ca_recall) + "  " + str(gl_recall) + "  " + str(
    es_recall) + "  " + str(en_recall) + "  " + str(pt_recall) + "  " + "\n"
eval_file.write(recall_line)

f1_line = str(eu_f1) + "  " + str(ca_f1) + "  " + str(gl_f1) + "  " + str(
    es_f1) + "  " + str(en_f1) + "  " + str(pt_f1) + "  " + "\n"
eval_file.write(f1_line)

macro_average_line = str(macro_f1) + "  " + str(weight_f1)
eval_file.write(macro_average_line)
