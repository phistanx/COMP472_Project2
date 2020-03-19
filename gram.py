from collections import Counter


def gram(message, n):
    final = []
    for j in message:
        c = [j[i:i + n] for i in range(len(j) - n + 1)]
        final += c
        # print(c)
    # print(final)
    createTable(final, 'en')


def createTable(gram, language):
    enList = []
    esList = []
    d = Counter(gram)
    for key, value in d.items():
        print(key +' ' + str(value))
