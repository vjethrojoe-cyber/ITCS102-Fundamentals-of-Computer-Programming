
mcu = []

isContinue = True

while isContinue == True:
    ans = input("Do you know any mcu movie? (yes / no)").lower()

    if ans == "yes":
        title = input("What is the title of the mcu movie?:")
        mcu.append(title)
        ans = input("Do you wish to continue? (yes / no)").lower()
        if ans == "yes":
            print("Continue")
            continue
        else:
            print("Stop")
            break
