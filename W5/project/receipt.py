'''
J Austin Hutchinson
CSE 111
Week #
Assignment Name
'''
# Creative Portion: Printing a return date 30 days in the future at 9pm 
import csv, datetime
def main():
    '''
    FOR:    x 
    PARAM:  x
    RETURN: x
    '''
    PRODUCTS_PATH = "products.csv"
    REQUEST_PATH = "request.csv"
    # PRODUCTS_PATH = "./W5/project/products.csv"
    # REQUEST_PATH = "./W5/project/request.csv"
    SALES_TAX_RATE = 0.06
    
    # print title   
    print("Emperors Emporium")
   
    try:
        products_dict = read_dictionary(PRODUCTS_PATH,0)
        # print(products_dict)
        receipt = []
        # print("Requested Items")
        with open(REQUEST_PATH,"rt") as request_file:
            requests = csv.reader(request_file)
            next(requests)
            for request in requests:
                product = products_dict[request[0]]
                
                print(f"{product[1]}: {request[1]} @ {product[2]}")
                receipt.append(product)
        
        # print total items
        print(f"Number of Items: {len(receipt)}")

        # calculate and display subtotal
        subtotal = 0
        for product in receipt:
            subtotal += float(product[2])
        print(f"Subtotal: {subtotal}")

        #calculate and display sales tax value
        sales_tax_total = round(subtotal * SALES_TAX_RATE,2)
        print(f"Sales Tax: {sales_tax_total}")

        # calculate and display inclusive_total
        inclusive_total = round(subtotal+sales_tax_total,2)

        # print Thank you message
        print("Thank you for shopping at the Emperor Emporium.")

        # print time
        current_time = datetime.datetime.now()
        print(f"{current_time.strftime("%c")}")

        # Print return Date
        return_date = current_time + datetime.timedelta(days=30)
        print(f"Return Date: {return_date.strftime("%a %b %d")} @ 9pm")

    except FileNotFoundError as e:
        print("Error: one of the files does not exist")
        print(e)
    except PermissionError as e:
        print("Error: You Lack permission to open one of your files")
        print(e)
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)

     



    return 0

# Helper Functions
def read_dictionary(filepath,key_column_index):
    '''
    FOR:    Read acsv file and create a compund dictionary 
    PARAM:  string filepath
    RETURN: dict with the contents of the csv file
    '''
    contents = {}
    with open(filepath,mode="rt") as csv_file:
        file = csv.reader(csv_file)
        next(file)
        for row in file:
            contents[row[key_column_index]] = row

    return contents


# Main call
if __name__ == "__main__":
    main()