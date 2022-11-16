print("Welcome to the Tip Calculator/n")
bill = input("What was the total bill? ")
tip = input("What percentage of tips would you like to give? ")
people = input("With how many people do you want to split? ")

percentage = (float(bill) * float(tip)) / 100
pay_per_person = float(bill) / float(people)
all_bill_whith_tips = pay_per_person + percentage / float(people)
round_number = round(all_bill_whith_tips)
print(f"Each person should pay {round_number:.2f}")
