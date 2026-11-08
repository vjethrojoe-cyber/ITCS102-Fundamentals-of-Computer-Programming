from getpass import getpass
isLogin = False
loginAttempt = 0

un = "scuderia"
pw = "sf-26"

while isLogin == False:
    uname = input("Input USERNAME: ")
    pword = input("Input PASSWORD: ")

    if uname == un and pword == pw:
        print("Successfully Login")
        print("Total Login Attempts ", loginAttempt)
    else:
        print("Login Failed")
        loginAttempt += 1
