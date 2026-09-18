age = int(input("What is your age --> "))
is_employed = input("Are you currently employed --> ") == "True"
credit_score = eval(input("Your credit score --> "))
annual_income = eval(input("How much is your annual income --> "))
has_collateral = input("Do you have any collateral --> ") == "True"

if age >= 21 and is_employed == True :
    if credit_score >= 750:
        if annual_income >= 100000:
            product = "Approved at 4.5% interest rate "
        else:
            product = "Approved at 5.0% interest rate "
    elif credit_score >= 600 and credit_score <= 750:
        if has_collateral == True:
            product = "Approved at 7.0% interest rate "
        elif annual_income <= 40000:
            product = "Approved at 9.5% interest rate  "
        else:
            product = "Approved at 8.0% interest rate  "
    else:
        product = "Rejected: Credit score too low "
    print(product)
else:
    print("Rejected: Fails baseline criteria")
