income = float(input("Enter the annual income: "))
tax_relief = 556.2

if income <= 3089:
    tax = 0.0
#tax below 85528 is 18% of the income minus tax relief
elif income < 85528:
    tax =income * .18 - tax_relief
#tax above 85528 is 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers
elif income >= 85528:
    tax = 14839.02 + (income - 85528) * .32

tax = round(tax, 0)
print("The tax is:", tax, "thalers")