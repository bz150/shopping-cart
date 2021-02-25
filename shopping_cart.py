# shopping_cart.py
# pasted in from https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md

from datetime import datetime #timestamp
import webbrowser #URL potentially

import os
from dotenv import load_dotenv #connected to env variables
from sendgrid import SendGridAPIClient #email receipt using sendgrid
from sendgrid.helpers.mail import Mail #email receipt using sendgrid
load_dotenv()

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price per": "item"},
    {"id":21, "name": "Organic Bananas", "department": "fruit", "aisle": "produce", "price": 0.79, "price per": "pound"}

] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

# print(type(products[0]["id"])) #product ID are all int

# 
# USER INPUT
#

valid_id_list = [str(x["id"]) for x in products]
active = True #setting the variable for the while loop to true to start
product_id_list = [] #creating an empty list to append IDs into
while active == True:    
    product_id = input("Please input the ID of your product or 'done': ")
    if product_id in valid_id_list:
        product_id_list.append(product_id)
    elif product_id.lower() == "done":    
        active = False
        #break
    else:
        print("Please enter a valid ID or 'done' if you are finished.")

# 
# PROGRAM OUTPUT
# 
print("---------------------------------")
print("BRYAN'S FRESH MARKET")
print("www.BryansFreshMarket.com")
print("---------------------------------")


# printing the time of checkout
now = datetime.now()
current_date_time = now.strftime("%m/%d/%Y  %H:%M:%S")
print("CHECKOUT AT:", current_date_time)
print("---------------------------------")


# printing selected products
    # thanks to Prof. Rossetti for the lookup matching lines
print("SELECTED PRODUCTS:")
price_list = []
item_list = []
for product_id in product_id_list:
    selected_products = [x for x in products if str(x["id"]) == str(product_id)]
    selected_product = selected_products[0]
    price_list.append(round(selected_product["price"],2))
    item_list.append(selected_product) #list of dictionaries with items selected
    print("+ ", selected_product["name"], "...", to_usd(selected_product["price"]))
print("---------------------------------")

            # my original way
            # for i in product_id_list:
            #     print("+", products[i-1]["name"], "...", to_usd(products[i-1]["price"]))
            #     price_list.append(products[i-1]["price"])
            # print("---------------------------------")


# totaling the bill
subtotal = sum(price_list)
TAX_RATE = os.getenv("TAX_RATE", default = 0.0875)
TAX_RATE = float(TAX_RATE) #convert the env var to a float
tax = subtotal * TAX_RATE


print("SUBTOTAL:", to_usd(subtotal))
#print("TAX RATE:", TAX_RATE) #used to test default/user entered tax rate working
print("TAX:", to_usd(tax))
print("TOTAL:", to_usd(tax+subtotal))
print("---------------------------------")


# 
# SENDGRID EMAIL RECEIPT (or skip to end)
# 
# Attribution for all Sendgrid-related content to Prof. Rossetti - https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md
customer_choice = input("Would you like a receipt emailed to you? (y for yes) ") #ask user
customer_choice = customer_choice.lower()
active = True
if customer_choice == "y":
    while active == True:
        customer_email = input("What is your email address? ")
        if "@" not in customer_email:
            reenter = input("That email address doesn't seem to be valid. Do you want to retry? (y for yes) ")
            if reenter.lower() == "y":
                active = True
            else:
                print("THANKS, SEE YOU AGAIN SOON!")
                print("---------------------------------")
                active = False
                exit()
        else:        
            SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
            SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
            SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

            template_data = { # must match the test data structure
                "total_price_usd": to_usd(subtotal+tax),
                "subtotal_price_usd": to_usd(subtotal),
                "tax_price_usd": to_usd(tax),
                "human_friendly_timestamp": current_date_time,
                "products": item_list
            } # or construct this dictionary dynamically based on the results of some other process :-D

            client = SendGridAPIClient(SENDGRID_API_KEY)
            #print("CLIENT:", type(client))

            #message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
            message = Mail(from_email=SENDER_ADDRESS, to_emails=customer_email)
            message.template_id = SENDGRID_TEMPLATE_ID
            message.dynamic_template_data = template_data
            #print("MESSAGE:", type(message))

            try:
                response = client.send(message)
                if response.status_code == 202:
                    print("Email sent successfully!")
                    print("THANKS, SEE YOU AGAIN SOON!")
                    print("---------------------------------")
                    exit()
                else:
                    reenter = input("Sorry, there was an error. Do you want to retry? (y for yes) ")
                    if reenter.lower() == "y":
                        active = True
                    else:
                        print("THANKS, SEE YOU AGAIN SOON!")
                        print("---------------------------------")
                        active = False
                        exit()
                #print("RESPONSE:", type(response))
                #print(response.headers)
                #print(response.status_code)
                #print(response.body)
            except Exception as err:
                reenter = input("Sorry, something went wrong with sending to that address. Do you want to retry? (y for yes) ")
                if reenter.lower() == "y":
                    active = True
                else:
                    #print(type(err))
                    #print(err)
                    print("THANKS, SEE YOU AGAIN SOON!")
                    print("---------------------------------")
                    active = False
                    exit()
else:
    print("THANKS, SEE YOU AGAIN SOON!")
    print("---------------------------------")
# for future reference, easier to just leave the last two lines outside and have user exit while loop instead of retyping many times