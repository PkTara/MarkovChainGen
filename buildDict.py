
import sys
args = sys.argv

outputFile="weights.json"
if len(args) > 2:
    outputFile = args[2]
if len(args) > 1:
    file = args[1]

else: # default file
    print("ERROR: must provide filename")
    quit()

# file = "bible.txt"
# file = "text.txt"
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

# ==== Dump Weights as JSON ==========================

import json
with open(outputFile, "w+") as f:
    json.dump(words, f)

print(f"'{outputFile}' weights successfully created!")

