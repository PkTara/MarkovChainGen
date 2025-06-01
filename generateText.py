
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=str, help="Path to the JSON file containing word frequencies.")
parser.add_argument("-n", "--noWords", type=int, default=100, help="Number of words to generate. Default is 100.")
parser.add_argument("-s", "--startWord", type=str, default="the", help="Starting word for text generation. Default is 'the'. Default may error if not found in the text.")
args = parser.parse_args()


# ========= Parse Arguments ===========

file_path = args.file_path
noWords = args.noWords
startWord = args.startWord

# ==== Import JSON ====
import os

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, "weights",  file_path)


import json
with open(file_path) as f:
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


def generate(startWord: str, noWords=100):
    output = ""
    word = startWord

    if word not in words:
        raise ValueError(f"Word '{word}' not found in the dictionary. You are currently using {file_path}. Try again with a different word.")
    
    for i in range(noWords):
        output += " " + word
        word = nextWord(word)

    return output

# ===================================================

if __name__ == "__main__":
    # startWord = input("Input: ")
    print(generate(startWord, noWords=noWords))