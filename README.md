# shopping-cart
Shopping cart project for OPIM 243 Python class

[Project Description](https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md) for reference

## Installation and Setup
Clone or download the [shopping-cart repo](https://github.com/bz150/shopping-cart)from GitHub. You may have to fork this first for your own usage.
To access, the program, you will first want to navigate to where it's saved through the command line. If on the desktop (recommended for simplicity), it would be `cd ~/desktop/shopping-cart`.
Next, you'll want to set up a virtual environment. While (base) is sufficient for the simplest version (just the receipt output), the full program requires you to install/activate a virtual environment using Anaconda `conda create -n shopping-env python=3.8` followed by `conda activate shopping-env`. You'll want to install the necessary packages specified with the line `pip install -r requirements.txt`.

## Usage
To run the program in its simplest form, enter `python shopping_cart.py` into the command line after completing the installation and setup.
To see options for customizing the tax rate and seting up email receipts, please see below.
### Custom Tax Rate
To set your own tax rate according to municipality, please change the TAX_RATE variable. This can be done in your local repository.
Create a .env file and a variable called TAX_RATE. Enter the rate as a decimal (e.g. `TAX_RATE=0.1` for 10%). If no rate is entered, it will default to 8.75%.
### Email Setup
Email receipts can be sent to the customer using the SendGrid API. Full reference from Prof. Rossetti's instructions can be found [here](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md).
First, install the sendgrid package `pip install sendgrid` and make sure the version is later than 6.0.5.
