# shopping_cart.py
# pasted in from https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md

from datetime import datetime #timestamp
import webbrowser #URL potentially

import os
from dotenv import load_dotenv #email receipt
from sendgrid import SendGridAPIClient #email receipt
from sendgrid.helpers.mail import Mail #email receipt
load_dotenv()

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
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

# print(products)
# print(type(products[0]["id"])) #product ID are all int

# 
# USER INPUT
# 
active = True #setting the variable for the while loop to true to start
product_id_list = [] #creating an empty list to append IDs into
while active == True:    
    product_id = input("Please input the ID number of your product:")
    if product_id != "done":
        product_id_list.append(product_id)
    elif product_id == "done":    
        #active == False
        break

# 
# PROGRAM OUTPUT
# 
print("---------------------------------")
print("BRYAN'S FRESH MARKET")
print("WWW.BryansFreshMarket.com") #add hyperlink?
print("---------------------------------")


# printing the time of checkout
now = datetime.now()
current_date_time = now.strftime("%m/%d/%Y %H:%M:%S")
print("CHECKOUT AT:", current_date_time)
print("---------------------------------")


# printing selected products
    # thanks to Prof. Rossetti for the lookup matching lines
print("SELECTED PRODUCTS:")
price_list = []
for product_id in product_id_list:
    selected_products = [x for x in products if str(x["id"]) == str(product_id)]
    selected_product = selected_products[0]
    price_list.append(selected_product["price"])
    print("+ ", selected_product["name"], "...", to_usd(selected_product["price"]))
print("---------------------------------")

# my original way
# for i in product_id_list:
#     print("+", products[i-1]["name"], "...", to_usd(products[i-1]["price"]))
#     price_list.append(products[i-1]["price"])
# print("---------------------------------")

# totaling the bill
subtotal = sum(price_list)
tax = subtotal * 0.0875
print("SUBTOTAL:", to_usd(subtotal))
print("TAX:", to_usd(tax))
print("TOTAL:", to_usd(tax+subtotal))
print("---------------------------------")


# 
# SENDGRID EMAIL RECEIPT
# (or skip out)

customer_choice = input("Would you like a receipt? (y/n) ")
customer_choice = customer_choice.lower()
if customer_choice == "y":
    customer_email = input("What is your email address?")
    if "@" not in customer_email:
        print("Sorry, there was an error.")
        print("THANKS, SEE YOU AGAIN SOON!")
        print("---------------------------------")
        exit()
    else:
        EMAIL_ADDRESS = customer_email
        print(f"Sending an email to {EMAIL_ADDRESS}")

        SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
        SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

        client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
        print("CLIENT:", type(client))

        subject = "Your Receipt from Bryan's Fresh Market"

        #message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

        price_list = []
        for product_id in product_id_list:
            selected_products = [x for x in products if str(x["id"]) == str(product_id)]
            selected_product = selected_products[0]
            price_list.append(selected_product["price"])
            print("+ ", selected_product["name"], "...", to_usd(selected_product["price"]))
        print("---------------------------------")

        subtotal = sum(price_list)
        tax = subtotal * 0.0875
        print(subtotal)
    #
    #    receipt = {
    #        "subtotal_price_usd": to_usd(subtotal),
    #        "tax_price_usd": to_usd(tax),
    #        "total_price_usd": to_usd(total),
    #        "human_friendly_timestamp": human_friendly_timestamp,
    #        "products": formatted_products
    #    }
    #    #print(receipt)
    #
        client = SendGridAPIClient(SENDGRID_API_KEY)
     
        message = Mail(from_email=customer_email, to_emails=customer_email)
        #message.template_id = SENDGRID_TEMPLATE_ID
        #message.dynamic_template_data = receipt
     
        response = client.send(message)
     
        if str(response.status_code) == "202":
            print("Email sent successfully!")
        else:
            print("Oh, something went wrong with sending the email.")
            print(response.status_code)
            print(response.body)

else:
    print("THANKS, SEE YOU AGAIN SOON!")
    print("---------------------------------")
    
    









