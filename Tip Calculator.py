print("Welcome to the tip Calculator")
bill=float(input("Enter amount of bill:"))
tip=float(input("Enter percent of tip[10,12,15]:"))
person=int(input("Enter number of persons for bill:"))
individual_bill=bill/person
individual_tip=((tip/100)*bill)/person
total_bill=individual_bill+individual_tip
Final_amount=round(total_bill,2)
print(f"Individual person payment:{Final_amount}")
