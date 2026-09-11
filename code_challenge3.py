print("PALAWAN EXPRESS")

name = input("name --> ")
type_of_item = input("type of item --> ")
is_Fragile = input("is the item fragile? Yes or No --> ") == "Yes"

print("MORE INFORMATIONS")

is_Express = input("is this express delivery? Yes or No --> ") == "Yes"
is_International = input("is this delivery from international? Yes or No --> ") == "Yes"
weight = float(input("weight in kg --> "))
distance = float(input("distance in km --> "))
base_cost = (weight * 2.50) + (distance * 0.15)
total = base_cost

if weight <= 2.0 and distance <= 100 and not is_Express and not is_International:
    total = 0.00
    tier = "Free Shipping"
elif is_International and is_Express:
    total = (base_cost * 1.40) + 50
    tier = "International Express"
elif is_Express or (is_International and weight > 20):
    total = (base_cost * 1.20) + 25
    tier = "Express or Heavy International"
elif weight > 30 or distance > 1000:
    total = base_cost + 30
    tier = "Oversized"
else:
    total = base_cost
    tier = "Standard Rate"


print("Tier:", tier)
print("Base Cost:", base_cost)
print("Total:", total)
