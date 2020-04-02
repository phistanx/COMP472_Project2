import re


class Language:
    language: None
    message: None
    tweetId: None

    def __init__(self, language, message, tweetId):
        self.language = language
        self.message = message
        self.tweetId = tweetId

def read(file_name):
    file = open(file_name, 'r', encoding="utf-8")
    my_list = []
    for line in file:
        try:
            y = line.replace("\t", " ")
            y = y.replace("\n", "")
            x = y.split(" ", 3)
            # first argument is the vocabulary, x[3] is the message
            message = vocabulariesUpdateMessage(1, x[3])
            # x[2] is the language of the tweet
            my_list.append(Language(x[2], message, x[0]))
        except:
            print("ERROR EXCEPTION =============")
            print(x[0])
    return my_list


def vocabulariesUpdateMessage(vocabulary, message):
    newMess = ""
    if vocabulary == 0:
        for i in range(len(message)):
            if re.match('[A-Z]', message[i]):
                newMess += message[i].lower()
            elif re.match('[a-z]', message[i]):
                newMess += message[i]
            else:
                newMess += "*"
    elif vocabulary == 1:
        for i in range(len(message)):
            if re.match('[a-zA-Z]', message[i]):
                newMess += message[i]
            else:
                newMess += "*"
    elif vocabulary == 2:
        for i in range(len(message)):
            if (message[i].isalpha()):
                newMess += message[i]
            else:
                newMess += "*"
    return newMess
