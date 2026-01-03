#pure vs impure functions
#PURE - these are the functions whhich do not change any of teh gloabal variables 
def pure_chai(cups):
    return cups*10
#IMPURE- these are the functions whhich change any of the gloabal variables 

total_chai=0
def impure_chai():
    global total_chai
    total_chai=total_chai*10
    return total_chai


