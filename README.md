# Codecademy Project: Sal's Shipping

![""](https://github.com/sarahm44/sals-shipping-project/blob/main/sals-shipping.jpg)

## Contents
- [Overview](#overview)
- [Shipping Options](#shipping-options)
- [Pricing Structure](#pricing-structure)
- [Python Program](#python-program)
- [Finding the Best Option for a Customer](#finding-the-best-option-for-a-customer)

## Overview
I was required to write a Python program for Sal's Shipping.

The program: 
1. Asks the user for the weight of their package;
2. Tells them which method of shipping is cheapest; and
3. Tells them how much it will cost to ship their package using Sal’s Shippers.

## Shipping Options
Sal’s Shippers has several different options for a customer to ship their package:
* Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
* Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
* Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

## Pricing Structure
### Ground Shipping

| Weight of Package | Price per Pound | Flat Charge |
| --- | --- | --- |
| 2 lb or less | $1.50 | $20.00 |
| Over 2 lb but less than or equal to 6 lb	| $3.00	| $20.00 |
| Over 6 lb but less than or equal to 10 lb	| $4.00	| $20.00 |
| Over 10 lb	| $4.75	| $20.00 |

### Ground Shipping Premium
Flat charge: $125.00

### Drone Shipping
| Weight of Package	| Price per Pound	| Flat Charge |
| --- | --- | --- |
| 2 lb or less	| $4.50	| $0.00 |
| Over 2 lb but less than or equal to 6 lb	| $9.00	| $0.00 |
| Over 6 lb but less than or equal to 10 lb	| $12.00	| $0.00 |
| Over 10 lb	| $14.25	| $0.00 |

## Python Program
The file [here](https://github.com/sarahm44/sals-shipping-project/blob/main/sals_shipping.py) contains the Python Program to help Sal's Shipping customers select the best option for their shipping needs.

I used if/elif/else statements to define the pricing structure set out above, per this image:

![""](https://github.com/sarahm44/sals-shipping-project/blob/main/python_code.png)

## Finding the Best Option for a Customer
### For a 4.8 pound package
I used the code to answer the question:

* *What is the cheapest method of shipping a 4.8 pound package and how much would it cost?*

To do so I defined the weight variable as per the below:

![""](https://github.com/sarahm44/sals-shipping-project/blob/main/weight_variable_4.8.png)

The output from running the code is:

![""](https://github.com/sarahm44/sals-shipping-project/blob/main/output_4.8.png)

As such, the cheapest option for the customer is **Ground Shipping** for a price of **$34.40**.

### For a 41.5 pound package
I used the code to answer the question:

* *What is the cheapest method of shipping a 41.5 pound package and how much would it cost?*

To do so I defined the weight variable as per the below:

![""](https://github.com/sarahm44/sals-shipping-project/blob/main/weight_variable.png)

The output from running the code is:

![""](https://github.com/sarahm44/sals-shipping-project/blob/main/output.png)

As such, the cheapest option for the customer is **Ground Shipping Premium** for a price of **$125**.
