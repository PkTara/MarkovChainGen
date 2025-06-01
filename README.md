# Markov Chain Text Generator

Given a piece of text, buildDict will create a dictionary of every word, and the probability of another word following it.
I.e   "cat" -> [("is", 0.6), ("scratched", 0.3), ("jumped", 0.1)]

A json file is then created with all these weights. 

generateText then loads up a json file, and generates words according to said probabilities.



# buildDict

usage: buildDict.py [-h] [-o OUTPUT] [-l LIMIT] text

Build a word frequency dictionary from a text file.

positional arguments:
  text                 The text file to read from.

options:
  -h, --help           show this help message and exit
  -o, --output OUTPUT  The output JSON file to write the word frequencies to.
  -l, --limit LIMIT    Limit the number of words to process. Default is -1 (no limit).



# generateText

usage: generateText.py [-h] [-n NOWORDS] [-s STARTWORD] file_path

positional arguments:
  file_path             Path to the JSON file containing word frequencies.

options:
  -h, --help            show this help message and exit
  -n, --noWords NOWORDS
                        Number of words to generate. Default is 100.
  -s, --startWord STARTWORD
                        Starting word for text generation. Default is 'the'. Default may error if not found in the text.

