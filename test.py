# Password-Generator 
# test.py
# Created by Mauro J. Pappaterra on 07 of November 2017.
import model as m
import mock
import unittest

simple = "dictionaries/dictionary_simple.txt" # path to dictionary
full = "dictionaries/dictionary_simple.txt" # path to dictionary
path = "dictionaries/idiot.txt"

dictionary_a = m.createDictionary(simple)
dictionary_b = m.createDictionary(full)
dictionary_c = m.createExternal(path)

print(m.getRandom(dictionary_a))
print(m.getRandom(dictionary_b))
print(m.getRandom(dictionary_c))

print(m.getPassword(dictionary_a,4))
print(m.getPassword(dictionary_a,10))

print(m.getPassword(dictionary_b,4))
print(m.getPassword(dictionary_b,10))

print(m.getPassword(dictionary_c,4))
print(m.getPassword(dictionary_c,10))

print(m.getEntropy(10000,5))
print(m.getEntropy(10,4))
print(m.getEntropy(26,4))
print(m.getEntropy(52,4))
print(m.getEntropy(62,4))

print(m.estimateLength(10,54))