# Password-Generator 
# controller.py
# Created by Mauro J. Pappaterra on 06 of November 2017.
import model as m
import view as v
import time

# DEFAULT DICTIONARIES
dictionary = []
simple = m.createDictionary("dictionaries/dictionary_simple.txt")
full = m.createDictionary("dictionaries/dictionary_full.txt")

use_simple = True
use_full = False

def start():

    exit = False
    while (not exit):

        print(v.welcome)
        print(v.instructions)

        read = input().lower()

        while (read != 's' and read != 'q'):
            print (v.error_start)
            read = input().lower()

        if (read == 's'):
            exit = main()

        if (read == 'q'):
            exit = True
    print (v.exit)

def main ():
    print(v.menu)

    read = input().lower()
    while (read != 'c' and read != 'd' and read != 'a' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == 'c'):
         return password()
    elif (read == 'd'):
        return dictionary_menu()
    elif (read == 'a'):
        return about()
    elif (read == 'q'):
        return True

def about():

    print (v.about)

    read = input().lower()
    while (read != 'b' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == 'b'):
        return main()
    elif (read == 'q'):
        return True

def password():
    global dictionary

    if (use_simple):
        dictionary = simple [:]
    elif (use_full):
        dictionary = full [:]

    size = len(dictionary)

    print (v.number_words)
    no_words = input()
    while (not (no_words.isdigit()) or not(1 <= int(no_words) <= 9999)):
        print(v.error_words)
        no_words = input()

    no_words = int (no_words)
    entropy = m.getEntropy(size, no_words)

    print (v.info_dictionary(size, no_words) + str(entropy) + " bits of entropy")
    time.sleep(1)
    print (v.your_password + m.getPassword(dictionary, no_words))

    ten = m.estimateLength(10, entropy)
    twentysix = m.estimateLength(26, entropy)
    fiftytwo = m.estimateLength(52, entropy)
    sixtytwo = m.estimateLength(62, entropy)

    time.sleep(1)

    v.compare(ten, twentysix, fiftytwo, sixtytwo)

    print (v.password_menu)

    read = input().lower()
    while (read != 'b' and read != 'n' and read != 'g' and read != 'd' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == 'b'):
        return main()
    elif (read == 'g'):
        return generate_new(dictionary, no_words)
    elif (read == 'n'):
        return password()
    elif (read == 'd'):
        return dictionary_menu()
    elif (read == 'q'):
        return True

def generate_new(dictionary, no_words):

    print (v.your_password + m.getPassword(dictionary, no_words))

    print(v.password_menu)

    read = input().lower()
    while (read != 'b' and read != 'n' and read != 'g' and read != 'd' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == 'b'):
        return main()
    elif (read == 'g'):
        return generate_new(dictionary, no_words)
    elif (read == 'n'):
        return password()
    elif (read == 'q'):
        return True

def dictionary_menu ():
    global use_simple
    global use_full

    print (v.dictionary)

    read = input().lower()
    while (read != 's' and read != 'f'and read != 'p'and read != 'b' and read != 'c' and read != 'q'):
        print (v.error_input)
        read = input().lower()

    if (read == 's'):
        use_simple = True
        use_full = False
        print (v.simple)
        return dictionary_menu()

    elif (read == 'f'):
        use_simple = False
        use_full = True
        print(v.full)
        return dictionary_menu()

    elif (read == 'p'):
        print(v.path)
        print("Available soon!")
        return dictionary_menu()

    elif (read == 'b'):
        return main()

    elif (read == 'c'):
        return password()

    elif (read == 'q'):
        return True