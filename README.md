# shopping-cart
Shopping cart project for OPIM 243 Python class

[Project Description](https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md) for reference

## Installation and Setup
Clone or download the shopping-cart repo from [GitHub](https://github.com/bz150/shopping-cart)
To access, the program, you will first want to navigate to where it's saved through the command line. If on the desktop (recommended for simplicity), it would be `cd ~/desktop/shopping-cart`
Next, you'll want to set up a virtual environment. While (base) is sufficient for the simplest version (just the receipt output), the full program requires you to install/activate a virtual environment using Anaconda. The lines are `conda create -n shopping-env python=3.8` followed by `conda activate shopping-env`. You'll want to install the necessary packages specified with the line `pip install -r requirements.txt`.

## Usage
To run the program, enter `python shopping_cart.py` into the command line after completing the installation and setup.

To set your own tax rate according to municipality, please change the TAX_RATE variable in the .env file as a decimal. If no rate is entered, it will default to 8.75%.