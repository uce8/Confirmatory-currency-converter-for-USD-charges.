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

#initialise a list for collecting the possible exchage rates
Dollar_charged_list = []
#initialise the possible exchange rates list
Exchange_rate_list = []

while not Lower_Exchange_rated > Higher_Exchange_rated:
        dollar_charged = Naira_charged/Lower_Exchange_rated
        if dollar_charged.as_tuple().exponent >= -2:
            Dollar_charged_list.append(dollar_charged)
            Exchange_rate_list.append(Lower_Exchange_rated)
        Lower_Exchange_rated += 1

#count the number of possible dollar charges
print("There are %d possible dollar charges" % len(Dollar_charged_list))

#Show the dollar charges and exchange rates
print("Here are the possible exchange rates and dollar charges")
n = 0
while n < len(Dollar_charged_list):
    print(" %g: %g" %(float(Exchange_rate_list[n]), float(Dollar_charged_list[n])))
    n += 1
print('THE END')
