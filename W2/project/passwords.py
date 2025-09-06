'''
J AUstin Hutchinson
CSE 111
Week #
Assignment Name
'''
'''
Enhancement: used the getpass module to hide the user input (so they don't display the password they are entering where anyone can see it)
'''
# Imports
import getpass as gp

# constants
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

# Main Function
def main():
    '''
    FOR:    the user input loop. quit the program if q/Q is entered 
    PARAM:  none
    RETURN: 0 if run successfully
    '''
    while True:
        word = gp.getpass("Please Enter a New Secure Password: ")
        if word.lower() == "q":
            return 0;
        word_score = password_strength(word)
        print(f"The Password has a complexity score of {word_score}") 

    return 0

# Helper Functions
def word_in_file(word,filename, case_sensitive=False):
    '''
    FOR:    reads words from a file and checks it against a set list, with toggle for case sensitivity 
    PARAM:  
        word - word to check against the file
        filename - string: file to read from
        case_sensitive - bool: toggles whether match is case sensitive or not
    RETURN: 
        True - if word matches one in the file
        False - if word doesn't match any in the file
    '''
    if case_sensitive == False:
        word = word.lower()

    with open(filename,"r",encoding="utf-8") as file:
        for line in file:
            if case_sensitive == False:
                line = line.lower()
            if word == line.strip():
                return True
    return False

def word_has_character(word, character_list):
    '''
    FOR:    checks if word includes a character in a given list
    PARAM:  
        word - word to check
        character_list - list to check against
    RETURN: 
        True - if the word contains one of the characters from the list
        False - if the word does not ~
    '''
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    '''
    FOR:    generates a value based on the types of characters the word contains. one point given per type(max 4)
    PARAM:  
        word - the word to check
    RETURN: 
        int - the complexity value
    '''
    complexity = 0;
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length = 10, strong_length = 16):
    '''
    FOR:    calculating and printing the passwords strength
    PARAM:  
        password - the word to check
        min_length - the minimum length the word should be
        max_length - the maximum length the word should be
    RETURN: 
        int - the passwords strength (0-5)
    '''
    if word_in_file(password,"wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0;
    elif word_in_file(password,"toppasswords.txt"):
        print("Password is a commonly used password and is not secure.")
        return 0;
    elif len(password)<min_length:
        print("Password is too short and is not secure.")
        return 1;
    elif len(password)>strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5;
    else:
        return 1+word_complexity(password)
    return 0

# Function call
if __name__ == "__main__":
    main()