# Password-Generator 
# model.py
# Created by Mauro J. Pappaterra on 04 of November 2017.
from random import *
import math

def createDictionary (path):
    mode = "r"
    with open(path, mode) as myFile:
        dictionary = (myFile.readlines())  # save each word as an element on a list
    return dictionary

def getRandom(dictionary):
    'Returns a randomized word from the dictionary'
    size = len(dictionary)
    random = randint(0, size)  # generates random number between zero and size of list
    word = dictionary[random] # fetches word from dictionary
    return word.replace('\n','')

def getPassword(dictionary, n):
    'Returns n randomized words from a dictionary concatenated together'
    password = ""
    while (n > 1):
        password += getRandom(dictionary) + " "
        n -= 1
    password += getRandom(dictionary)
    return password

def getEntropy (size, n):
    entropy = math.log(size, 2) * n
    return round(entropy, 2)

def estimateLength(s, n):
    """Given the size of the set and the entropy (n) as an argument
    returns the number of characters needed to get the same
    entropy on a set of s character """

    entropy = n / math.log(s, 2)
    return str(round(entropy, 2))