# shopping-cart
Shopping cart project for OPIM 243 Python class

[Project Description](https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md) for reference

## Installation and Setup
Clone or download the [shopping-cart repo](https://github.com/bz150/shopping-cart)from GitHub. You may have to fork this first for your own usage.

To access, the program, you will first want to navigate to where it's saved through the command line. If on the desktop (recommended for simplicity), it would be `cd ~/desktop/shopping-cart`.

Next, you'll want to set up a virtual environment. While (base) is sufficient for the simplest version (just the receipt output), the full program requires you to install and activate a virtual environment using Anaconda and install the necessary packages.
```
conda create -n shopping-env python=3.8
conda activate shopping-env
pip install -r requirements.txt
```

## Usage
To run the program in its simplest form, enter `python shopping_cart.py` into the command line after completing the installation and setup.

To see options for customizing the tax rate and seting up email receipts, please see below.

### Custom Tax Rate
To set your own tax rate according to municipality, please change the TAX_RATE variable. This can be done in your local repository.

Create a .env file and a variable called TAX_RATE. Enter the rate as a decimal (e.g. `TAX_RATE=0.1` for 10%). If no rate is entered, it will default to 8.75%.

### Email Setup
Email receipts can be sent to the customer using the SendGrid API. Full reference from Prof. Rossetti's instructions can be found [here](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md), the following is adapted and abbreviated.

First, install the SendGrid package `pip install sendgrid` and make sure the version is later than 6.0.5.

After signing up and verifying your account online, create a SendGrid API key and be sure to allow "full access" when asked. This will be entered into your .env file as the SENDGRID_API_KEY.

The SENDER_ADDRESS is the email that you used to create and verify your SendGrid account. Quotes are required.

Lastly, the SENDGRID_TEMPLATE_ID is up to you to create. If you add a [dynamic template](https://mc.sendgrid.com/dynamic-templates), SendGrid will provide you an ID. 
```
SENDGRID_API_KEY = key
SENDER_ADDRESS = "user@email.com"
SENDGRID_TEMPLATE_ID = key 
```
This is an example template, once again based off of Prof. Rossetti's. Please feel free to customize it based off of your goals.
```
<html>
    <head>
      <title></title>
    </head>
    <body>
    
    <img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

    <h3>Hello this is your receipt</h3>

    <p>Date: {{human_friendly_timestamp}}</p>

    <p>You ordered:</p>
    <ul>
    {{#each products}}
	<li>+ {{this.name}} ... ${{this.price}}</li>
    {{/each}}
    </ul>
    
    <p>Subtotal: {{subtotal_price_usd}}</p>
    <p>Tax: {{tax_price_usd}}</p>
    <p>Total: {{total_price_usd}}</p>
    
    
    
    
      <div data-role="module-unsubscribe" class="module" role="module" data-type="unsubscribe" style="color:#444444; font-size:12px; line-height:20px; padding:16px 16px 16px 16px; text-align:Center;" data-muid="4e838cf3-9892-4a6d-94d6-170e474d21e5">
        
        <p style="font-size:12px; line-height:20px;">
          <a class="Unsubscribe--unsubscribeLink" href="{{{unsubscribe}}}" target="_blank" style="font-family:sans-serif;text-decoration:none;">
            Unsubscribe
          </a>
          -
          <a href="{{{unsubscribe_preferences}}}" target="_blank" class="Unsubscribe--unsubscribePreferences" style="font-family:sans-serif;text-decoration:none;">
            Unsubscribe Preferences
          </a>
        </p>
      </div>
    </body>
</html>
```