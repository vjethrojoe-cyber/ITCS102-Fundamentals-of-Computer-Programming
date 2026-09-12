name = input("Input your name: ")
age = int(input("Input your age: "))

if age >= 0 and age <= 5 :
    print("That age is considered INFANT ")
elif age >= 6 and age <= 12 :
    print("That age is considered KID ")
elif age >= 13 and age <= 19 :
    print("That is considered TEENAGER ")
elif age >= 20 and age <= 34 :
    print("That age is considered YOUNG ADULT ")
elif age >= 35 and age <= 59 :
    print("That age is considered MIDDLE-AGED ADULT ")
elif age >= 60 :
    print("That age is considered SENIOR ")

else:
    print("AGE INVALID")
