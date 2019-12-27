import decimal

#Accept Naira charge
Naira_charge = input("Enter the Naira amount charged: ")
try:
    Naira_charged = decimal.Decimal(Naira_charge)
except:
    print("Invalid Input")
    exit()

#Accept lower exchange rate value
Lower_Exchange_rate = input("Enter the lower limit of exchage rate: ")
try:
    Lower_Exchange_rated = decimal.Decimal(Lower_Exchange_rate)
except:
    print("Invalid Input")
    exit()

#Accept higher exchange rate value
Higher_Exchange_rate = input("Enter the upper limit of exchage rate: ")
try:
    Higher_Exchange_rated = decimal.Decimal(Higher_Exchange_rate)
except:
    print("Invalid Input")
    exit()

#test the validity of the spwcified limits
if Lower_Exchange_rated >= Higher_Exchange_rated:
    print('''
    Lower limit of Exchange rate cannot be higher than the
    upper limit of exchange rate.
    ''')
    exit()

#initialise a dictionary for collecting the possible dollar charges
#and exchange rates
exchange_dict = {}

while not Lower_Exchange_rated > Higher_Exchange_rated:
        dollar_charged = Naira_charged/Lower_Exchange_rated
        if dollar_charged.as_tuple().exponent >= -2:
            #key is exchange rate and value is dollar_charged
            exchange_dict[Lower_Exchange_rated] = dollar_charged
        Lower_Exchange_rated += 1

#count the number of possible dollar charges
print("\nThere are %d possible dollar charges\n" % len(exchange_dict))

#Show the dollar charges and exchange rates
print("Here are the possible exchange rates and dollar charges")
for rate in exchange_dict:
    print(rate, exchange_dict[rate])
print('\nTHE END')
