snack=input("enter what you want to have :").lower()


print(f"user said:{snack}")

if snack=="cookie" or snack=="samosa":
    print(f"{snack} will be served at your table")
else:
    print("unavailable")