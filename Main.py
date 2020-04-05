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
        "f1": 0,
        "triList": [],
        "triAB": [],
        "triBC": 0,
        "triBstar": 0
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
        "recallNum": 0,
        "f1": 0,
        "triList": [],
        "triAB": [],
        "triBC": 0,
        "triBstar": 0
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
        "f1": 0,
        "triList": [],
        "triAB": [],
        "triBC": 0,
        "triBstar": 0
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
        "f1": 0,
        "triList": [],
        "triAB": [],
        "triBC": 0,
        "triBstar": 0
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
        "f1": 0,
        "triList": [],
        "triAB": [],
        "triBC": 0,
        "triBstar": 0
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
        "f1": 0,
        "triList": [],
        "triAB": [],
        "triBC": 0,
        "triBstar": 0
    }
}

vocabulary = 2
whichGram = 2
smooth_value = 0.3
# accuracy
accuracy_numerator = 0
number_tweet = 0
accuracy_percentage = 0

solution_file_name = "trace_" + str(vocabulary) + "_" + str(whichGram) + "_" + str(smooth_value) + ".txt"
solution_file = open("trace/" + solution_file_name, 'w+', encoding='utf-8')

training_tweet = "training-tweets.txt"
test_tweet = "test-tweets-given.txt"

# Create the dictionary of words and their count
for i in Vocabulary.read(training_tweet, vocabulary):
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

if whichGram == 3:
    for tweet in Vocabulary.read(training_tweet, vocabulary):
        languages[tweet.language]["triList"] += gram.gram(tweet.message, 2)
        languages[tweet.language]["triAB"] += gram.gram(tweet.message, 1)

    for key, value in languages.items():
        languages[key]["triList"] = (Counter(languages[key]["triList"]))
        addSmoothValue(languages[key]["triList"], smooth_value)
        languages[key]["triAB"] = (Counter(languages[key]["triAB"]))
        addSmoothValue(languages[key]["triAB"], smooth_value)

# Evaluate Test tweets
for i in Vocabulary.read(test_tweet, vocabulary):
    dummy_message = i.message
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
        # test = ["ab',"cd"]
        for key, value in languages.items():
            languages[key]["score"] = math.log(languages[key]["tweetProb"], 10)
        for i in test:
            for lang, value in languages.items():
                firstCharCount = 0
                newdic = {k: v for k, v in languages[lang]["list"].items() if k[0] == i[0]}
                for key, count in newdic.items():
                    firstCharCount += int(count)
                try:
                    languages[lang]["score"] += math.log(
                        (languages[lang]["list"].get(i, smooth_value)) / firstCharCount, 10)
                except:
                    pass
                if vocabulary == 3:
                    diff_lang = ['Ç', 'ü', 'é', 'â', 'ä', 'à', 'ç', 'ê', 'ë', 'è', 'ï', 'î', 'ì', 'Ä', 'Å', 'É', 'ô', 'ö',
                                 'ò', 'û', 'ù', 'ÿ', 'Ö', 'Ü', 'á', 'í', 'ó', 'ú', 'ñ', 'Ñ']
                    if 1 in [c in dummy_message for c in diff_lang]:
                        languages["en"]["score"] = -100000
                        languages["eu"]["score"] = -100000

    if whichGram == 3:
        # Tri-gram P(ABC) = P(AB) * P(BC) / P(B*), B* = all tri-grams starting with B
        # AB list
        # building the bi-gram list

        for key, value in languages.items():
            languages[key]["score"] = math.log(languages[key]["tweetProb"], 10)

        for val in test:
            for lang, value in languages.items():
                # P(C)
                languages[lang]["score"] += math.log(languages[lang]["triAB"].get(val[0], smooth_value)/ languages[lang]["words"], 10) * 0.1

                # P(C |B )
                firstCharCount = 0
                newdic = {k: v for k, v in languages[lang]["triList"].items() if k[0] == val[0]}
                for key, count in newdic.items():
                    firstCharCount += int(count)
                try:
                    languages[lang]["score"] += math.log(
                        (languages[lang]["triList"].get(val[0]+val[1], smooth_value)) / firstCharCount, 10) * 0.3
                except:
                    pass

                # P(C |A,B ) = P(ABC) / P(start AB)
                firstCharCount = 0
                newdic = {k: v for k, v in languages[lang]["list"].items() if (k[0]+k[1]) == val[0]+val[1]}
                for key, count in newdic.items():
                    firstCharCount += int(count)
                try:
                    languages[lang]["score"] += math.log(
                        (languages[lang]["list"].get(val, smooth_value)) / firstCharCount, 10) * 0.6
                except:
                    pass
            # firstCharCount = 0
            # ABtrigram = val[0] + val[1]
            # BCtrigram = val[1] + val[2]
            # for lang, value in languages.items():
            #     languages[lang]["triAB"] = 0
            #     newdic = {k: v for k, v in languages[lang]["triList"].items() if k[0] == val[0]}
            #     for key, count in newdic.items():
            #         firstCharCount += int(count)
            #     try:
            #         languages[lang]["triAB"] = (languages[lang]["triList"].get(ABtrigram, smooth_value)) / firstCharCount
            #     except:
            #         pass
            #
            # for lang, value in languages.items():
            #     languages[lang]["triBC"] = 0
            #     newdic = {k: v for k, v in languages[lang]["triList"].items() if k[0] == val[1]}
            #     for key, count in newdic.items():
            #         firstCharCount += int(count)
            #     try:
            #         languages[lang]["triBC"] = (languages[lang]["triList"].get(BCtrigram,
            #                                                                    smooth_value)) / firstCharCount
            #     except:
            #         pass
            #
            # for lang, value in languages.items():
            #     languages[lang]["triBstar"] = 0
            #     for key, value in languages[lang]["list"].items():
            #         if key[0] == val[1]:
            #             languages[lang]["triBstar"] += int(value)
            #     try:
            #         languages[lang]["triBstar"] = languages[lang]["triBstar"] / languages[lang]["words"]
            #     except:
            #         languages[lang]["triBstar"] = -5
            #
            # for lang, value in languages.items():
            #     try:
            #         languages[lang]["score"] += math.log(languages[lang]["triAB"] * languages[lang]["triBC"] / (languages[lang]["triBstar"]), 10)
            #     except:
            #         pass

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
    print(label + "  " + guess)

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
try:
    accuracy_percentage = accuracy_numerator / number_tweet
except:
    pass

evaluation.writeToEvaluationFile(languages, whichGram, number_tweet, smooth_value, vocabulary, accuracy_percentage)

print("Done")
