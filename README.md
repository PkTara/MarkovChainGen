# Markov Chain Text Generator

Given a piece of text, buildDict will create a dictionary of every word, and the probability of another word following it.
I.e   "cat" -> [("is", 0.6), ("scratched", 0.3), ("jumped", 0.1)]

A json file is then created with all these weights. 

generateText then loads up a json file, and generates words according to said probabilities.



