from collections import Counter
def gram(n):

    b = ['student', 'stud', 'mike']
    final = []
    for j in b:
        c = [j[i:i + n] for i in range(len(j) - n+1)]
        final += c
        print(c)
    print(final)
    createTable(final, 'en')

def createTable(gram, language):
    enList = []
    esList = []
    d = Counter(gram)
    print(d)



gram(3)
