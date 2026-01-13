# set comprehension


favourite_chais=[
    "masala chai",
    "lemon tea",
    "green tea",
    "elaichi chai",
    "masala chai"
]

unique_chai={chai for chai in favourite_chais}
print(unique_chai)



recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}
unique_spices=[spice for ingriedients in recipes.values() for spice in ingriedients]
print(unique_spices)# gives us all the unique ingriedients