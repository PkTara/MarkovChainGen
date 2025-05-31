
file = "bible.txt"
# file = "text.txt"
text = open(file, encoding="utf-8").read()
text = text.split()


words = {}

# text = "pine pine a dog twelve a dog dog".split()
def isalnum(word): # method to function converter... ick. would be ideal place for lambda func tho
    return word.isalnum()

for i in range(len(text[:1000]) - 2):
    first, last = text[i:i+2]
    for chunk in [first, last]:
        chunk = filter(isalnum, chunk)


    if first not in words:
        words[first] = {}

    if last not in words[first]:
        words[first][last] = 0

    words[first][last] += 1



for word in words.keys():
    # print(words[word])
    words[word] = dict(sorted(words[word].items()))
# print(words)



word = input("Input: ")

import random

temperature = 1
def nextWord(word):
    # The list is sorted, so will return most frequent word.

    wordList = list(words[word].keys())

    frequencies = list(words[word].values())
    total = sum(frequencies)
    probabilities = [freq / total for freq in frequencies]

    cumulativeProb = [probabilities[0]]
    for prob in probabilities[1:]:
        # print(prob)
        cumulativeProb.append(cumulativeProb[-1] + prob)
        # print("cum: ", cumulativeProb[-1])

    
    randomPoint = random.random()
    choice = ""
    for index, prob in enumerate(cumulativeProb):
        if prob > randomPoint:
            choice = wordList[index]
            # print(choice)
            break

    return(choice)




    # print(list(words[word].keys()))
    print(frequencies)

    return list(words[word].keys())[0]


output = ""
for i in range(200):
    output += " " + word
    word = nextWord(word)

print(output)