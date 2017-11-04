# Password-Generator 
# passwords.py
# Created by Mauro J. Pappaterra on 04 of November 2017.
from random import *

path = "dictionary_simple.txt" # path to dictionary
mode = "r" # read mode

with open (path, mode) as myFile:
    dictionary = (myFile.readlines()) # save each word as an element on a list

size = len (dictionary) # retrieve size of the list

def getRandom():
    'Returns a randomized word from the dictionary'
    random = randint(0, size)  # generates random number between zero and size of list
    word = dictionary[random] # fetches word from dictionary
    return word.replace('\n','')

def getPassword():
    'Returns four randomized words from the dictionary concatenated together'
    password = getRandom() +" "+ getRandom() +" "+ getRandom() +" "+ getRandom()
    print (password)
    return password.replace(' ','')

# FOR TESTING
#print(getRandom()) # print a random word
#print (getPassword()) # print a password