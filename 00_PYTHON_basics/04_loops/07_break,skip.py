#continue skips one loop 
#break makes you come out of the loop 


flavours=["ginger","outosstock","tulsi","dicountinued","lemon"]

for flavour in flavours:
    if(flavour=="outosstock"):
        continue
    if(flavour=="dicountinued"):
        break
    print(f"{flavour} item found")

print("outof loop")



staff = [("Amit", 16), ("Zara", 17), ("Raj", 15) ]

for name, age in staff:
    if age <= 18:
    print(f"{name} is eligible to manage the staff")
    break

print(f"No one is eligible to manage the staff")