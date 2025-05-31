word = input("Input: ")

# ==== Import JSON ====

file = "bible.json"
import json
with open(file) as f:
    words = json.load(f)

# ======================


import random
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

def printWords(noWords):
    output = ""
    for i in range(noWords):
        output += " " + word
        word = nextWord(word)

    return output

# ===================================================

if "__name__" == "__main__":
    print(printWords())