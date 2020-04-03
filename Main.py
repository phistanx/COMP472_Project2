import Vocabulary
import gram
from collections import Counter
import math
import evaluation

def countWords(dictionary):
    count = 0
    for key, value in dictionary.items():
        count += value
    return count


def addSmoothValue(languagelist, smooth_value):
    for key, value in languagelist.items():
        languagelist[key] = value + smooth_value


languages = {
    "en": {
        "count": 0,
        "list": [],
        "words": 0,
        "tweetProb": 0,
        "score": 0,
        "precision": 0,
        "precisionDen": 0,
        "precisionNum": 0,
        "recall": 0,
        "recallDen": 0,
        "recallNum": 0,
        "f1": 0
    },
    "es": {
        "count": 0,
        "list": [],
        "words": 0,
        "tweetProb": 0,
        "score": 0,
        "precision": 0,
        "precisionDen": 0,
        "precisionNum": 0,
        "recall": 0,
        "recallDen": 0,
        "recallNum":0,
        "f1": 0
    },
    "pt": {
        "count": 0,
        "list": [],
        "words": 0,
        "tweetProb": 0,
        "score": 0,
        "precision": 0,
        "precisionDen": 0,
        "precisionNum": 0,
        "recall": 0,
        "recallDen": 0,
        "recallNum": 0,
        "f1": 0
    },
    "eu": {
        "count": 0,
        "list": [],
        "words": 0,
        "tweetProb": 0,
        "score": 0,
        "precision": 0,
        "precisionDen": 0,
        "precisionNum": 0,
        "recall": 0,
        "recallDen": 0,
        "recallNum": 0,
        "f1": 0
    },
    "ca": {
        "count": 0,
        "list": [],
        "words": 0,
        "tweetProb": 0,
        "score": 0,
        "precision": 0,
        "precisionDen": 0,
        "precisionNum": 0,
        "recall": 0,
        "recallDen": 0,
        "recallNum": 0,
        "f1": 0
    },
    "gl": {
        "count": 0,
        "list": [],
        "words": 0,
        "tweetProb": 0,
        "score": 0,
        "precision": 0,
        "precisionDen": 0,
        "precisionNum": 0,
        "recall": 0,
        "recallDen": 0,
        "recallNum": 0,
        "f1": 0
    }
}

vocabulary = 0
whichGram = 1
smooth_value = 0.1
# accuracy
accuracy_numerator = 0
number_tweet = 0
accuracy_percentage = 0

solution_file_name = "trace_" + str(vocabulary) + "_" + str(whichGram) + "_" + str(smooth_value) + ".txt"
solution_file = open("trace/" + solution_file_name, 'w+', encoding='utf-8')

training_tweet = "training-tweets.txt"
test_tweet = "test-tweets.given.txt"

# Create the dictionary of words and their count
for i in Vocabulary.read(training_tweet):
    # create a dictionary of uni/bi/tri-gram
    languages[i.language]["count"] += 1
    languages[i.language]["list"] += gram.gram(i.message, whichGram)

# create the probability of each language for a tweet
totalTweet = 0
for key, value in languages.items():
    totalTweet += languages[key]["count"]
# use Counter library to create dictionary with unique keys (character) and the count of the keys and add smooth value
for key, value in languages.items():
    languages[key]["list"] = (Counter(languages[key]["list"]))
    addSmoothValue(languages[key]["list"], smooth_value)
    languages[key]["words"] = countWords(languages[key]["list"])
    languages[key]["tweetProb"] = languages[key]["count"] / totalTweet

# Evaluate Test tweets
for i in Vocabulary.read(training_tweet):
    tweetId = i.tweetId
    language = i.language
    test = gram.gram(i.message, whichGram)
    if whichGram == 1:
        for key, value in languages.items():
            languages[key]["score"] = math.log(languages[key]["tweetProb"], 10)
        for i in test:
            for key, value in languages.items():
                languages[key]["score"] += math.log(
                    ((languages[key]["list"].get(i, smooth_value)) / languages[key]["words"]), 10)

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
    largest_number = max(languages["es"]["score"], languages["en"]["score"], languages["pt"]["score"],
                         languages["ca"]["score"], languages["gl"]["score"], languages["eu"]["score"])
    for key, value in languages.items():
        if languages[key]["score"] == largest_number:
            guess = key
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

    for key, value in languages.items():
        # Precision
        if guess == key:
            languages[key]["precisionDen"] += 1
            if label == "correct":
                languages[key]["precisionNum"] += 1
        # Recall
        if language == key:
            languages[key]["recallDen"] += 1
            if label == "correct":
                languages[key]["recallNum"] += 1

accuracy_percentage = accuracy_numerator / number_tweet

evaluation.writeToEvaluationFile(languages, whichGram, number_tweet, smooth_value, vocabulary, accuracy_percentage)

print("Done")
