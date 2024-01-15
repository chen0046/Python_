#score = 0
## f string, when mixing data types, instead of +, it can be replace by f string
#print(f"your score is {score}" )

#tip calculator

print("Welcome to the tip calculator.\n")

total_bill = float(input("What was the total bill?$\n"))
percetage_tip = int(input("What percentage tip would you like to give? 10,12 or 15?\n"))
Number_of_people = int(input("How many people to split the bill?\n"))


Tip = (percetage_tip / 100) * total_bill
Price_include_tip = Tip + total_bill
bill_per_person = Price_include_tip / Number_of_people
Final_Amount = round(bill_per_person,2)

#this changes the float number to two decimal when the result is only with one eg. 33.6 to 33.60
Final_Amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${Final_Amount}")



