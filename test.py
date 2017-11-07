# Password-Generator 
# test.py
# Created by Mauro J. Pappaterra on 07 of November 2017.

import model as m


simple = "dictionaries/dictionary_simple.txt" # path to dictionary
full = "dictionaries/dictionary_simple.txt" # path to dictionary
path = "dictionaries/karamazov.txt"

dictionary_a = m.createDictionary(simple)
dictionary_b = m.createDictionary(full)
dictionary_c = m.createDictionary(path)


print(m.getRandom(dictionary_a))
print(m.getRandom(dictionary_b))
print(m.getRandom(dictionary_c))

print(m.getPassword(dictionary_a))
print(m.getPassword(dictionary_b))

print(m.getEntropy(10000))
print(m.getEntropy(10))
print(m.getEntropy(26))
print(m.getEntropy(52))
print(m.getEntropy(62))

print(m.estimateLength(10,54))




