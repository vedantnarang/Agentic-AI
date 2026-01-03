# scopes and names 


def serve_chai():
    chai_type="masla"#local scope 
    print(f"inside function:{chai_type}")
chai_type="lemon" 
serve_chai()
print(f"outside function:{chai_type}")



def chai_counter():
    chai_order="ginger"# enclo sing scope 
    def print_order():
        chai_order="lemon"
        print(f"inner:{chai_order}")
    print_order()    

    print(f"outer:{chai_order}")

chai_order="masala"#global scope 
chai_counter()
print("global:",chai_order)