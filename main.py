# input statements
salary = 1250
numDependents = 5

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * 0.025 * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
print("State Tax: $" + str(round(stateTax, 2)))
print("Federal Tax: $" + str(round(federalTax, 2)))
print("Dependants: $" + str(round(dependentDeduction, 2)))
