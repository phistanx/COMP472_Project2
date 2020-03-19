import Vocabulary
import gram

for i in Vocabulary.read():
    # print(i.message)
    gram.gram(i.message, 1)
