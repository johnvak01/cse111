'''
J AUstin Hutchinson
CSE 111
Week 2
Assignment Fuel Efficiency
'''
def main():
    '''
    FOR:    handling user input and output 
    PARAM:  none
    RETURN: 0 on successful completion
    '''
    start = float(input("Enter the first odometer reading (miles): "))
    end = float(input("Enter the second odometer reading (miles): "))
    gallons = float(input("Enter the amount of fuel used (gallons): "))

    mpg = miles_per_gallon(end, start,gallons)
    lpk = lp100k_from_mpg(mpg)
    
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lpk:.2f} liters per 100 kilometers")

    return 0

# Helper Functions
def miles_per_gallon(end, start, gallons):
    '''
    FOR:    the calculation of miles per gallon
    PARAM:  
        - end | the odometer value at the end of the trip in miles
        - start | the odometer value at the start of the trip in miles
        - gallons | the fuel amount in US gallons
    RETURN: the fuel efficiency in miles per gallon
    '''
    mpg = (end-start)/gallons
    return mpg
    
def lp100k_from_mpg(mpg):
    '''
    FOR:    Converting Miles per gallon to liters per 100 kilometers 
    PARAM:  
        - mpg | the figure to be converted
    RETURN: the converted fuel efficiency value in liters per 100 kilomter
    '''
    lp1k = 235.215/mpg
    return  lp1k

# Function call
main()