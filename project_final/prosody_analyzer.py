'''
J Austin Hutchinson
CSE 111
Week #
Assignment Name
'''

import requests,json,string


def main():
    '''
    FOR:    Handling User Input
    PARAM:  none
    RETURN: 0
    '''
    # print intro and disclaimer

    print("This tool uses the Datamuse API to analyze a line of text for word stress and calculates in what poetic meter the line is in.") 
    print("Disclaimer: Datamuse can only calculate on a word by word basis. Changes in a words stresses based on their context in a statement is not calculated.")
    while True:
        # get desired text
        text = input("Please insert a line of english words to analyze. Punctuation is ignored. (q to quit): ").lower()
        
        if text == "q":
            print("Thank you for using this tool!")
            break
            
        cleaned_text = clean_text(text)
        # print(cleaned_text)
        
        if any(char.isdigit() for char in cleaned_text):
            print("\tThat line contains a digit, and is thus invalid. Please use the whole english words when using numbers. ex. \"Two\", not \"2\".\n")
            continue
        # get the analysis from datamuse
        text_analysis = get_api_response(cleaned_text)
        # print(text_analysis)

        if text_analysis == []:
            print("\tInvalid Line. Please enter a valid line of english text.\n")
            continue
        elif len(text_analysis) < 2:
            print("\tA single word is not a valid target for analysis. Please enter a line of text for analysis.\n")
            continue
        # extract wor stress pattern from datamuse analysis
        text_stresses = calculate_stresses(text_analysis)
        
        # use stress pattern to calculate line type
        foot_pattern = calculate_foot_pattern(text_stresses)
        final_pattern = match_metrical_pattern(foot_pattern) 
        # Print Result
        print(f"This line has the following poetic feet:")
        foot_string = ""
        for foot in foot_pattern:
            foot_string += foot + ", "
        print(f"\t{foot_string}")
        print(f"\tThis line is written in {final_pattern.title()}.\n")
        
    return 0

# Helper Functions

def clean_text(text):
    '''
    FOR:    cleaning the input text of punctuation
    PARAM:  text
    RETURN: list of words
    '''
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    cleaned_text = cleaned_text.lower().split()
    return cleaned_text

def get_api_response(text):
    '''
    FOR:    getting the basic analysis from https://www.datamuse.com/api/
    PARAM:  text
    RETURN: api
    '''
    responses = []
    for word in text:
        raw_request = requests.get(f"https://api.datamuse.com/words?sp={word}&max=1&md=r&ipa=1").text
        raw_request = json.loads(raw_request)
        responses.append([raw_request[0]["word"],raw_request[0]["tags"][0]])
    return responses

def calculate_stresses(text):
    '''
    FOR:    take the analysed text and calculatre the meter
    PARAM:  text
    RETURN: string of 1's and 0's indicating the stresses
    '''
    stresses = ""
    for word in text:
        for character in word[1]:
            if character in string.digits:
                stresses+=character
    # print(stresses)
    return stresses
def check_syllables(pattern, check_list, final_list):
    '''
    FOR:    checking a pattern vs entries in a list of syllables  
    PARAM:  the pattern to check, the list of patterns to check it against, the final list to be modified by a matched pattern
    RETURN: how many lines to skip, or 0 if no match was found
    '''
    for syllable in check_list:
        if pattern == syllable[0]:
           final_list.append(syllable[1])
           return len(syllable[0])-1
    return 0
