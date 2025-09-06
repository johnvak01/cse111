'''
Enter the number of items: 8
Enter the number of items per box: 5
For 8 items, packing 5 items in each box, you will need 2 boxes.
> python boxes.py
Enter the number of items: 25
Enter the number of items per box: 4
For 25 items, packing 4 items in each box, you will need 7 boxes.
'''

import math
items_total = int(input("Enter the number of items: "))
per_box_total = int(input("Enter the number of items per box: "))
print(f"For {items_total} items, packing {per_box_total} items in each box, you will need {math.ceil(items_total/per_box_total)} boxes.")