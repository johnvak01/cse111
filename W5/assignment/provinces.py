'''
J Austin Hutchinson
CSE 111
Week #
Assignment Name
'''
import os

def main():
    '''
    FOR:    x 
    PARAM:  x
    RETURN: x
    '''
    print(os.getcwd())
    provinces = []
    with open("W5/assignment/provinces.txt", mode="rt") as province_list:
        for province in province_list:
            provinces.append(province.strip())
    print(provinces)
    # altering the list
    provinces.pop(0)
    provinces.pop()
    provinces = [province.replace("AB", "Alberta") for province in provinces]
    total = provinces.count("Alberta")
    print(f"Alberta occurs {total} times in the modified list.")
    return 0

# Helper Functions

# Main call
if __name__ == "__main__":
    main()