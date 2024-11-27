# Prompt the user to provide their name
user_name = input("Enter name: ")

# Prompt the user to input their account number
account_number = input("Enter account number: ")

# Prompt the user to specify the loan amount and convert it to a float
principal = float(input(" Principal loan amount: "))

# Prompt the user to specify the annual interest rate and convert it to a float
interest_rate = float(input("Enter annual interest rate : "))

# Prompt the user to input the time period of the loan in years and convert it to a float
duration = float(input("Enter time in years): "))

# Calculate the simple interest using the formula SI = P * R * T / 100
simple_interest = principal * interest_rate * duration / 100

# Calculate the compound interest using the formula CI = P * [(1 + R/100)^T - 1]
compound_interest = principal * (pow((1 + interest_rate / 100), duration) - 1)

# Display the user's name
print("Account Holder Name:", user_name)

# Display the user's account number
print("Account Number:", account_number)

# Display the principal loan amount
print("Loan Amount :", principal)

# Display the calculated simple interest rounded to two decimal places
print("Simple Interest amount only: {:.2f}".format(simple_interest))

# Display the calculated compound interest rounded to two decimal places
print("Compound Interest amount only: {:.2f}".format(compound_interest))
