import sys

#Request Rental code from user input 
rentalCode = input('(B)udget, (D)aily, or (W)eekly rental?\n')


#Request time period the car was rented.
if rentalCode == 'B' or rentalCode == 'D':
  
  rentalPeriod = int(input("Number of Days Rented:\n"))
else:
    rentalPeriod = int(input("Number of Weeks Rented:\n"))


#print statements to debug code in early steps ||commented out
#print(rentalCode)
#print(rentalPeriod)

#Pricing
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00


##Set the base charge for the rental type as the variable baseCharge. 
#The base charge is the rental period * the appropriate rate:

if rentalCode == 'B':
    baseCharge = rentalPeriod * budget_charge
elif rentalCode == 'D':
    baseCharge = rentalPeriod * daily_charge
elif rentalCode == 'W':
  baseCharge = rentalPeriod * weekly_charge

##2 decimal places to the right, threw error w/out it. Expected had 2 decimal point shown 
#without it 300.0 was wrong and 300.00 was expected
#print('%.2f' % baseCharge)


#Collect Mileage information odoStart

odoStart = input('Starting Odometer Reading:\n')

#Collect Mileage information odoEnd
odoEnd = input('Ending Odometer Reading:\n')

#Calculate total miles with int 
totalMiles = int(odoEnd) - int(odoStart)

#Print odoStart, odoEnd and totalMiles
#print(odoStart)
#print(odoEnd)
#print(totalMiles)



##Calculate the mileage charge and store it as the variable mileCharge:
#Code 'B' (budget) mileage charge: $0.25 for each mile driven
if rentalCode == 'B':
  mileCharge = 0.25 * totalMiles

#Calculate daily mileage charge: no charge if the average
#number of miles driven per day is 100 miles or less;
#If averageDayMiles is above the 100 mile per day
# calculate extraMiles (averageDayMiles  - 100)
# mileCharge is the charge for extraMiles, 0.25 for each mile
if rentalCode == 'D':
  averageDayMiles = int(totalMiles) / int(rentalPeriod)
  if averageDayMiles <= 100:
    totalMiles = 0
  elif averageDayMiles > 100:
    extraMiles = float(averageDayMiles - 100)
  mileCharge = 0.25 * extraMiles 

#Calculate Weekly mileage charge 
#no charge if the average number of miles driven per week is 900 miles or less;
#Calculate the averageWeekMiles (totalMiles/ rentalPeriod)
#	mileCharge is $100.00 per week if the average number of miles driven per week exceeds 900 miles
averageDayMiles = int(totalMiles) / int(rentalPeriod)
if rentalCode == 'W' and averageDayMiles > 900:
  mileCharge = rentalPeriod * 100
elif rentalCode == 'W' and averageDayMiles <= 900:
  mileCharge = 0

 #printstatements & amount due
amtDue = float(baseCharge) + (mileCharge)
print('Rental Summary')
print('Rental Code: ' + str(rentalCode))
print('Rental Period: ' + str(rentalPeriod))
print('Starting Odometer: ' + str(odoStart))
print('Ending Odometer: ' + str(odoEnd))
print('Miles Driven: ' + str(totalMiles))
#print('Amount Due: ' + '${:,.2f}'.format(amtDue)
print('Amount Due: $' + '%.2f' % amtDue)