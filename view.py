# Password-Generator 
# view.py
# Created by Mauro J. Pappaterra on 06 of 11 2017.

welcome = """                ____                                          __
               / __ \____ ____________      ______  _________/ /
              / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  / 
             / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  
            /_/____\\_,_/____/____/ |__/|__/\___\\_/   \__,_/   
              / ____/__  ____  ___  _________ _/ /_____  _____  
             / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/  
            / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /      
            \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     v1.0

              = Create passwords and calculate entropy =                                   

            """
instructions = """Welcome to Password Generator. This short program will help you generate a random password from 
our available dictionaries or any external .txt file and calculate its entropy. You can also compare entropy and password strengths! 
Enter 'q' at any time to exit the program.

Enter 's' and press <enter> to begin!
"""

menu = """Select one of the available options:
1 - CREATE PASSWORD => Generate a password and calculate it's entropy!
2 - CHANGE DICTIONARY => Change default dictionary or enter a path to your own text file!
3 - ABOUT => Read more about secure passwords and entropy.

q - quit

"""

about = """To create a stronger, but easier to remember password, the program will randomly select words from the selected dictionary.

b - back to menu

"""

def info_dictionary(n):
    text = "DICTIONARY: You are using a dictionary of " + str(n) + " words.\n" + \
           "ENTROPY <choosing 4 random words> : "
    return text


def compare(ten, twentysix, fiftytwo, sixtytwo):
    print("\nThe necessary length for a randomly generated password to have the same entropy, would be:")
    print("From a set of 10 characters [0-9] => " + ten)
    print("From a set of 26 characters [a-z] or [A-Z] => " + twentysix)
    print("From a set of 52 characters [a-z] and [A-Z] => " + fiftytwo)
    print("From a set of 62 characters [a-z] and [A-Z] and [0-9] => " + sixtytwo)

your_password = "\nYour password is => "

password_menu = """
n - new password
b - back to menu
"""

dictionary = """ Select a dictionary to generate the password:
f - Full Dictionary 
s - Simplified Dictionary (default)
p - Enter path to your own file...

b - back to menu
"""

simple = "\nMESSAGE: You have selected a simplified dictionary of 10000 words.\n"
full = "\nMESSAGE: You have selected a full dictionary of 370099 words.\n"
path = "\nMESSAGE: This option is unavailable. Nothing has changed.\n"

error_start = "Invalid Input. Enter 's' to start or 'q' to quit - press <enter>"
error_input = "Invalid Input. Select a valid option from the menu"
error_path = "Error: Not a valid path or file. Try again.."
exit = "EXIT BY USER"