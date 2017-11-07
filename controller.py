# Password-Generator 
# controller.py
# Created by Mauro J. Pappaterra on 04 of November 2017.
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

        read = input()

        while (read != 's' and read != 'q'):
            print (v.error_start)
            read = input()

        if (read == 's'):
            exit = main()

        if (read == 'q'):
            exit = True
    print (v.exit)

def main ():
    print(v.menu)

    read = input()
    while (read != '1' and read != '2' and read != '3' and read != 'q'):
        print (v.error_input)
        read = input()

    if (read == '1'):
         return password(True)
    elif (read == '2'):
        return dictionary_menu()
    elif (read == '3'):
        return about()
    elif (read == 'q'):
        return True

def about():

    print (v.about)

    read = input()
    while (read != 'b' and read != 'q'):
        print (v.error_input)
        read = input()

    if (read == 'b'):
        return main()
    elif (read == 'q'):
        return True

def password(intro):

    if (use_simple):
        dictionary = simple [:]
    elif (use_full):
        dictionary = full [:]

    size = len(dictionary)
    entropy = m.getEntropy(size)

    if (intro):
        print (v.info_dictionary(size) + str(entropy) + " bits")
        time.sleep(1)
        print (v.your_password + m.getPassword(dictionary))

        ten = m.estimateLength(10, entropy)
        twentysix = m.estimateLength(10, entropy)
        fiftytwo = m.estimateLength(52, entropy)
        sixtytwo = m.estimateLength(62, entropy)

        time.sleep(1)

        v.compare(ten, twentysix, fiftytwo, sixtytwo)

    else:
        print(v.your_password + m.getPassword(dictionary))

    print (v.password_menu)

    read = input()
    while (read != 'b' and read != 'n' and read != 'q'):
        print (v.error_input)
        read = input()

    if (read == 'b'):
        return main()
    elif (read == 'n'):
        return password(False)
    elif (read == 'q'):
        return True

def dictionary_menu ():
    global use_simple
    global use_full

    print (v.dictionary)

    read = input()
    while (read != 's' and read != 'f'and read != 'p'and read != 'b' and read != 'q'):
        print (v.error_input)
        read = input()

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

    elif (read == 'q'):
        return True
