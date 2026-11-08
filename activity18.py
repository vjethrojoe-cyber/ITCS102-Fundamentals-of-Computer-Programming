tuloy = True

#boolean variable
tuloy = True

while tuloy == True:
    ask = input("Are you handsome? (yes / no) ---> ")

    if ask.lower() == "yes":
        print("continuing")
        continue
    else:
        print("stopping")
        break
