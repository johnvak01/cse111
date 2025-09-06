"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# code start
import math
age = int(input(f"Please enter your age: "))
max_rate = 220 - age
top_rate = math.floor(max_rate * 0.85)
bottom_rate = math.floor(max_rate * 0.65)

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {top_rate} and {bottom_rate} beats per minute.")