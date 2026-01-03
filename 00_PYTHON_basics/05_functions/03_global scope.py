chai_type="plain"


def front_desk():
    def kitchen():
        global chai_type
        chai_type="kava"
    kitchen()
    print(chai_type)


front_desk()