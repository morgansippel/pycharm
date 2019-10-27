#   Monthly wage
baseWage = float(input("What is your base wage"))
salesMonth = float(input( "How much were you able to sell?"))
commision = float(input("How much is your commission?"))
totalAmount = baseWage + (salesMonth*commision/100)
print("You earned: \t", totalAmount , " this month.")