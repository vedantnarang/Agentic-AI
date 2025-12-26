#DICTIONARY
#key:value
chai_order=dict(type="masala chai",size="large",sugar_level=3)

print(chai_order)

chai_recipe={}
print(chai_recipe)
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"
print(chai_recipe)
del chai_recipe["liquid"]
print(chai_recipe)
print(3 in chai_recipe)
print("sugar_level" in chai_order)
print("large" in chai_order)# you can seach for the the key only  


print(chai_order.keys())
print(chai_order.values())
print(chai_order.items())
changes_in_order={"liquid":"milk","ratio":"3:1"}

chai_order.update(changes_in_order)
print(chai_order)

print(chai_order.get("size","small"))
print(chai_order.get("does not exisit","non existent property"))
print(chai_order.get("ratio"))