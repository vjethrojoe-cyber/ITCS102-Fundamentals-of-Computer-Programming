correct_username = "jetjet"
correct_password = "haha-67"

username = input("Username: ")
password = input("Password: ")

if username != correct_username or password != correct_password:
    print("Login failed")
    exit()
print("Login successful")

loanee_name = input("Enter the loanee's first name: ")
job_description = input("Enter the loanee's job: ")

age = int(input("Input age: "))
is_employed = bool(input("Are you currently employed (True/False) "))
credit_score = int(input("Credit Score: "))
annual_income = float(input("What is your annual income: "))
has_collateral = bool(input("Do you have any collateral (True/False) "))

if has_collateral:
    collateral_name = input("Enter name/description of of collateral (e.g. motorcycle, land, house): ")
    collateral_value = float(input("Enter the value of the collateral: "))
    if collateral_value <= 30000:
        print("Invalid collateral: must be worth at least 30000 ")
        has_collateral = False

if age >= 21 and age <= 65 and is_employed == True:

     if credit_score >= 750:
         base_rate = 4.5 if annual_income >= 100000 else 5.0
     elif credit_score >= 600 and credit_score <= 750:
        if has_collateral == True:
             base_rate = 7.0
        elif annual_income <= 40000:
             base_rate = 9.5
        else:
             base_rate = 8.0
     else:
         base_rate = None

     if base_rate is not None:
         loan_amount = float(input("How much would you like to loan? "))
         print(f"\nLoanee: {loanee_name} ({job_description})")
         print(f"Loan amount: {loan_amount}")
         print(f"Interest rate: {base_rate}%")
     else:
         print("Rejected: Credit score too low")
else:
    print("Rejected: Fails baseline criteria")
