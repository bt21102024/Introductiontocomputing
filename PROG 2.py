GI = int(input("Enter Gross income: "))

SD = 10000

NOD = int(input("Enter Number of dependents: "))

TI = GI-SD-(3000*NOD)

Tax = TI*0.2

print("Person's Income tax:", Tax)
