minute = float(input("how many minutes?"))
percentage = (minute * 100) / 60 # percentage of an hr
print("%.2f"%percentage, " percentage of an hour")
mph = 100 / percentage
print("%.2f"%mph)