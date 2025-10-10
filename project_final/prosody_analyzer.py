'''
J Austin Hutchinson
CSE 111
Week #
Assignment Name
'''

import requests,json


def main():
    '''
    FOR:    Handling User Input
    PARAM:  none
    RETURN: 0
    '''
    # get desired text
    text = input("What text are we analyzing?")
    # clean the text
    text = clean_text(text)
    analysis = get_api_response(text)

    return 0

# Helper Functions

def clean_text(text):
    '''
    FOR:    cleaning the input text of punctuation
    PARAM:  text
    RETURN: list of words
    '''
    cleaned_text = text.split()
    print(cleaned_text)
    return cleaned_text


def get_api_response(text):
    '''
    FOR:    getting the basic analysis from https://www.datamuse.com/api/
    PARAM:  text
    RETURN: api
    '''
    responses = []
    for word in text:
        raw_request = requests.get(f"https://api.datamuse.com/words?sp={word}&max=1&md=r").text
        print(raw_request)
        raw_request = json.loads(raw_request)
        print(raw_request)
        responses.append([raw_request[0]["word"],raw_request[0]["tags"][0]])
    print(responses)
    return responses

def calculate_meter():
    '''
    FOR:    take the analysed text and calculatre the meter
    PARAM:  x
    RETURN: x
    '''
    pass
def match_metrical_pattern():
    '''
    FOR:    determine if a metrical pattern matches a particular poems pattern  
    PARAM:  x
    RETURN: x
    '''
    pass
def check_alliteration():
    '''
    FOR:    check for matching consonant sounds
    PARAM:  x
    RETURN: x
    '''
    pass
def check_rhyme():
    '''
    FOR:    check for rhyme
    PARAM:  x
    RETURN: x
    '''
    pass

def lineate_text():
    '''
    FOR:    take a text and convert it into poetic form, seperating lines etc.
    PARAM:  x
    RETURN: x
    '''
    pass
    
# Main call
if __name__ == "__main__":
    main()