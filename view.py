# Password-Generator 
# view.py
# Created by Mauro J. Pappaterra on 06 of November 2017.

#START SCREEN
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
our available dictionaries or any external .txt file and calculate its entropy. You can also compare equivalent 
entropy and password strengths in different sets of characters! 
You might enter 'q' at any time to exit the program.

Enter 's' and press <enter> to begin!
"""

# MAIN MENU
menu = """::::Select one of the available options:
c - Create Password: Generate a random password and calculate it's entropy!
d - Change Dictionary: Change default dictionary, or enter a path to your own text file!
a - About: Read more about secure passwords and entropy.

q - Quit
"""

# ABOUT PAGE
about = """To create a stronger, but easier to remember password, the program will randomly select words from the selected dictionary.

b - Back to menu
"""

# PASSWORD MENU
custom = "Using Custom Dictionary - This might take a few seconds..."

def info_dictionary(n,w):
    text = "DICTIONARY: You are using a dictionary of " + str(n) + " unique words.\n" + \
           "ENTROPY <choosing "+ str(w)+ " random words> : "
    return text

def compare(ten, twentysix, fiftytwo, sixtytwo):
    print("\nThe necessary length for a randomly generated password to have the same entropy, would be:")
    print("From a set of 10 characters [0-9] => " + ten + " characters long")
    print("From a set of 26 characters [a-z] or [A-Z] => " + twentysix + " characters long")
    print("From a set of 52 characters [a-z] and [A-Z] => " + fiftytwo + " characters long")
    print("From a set of 62 characters [a-z] and [A-Z] and [0-9] => " + sixtytwo + " characters long")

your_password = "\nYour password is => "

number_words = "\nHow many random words do you want to use for your password? (Recommended >= 4)"

password_menu = """
g - Generate another password using the same settings
n - New random password
d - Change Dictionary
b - Back to menu
"""

# DICTIONARY MENU
dictionary = """::::Select one of the available options:
f - Use full dictionary 
s - Use simplified dictionary (default)
p - Enter path to your own file...

c - Create random password
b - Back to menu
"""

simple = "\nMESSAGE: You have selected a simplified dictionary of 10000 words.\n"
full = "\nMESSAGE: You have selected a full dictionary of 370099 words.\n"

ask_path = "\n:::: Enter the path to the external .txt file you want to use as a dictionary"
path = "\nMESSAGE: Success! You have selected a custom external dictionary ("

# ERROR MESSAGES
error_start = "\nInvalid Input: Enter 's' to start or 'q' to quit - press <enter>"
error_input = "\nInvalid Input: Select a valid option from the menu"
error_words = "\nInvalid Input: Enter an integer number between 1 and 9999"
error_path = "\nInvalid Input: Not a valid path or file. Try again, or enter 'c' and press <enter> to cancel"

exit = "EXIT BY USER"