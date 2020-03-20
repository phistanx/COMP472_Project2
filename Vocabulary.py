import re


class Language:
    language: None
    message: None

    def __init__(self, language, message):
        self.language = language
        self.message = message


def read():
    file = open("training-tweets.txt", 'r', encoding="utf-8")
    my_list = []
    for line in file:
        y = line.replace("\t", " ")
        y = y.replace("\n", "")
        x = y.split(" ", 3)
        message = vocabularies(0, x[3])
        my_list.append(Language(x[2], message))
    return my_list


def vocabularies(vocabulary, message):
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
