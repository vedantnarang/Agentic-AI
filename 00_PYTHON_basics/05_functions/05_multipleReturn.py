def make_chai():
    return "here is your chai"
return_value=make_chai()

print(return_value)

# when you return nothing then by default the function return NONE
#implicity return None

def chai_status(cups_left):
    if cups_left == 0:
        return "sorry chai over"
    return "chai is ready"

returned_value=chai_status(7)
print(returned_value)

def chai_report():
    return 100,20,10 # if we add an extra return value then we will get an error 

sold,remains,old=chai_report()
print(sold)
print(remains)
print(old)
