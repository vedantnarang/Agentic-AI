# types of comprehensions : list ,set ,dictionary ,and generator

# list comprehensions

menu=["masala","green","blue","ginger","iced lemon","iced peach"]

iced_tea=[tea for tea in menu if len(tea)<10]
print(iced_tea)