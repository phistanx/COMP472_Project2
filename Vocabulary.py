import re

class Language:
    language: None
    message: None
    def __init__(self,language,message):
        self.language = language
        self.message = message

def read():
    file = open("training-tweets.txt", 'r', encoding="utf-8")
    my_list = []
    for line in file:
        y = line.replace("\t"," ")
        x = y.split(" ", 3)  
        my_list.append(Language(x[2],x[3]))
        # my_List.append(Language(x[2], x[3]))       
    return my_list

def vocabularies(vocabulary, message):
    x = ""
    if(vocabulary == 0):
        for i in range(len(message)):
            if re.match('[A-Z]', message[i]):
                x+=message[i].lower()
            elif re.match('[a-z]', message[i]):
                x += message[i]
            else:
                x += "*"
    elif(vocabulary == 1):
        for i in range(len(message)):
            if re.match('[a-zA-Z]', message[i]):
                x += message[i]
            else:
                x += "*"
    elif (vocabulary == 2):
        for i in range(len(message)):
            if(message[i].isalpha()):
                x += message[i]
            else:
                x += "*"

    return x    

