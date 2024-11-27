# Step 1: Initialize account details with default balance
bank_name = "US Bank"
account_id = 123456
current_balance = 0
account_info = {
    "bank_name": bank_name,
    "account_id": account_id,
    "balance": current_balance
}

# Step 1: Print account details in a readable format
print(f"Bank Name: {bank_name}")
print(f"Account Number: {account_id}")
print(f"Current Balance: {current_balance}")

# Step 2: Accept an initial deposit amount from the user
deposit_amount = int(input("Enter the amount to deposit initially: "))
account_info["balance"] += deposit_amount
print("Balance after initial deposit:", account_info["balance"])

# Step 3: Add a monthly salary credit of 3300
monthly_salary = 3300
account_info["balance"] += monthly_salary
print("Balance after salary credit:", account_info["balance"])

# Step 4: Deduct for an online transaction of 33.33
online_expense = 33.33
account_info["balance"] -= online_expense
print("Balance after online purchase:", account_info["balance"])

# Step 5: Deduct for house rent payment of 1500
rent_payment = 1500
account_info["balance"] -= rent_payment
print("Balance after rent payment:", account_info["balance"])
