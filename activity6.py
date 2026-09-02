#dynamic , static
#dynamic - ever changing
#static - fixed

name = input("What is your name ? -->") #by default input would release a string type data
print("Hello ", name)

age = input("What is your age ? -->")
print("You are", age, "years old")
print(type(age)) #shows it's still a string, even though it looks like a number


#to actually use it as a number, we must convert it
age = int(age)
print(type(age)) #now it's an int

city = input("Which city do you live in ?")
print(name, "lives in", city)

favorite_number = input("Enter your favorite number --> ")
favorite_number = float(favorite_number) #convert to float type
print("Your favorite number times 2 is", favorite_number * 2)
