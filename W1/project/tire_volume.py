'''
# J Austin Hutchinson
# Week 1 - Project - Volumes
'''

'''
Extra Feature
Sales Lead generation. appending contact phone number if the customer desires to purchase a tire of said dimension.
'''
import math
tire_width = int(input(f"Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input(f"Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input(f"Enter the diameter of the wheel in inches (ex 15): "))
volume = math.pi * (tire_width **2)*aspect_ratio*(tire_width*aspect_ratio+2540*diameter)*(1/10_000_000_000)
volume = round(volume,2)
print(f"The approximate volume is {volume} liters")

'''
part 2
'''
from datetime import datetime

current_date = datetime.now(tz=None).strftime("%Y-%m-%d")

with open("volumes.txt","a") as volumes:
    volumes.write(f"{current_date}, {tire_width}, {aspect_ratio}, {diameter}, {volume}")
    response = 0
    while response != "y" and response != "n":
        response = input("Do you wish to purchase a tire of these dimensions(y/n): ").lower()
        if response == "y":
            phone = input("Please enter you phone number: ")
            volumes.write(f"\n{phone}\n")
            print(f"A sales Representative will call you back at {phone}")
        elif response != "n":
            print("INVALID RESPONSE")
        


'''
Extra
'''
