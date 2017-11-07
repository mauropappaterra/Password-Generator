# Password-Generator 
# GUI.py
# Created by Mauro J. Pappaterra on 04 of November 2017.
import passwords as p
import view as v
import time

def start():
    exit = False
    while (not exit):

        print(v.welcome)
        print(v.instructions)

        read = input()

        while (read != 's' and read != 'q'):
            print ("Invalid Input. Enter 's' to start or 'q' to quit")
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
        print("Invalid Input. Select a valid option from the menu")
        read = input()

    if (read == '1'):
         return password()
    elif (read == '2'):
        return main()
    elif (read == '3'):
        return about()
    elif (read == 'q'):
        return True

def about():

    print (v.about)

    read = input()
    while (read != 'b' and read != 'q'):
        print("Invalid Input. Select a valid option from the menu")
        read = input()

    if (read == 'b'):
        return main()
    elif (read == 'q'):
        return True

def password():
    print (v.password_intro)

    time.sleep(0.5)

    print (v.entropy(10000) + p.getEntropy(10000) + " bits")

    time.sleep(0.5)

    print (v.your_password + p.getPassword())

    ten = p.estimateLength(10, 44)
    twentysix = p.estimateLength(10, 44)
    fiftytwo = p.estimateLength(52, 44)
    sixtytwo = p.estimateLength(62, 44)

    time.sleep(0.5)

    v.compare(ten, twentysix, fiftytwo, sixtytwo)

    time.sleep(0.5)

    read = input()
    while (read != 'b' and read != 'a' and read != 'q'):
        print("Invalid Input. Select a valid option from the menu")
        read = input()

    if (read == 'b'):
        return main()
    elif (read == 'a'):
        return password()
    elif (read == 'q'):
        return True





start()

