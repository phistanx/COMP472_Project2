from collections import Counter


def gram(message, n):
    grams = [message[i:i + n] for i in range(len(message) - n + 1)]
    final = removeStar(grams)
    # print(final)
    return final


def removeStar(grams):
    newarr = []
    for i in grams:
        if '*' not in i:
            newarr.append(i)
    return newarr
