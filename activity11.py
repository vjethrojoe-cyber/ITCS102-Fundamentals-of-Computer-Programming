import getpass


username = "NeverGrowOld"
password = "pwede_magtanong?"

u = input("Input USERNAME ---> ")
p = getpass.getpass("Input PASSWORD ---> ")
if u == username and p == password:
    print("Access Granted")

else:
    print("Access Denied")
