# Password-Generator 
# model.py
# Created by Mauro J. Pappaterra on 04 of November 2017.
from random import *
import math
import codecs

# NOTE: 'Dictionaries' are stored into lists, not in a Python's actual dictionary data structure.

def createDictionary (path):
    "Takes a path to a dictionary-formatted .txt file, and returns a list (or 'dictionary') containing all words"
    mode = "r"
    with open(path, mode) as myFile:
        dictionary = (myFile.readlines())  # save each word as an element on a list
    return dictionary

def createExternal (path):
    "Takes a path to an external .txt file and returns a list (or 'dictionary') containing all words"
    mode = "r"
    dictionary = []
    word = ""

    with codecs.open(path, mode, encoding='utf8') as myFile :
        full_text = myFile.readlines() # saves each line of the text into a list

        for line in full_text:  # iterates on each line on the list
            #FOR TESTING PURPOSES
            #print('\n' + line)

            for character in line:  # iterates every character on a line with a for loop
                if (character.isalpha() or character == '-' or character == "'"):
                    word += character.lower()
                elif (character.isspace()):
                    if not (word in dictionary):
                        #FOR TESTING PURPOSES
                        #print(word)
                        dictionary.append(word)
                    word = ""

    dictionary.sort()
    #FOR TESTING PURPOSES
    #print(dictionary)
    return dictionary

def getRandom(dictionary):
    "Returns a random word from a given list (or 'dictionary')"
    size = len(dictionary)
    random = randint(0, size)  # generates random number between zero and size of list
    word = dictionary[random] # fetches word from dictionary
    return word.replace('\n','')

def getPassword(dictionary, n):
    "Returns n randomized words from a list (or 'dictionary') concatenated together"
    password = ""
    while (n > 1):
        password += getRandom(dictionary) + " "
        n -= 1
    password += getRandom(dictionary) # work around to avoid extra space
    return password

def getEntropy (size, n):
    "Takes the size of a set and the number of elements to be selected from the set, calculates entropy"
    entropy = math.log(size, 2) * n
    return round(entropy, 2) # rounded to two digits

def estimateLength(s, n):
    """Takes the size of a set (s) and an entropy value (n)
    returns the number of elements that need to be selected from the set
    to achieve the same entropy value"""
    entropy = n / math.log(s, 2)
    return str(round(entropy, 2))