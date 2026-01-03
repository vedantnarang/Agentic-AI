
value=15

def update_order():
    chai_type="elaichi"
    def kitchen():
        nonlocal chai_type
        nonlocal value# shows error
        chai_type="kesar"
    kitchen()
    print("after kitchen update",chai_type)


update_order()    

#non local ke liye outer function mien uss name se variable hon ajaruri hai 