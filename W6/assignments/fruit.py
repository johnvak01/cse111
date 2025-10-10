'''
J Austin Hutchinson
CSE 111
Week #
Assignment Name
'''
def main():
    '''
    FOR:    manipulating the fruit list
    PARAM:  none
    RETURN: int 0 if successfully run
    '''
    # step 1
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    # reverse and print the list
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")
    # append "orange" to the end of fruit_list and print the list.
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")
    # find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
    index = fruit_list.index("apple")
    fruit_list.insert(index,"cherry")
    print(f"insert cherry: {fruit_list}")
    # remove "banana" from fruit_list and print the list
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")
    # pop the last element from fruit_list and print the popped element and the list.
    fruit_list.pop()
    print(f"pop orange: {fruit_list}")
    # sort and print fruit_list
    fruit_list.sort()
    print(f"sorted: {fruit_list}")
    # clear and print fruit_list
    fruit_list.clear()
    print(f"cleared: {fruit_list}")
    
    return 0

# Main call
if __name__ == "__main__":
    main()