def calculate_foot_pattern(pattern):
    '''
    FOR:    determine if a metrical pattern matches a particular poems pattern  
    PARAM:  the pattern to check as a string of 1's and 0's, 1's being stressed syllables and 0's being unstressed
    RETURN: a list of the poetic feet for the pattern
    '''
    # feet patterns: "01"-"iamb", "10"-"trochee", "110"-"anapest", "011"-"dactyl", 
    # only top be found in the revision "101" - amphibrach, "100" - bacchius, "010" - cretic, 011 - dactyl

    #TODO: add handling for empty strings and single digit patterns
    # list the syllables we are going to be testig against
    disyllables = [
                    ["00","dibrach"],
                    ["01","iamb"],
                    ["10","trochee"],
                    ["11","spondee"],
                    ]
    trisyllables = [
                    ["000","tribrach"],
                    ["100","dactyl"],
                    ["010","amphibrach"],
                    ["001","anapest"],
                    ["011","bacchius"],
                    ["101","amphimacer"],
                    ["110","antibacchius"],
                    ["111","molossus"]
                    ]
    disyllables_common = [
                    ["01","iamb"],
                    ["11","spondee"]
                    ]   
    trisyllables_common = [                
                    ["001","anapest"],
                    ["100","dactyl"]
                    ]
    disyllables_uncommon = [
                    ["10","trochee"],
                    ["00","pyrrhic"]
                    ]
    trisyllables_uncommon = [
                    ["110","antibacchius"],
                    ["010","amphibrach"],
                    ["000","tribrach"],
                    ["111","molossus"],
                    ["011","bacchius"],
                    ["101","cretic"]
                    ]
    unisyllables = [
                    ["0", "macer"],
                    ["1", "brach"]
                    ]
    
    # do initial setup   
    foot_pattern = []
    pattern_length = len(pattern)
    skip_step = 0

    for index in range(0, pattern_length):
        # ship this round if previous checks indicate so
        if skip_step > 0:
            skip_step -= 1
            continue
        # establish what we're testing
        pattern_remaining = pattern_length - index
        # print(pattern_remaining)
        unisyllable = pattern[index]
        disyllable = pattern[index]+pattern[index+1]
        if pattern_remaining > 2:
            trisyllable = pattern[index]+pattern[index+1]+pattern[index+2]
        else:
            trisyllable = ""
        
        # start testing
        if pattern_remaining > 4:
            # check most likely
            if skip_step == 0:
                skip_step = check_syllables(disyllable, disyllables_common, foot_pattern)
            if skip_step == 0:
                skip_step = check_syllables(trisyllable, trisyllables_common, foot_pattern)
            if skip_step == 0:
                skip_step = check_syllables(disyllable, disyllables_uncommon, foot_pattern)
            if skip_step == 0:
                skip_step = check_syllables(trisyllable, trisyllables_uncommon, foot_pattern)
            if skip_step == 0:
                skip_step = check_syllables(unisyllable, unisyllables, foot_pattern)
            continue
        elif pattern_remaining == 3:
            skip_step = check_syllables(trisyllable, trisyllables, foot_pattern)
            if skip_step == 0:
                skip_step = check_syllables(trisyllable, trisyllables_uncommon, foot_pattern)
            continue
        elif pattern_remaining == 2 or pattern_remaining == 4: 
            skip_step = check_syllables(disyllable, disyllables, foot_pattern)
            continue
    return foot_pattern
def match_metrical_pattern(passed_pattern):
    '''
    FOR:    determine if a metrical pattern matches a particular poems pattern  
    PARAM:  
    RETURN: list of
    '''
    number_of_feet = ["monometer", "dimeter", "trimeter", "tetrameter", "pentameter", "hexameter", "heptameter", "octameter", "nonameter"]
    mono_foot_types = [
        ["dibrach", "dibrachic"],
        ["iamb", "iambic"],
        ["trochee", "trocheeic"],
        ["spondee", "spondeeic"],
        ["tribach", "tribrachic"],
        ["dactyl", "dactylic"],
        ["amphibrach", "amphibrachic"],
        ["anapest", "anapestic"],
        ["bacchius", "bacchiusic"],
        ["amphimacer", "amphimaceric"],
        ["antibacchius", "antibacchiusic"],
        ["molossus", "molossusic"]
        ]
    # patterns = ["iambic pentameter", "alexandrine", "blank verse", "Common Meter", "long Meter"]

    output = ""

    # calculate mono_pattern
    mono = True
    for type in mono_foot_types:
        for foot in passed_pattern:
            if type[0] != foot:
                mono = False
        if mono == True:
            output+=type[1]+" "
            break
        else:
            mono = True
    
    # calculate total number of feet in line
    total_feet = len(passed_pattern)
    output+=number_of_feet[total_feet-1]
    # return output
    return output


# Main call
if __name__ == "__main__":
    main()