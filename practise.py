name=input("Enter your name: ")
salary=float(input("Enter your salary(ommitting currency symbol): "))
service=float(input("How many years have you been working in this company:"))
if service>=5:
    print("Congratulations, you are eligible for bonus. Your bonus amount is:",0.05*salary)
else:
    print("Sorry Your are not eligible for bonus.")