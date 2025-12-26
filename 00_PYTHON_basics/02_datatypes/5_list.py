#lists are mutable
# just like arrays but in python we call them arrays 

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients. remove("water")
print(f"Ingredients are: {ingredients}")
spices=["cardamom","cinnamon"]

ingredients.extend(spices)

print(ingredients)


ingredients.insert(3,"tea leaves")
print(ingredients)


ingredients.pop()#last se remove
print(ingredients)


#reverse 
ingredients.reverse()
print(ingredients)

#sort

ingredients.sort()
print(ingredients)#alphabetically 

print(max(ingredients))

sugar_levels=[1,2,3,4,5]
print(max(sugar_levels))
print(min(sugar_levels))

satisfaction_levels=[1,2,3,4,5,6,7,8,9,10]
#operation overloading
print(sugar_levels+satisfaction_levels)


strong_coffee=["coffee","water"]

# byte array 
#it return a new array of bytes ...it is mutable sequence
raw_spice_data = bytearray(b"CINNAMON")
print(raw_spice_data)
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(raw_spice_data)



