
# ========= Parse Arguments ===========
import argparse

parser = argparse.ArgumentParser(description="Build a word frequency dictionary from a text file.")
parser.add_argument("text", type=str, help="The text file to read from.")
parser.add_argument("-o", "--output", type=str, default="weights.json", help="The output JSON file to write the word frequencies to.")
parser.add_argument("-l", "--limit", type=int, default=-1, help="Limit the number of words to process. Default is -1 (no limit).")
args = parser.parse_args()


file = args.text
outputFile = args.output
limit = args.limit

# ==== Read File and Build Dictionary ====

try:
    text = open(file, encoding="utf-8").read()
    text = text.split()
except FileNotFoundError:
    print("ERROR: File not found")
    quit()
     


words = {}

# text = "pine pine a dog twelve a dog dog".split()
def isalnum(word): # method to function converter... ick. would be ideal place for lambda func tho
    return word.isalnum()


for i in range(len(text[:limit]) - 2):
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

    

# ==== Dump Weights as JSON ==========================

import json
with open(outputFile, "w+") as f:
    json.dump(words, f)

print(f"'{outputFile}' weights successfully created!")

