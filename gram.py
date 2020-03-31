def gram(message, n):
    grams = [message[i:i + n] for i in range(len(message) - n + 1)]
    final = removeStar(grams)
    return final


def removeStar(grams):
    newarr = []
    for i in grams:
        if '*' not in i:
            newarr.append(i)
    return newarr
