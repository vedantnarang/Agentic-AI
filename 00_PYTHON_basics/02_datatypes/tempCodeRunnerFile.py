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

print(chai_order.items())