#
costOfLoan=input("Enter the cost of loan ")
rate=input("Enter the rate of loan ")
years=input("How many years you will pay the loan? ")

#Converting values entered
costOfLoan=float(costOfLoan)
rate=float(rate)
years=int(years)

#Calculate monthly payment
monthlyPayment=costOfLoan*((rate*(1+rate)**years)/(1+rate)**(years-1))

print("Monthly Payment %.3f " % monthlyPayment)

#print(costOfLoan)
#print(rate)
#print(years)