# chai="ginger chai"


# def prepare_chai(order):
#     print("preparing ",order)

# prepare_chai(chai)

chai=[1,2,3]

def edit_chai(cup):# cup is parameters
    cup[1]=42

edit_chai(chai)#chai here is arguement 
print(chai)# chai array is changeed now 


#ARGS

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("ginger",True,"low")#positional
make_chai(tea="ginger",sugar="low",milk=True) #using keywords


def special_chai(*ingredients,**extras):
    print("ingredients:",ingredients)
    print("extras:",extras)

special_chai("ginger","lemon",sweetener="honey",size="medium")    
#the arguements which have * will be stored as a tuple and also you do not have to give name to these arguements
# #teh arguemnets with ** are stored as a dictionary and you have to give name to these arguements 

def chai_orders(order=[]):
    order.append("masala")
    print(order)

chai_orders()
chai_orders()



