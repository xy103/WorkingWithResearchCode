# Checks to see if your customer can buy a drink based on 
# age and number of drinks (has to be under max of 4)

age = 24
number_of_drinks = 3 

LEGAL_DRINKING_AGE = 21
DRINKS_CAP = 4

of_legal_age = age >= LEGAL_DRINKING_AGE
under_drinks_cap = number_of_drinks < DRINKS_CAP
if of_legal_age and under_drinks_cap:
    print('can buy a drink')
